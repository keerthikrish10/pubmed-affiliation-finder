import re
import json
from typing import Optional, Tuple
from .utils import get_logger
import google.generativeai as genai
from functools import lru_cache
from dotenv import load_dotenv
import os

# Load environment variables (e.g. GOOGLE_API_KEY)
load_dotenv()

# Configure Gemini API key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

logger = get_logger()

NON_ACADEMIC_KEYWORDS = [
    "inc", "pharma", "biotech", "gmbh", "ltd", "llc", "corp",
    "therapeutics", "biosciences", "laboratories", "research center",
    "diagnostics", "healthcare", "lifesciences", "medtech"
]

ACADEMIC_KEYWORDS = [
    "university", "college", "institute", "department", "faculty",
    "school of", "hospital", "centre for", "ministry", "public health",
    "clinic", "national lab"
]


def is_non_academic_rule_based(affiliation: str) -> bool:
    affil_clean = re.sub(r"[^\w\s]", "", affiliation.lower())
    if any(kw in affil_clean for kw in ACADEMIC_KEYWORDS):
        return False
    return any(kw in affil_clean for kw in NON_ACADEMIC_KEYWORDS)


# Caching the LLM classification results for repeated affiliations
@lru_cache(maxsize=512)
def classify_affiliation_llm_cached(affil: str) -> str:
    """
    Helper function for caching. Wraps the original classify logic and returns JSON string.
    """
    prompt = f"""
You're an expert at analyzing research author affiliations. Given the affiliation below, answer whether it's from a pharmaceutical, biotech, or private healthcare company.

Affiliation: "{affil}"

Please reply with only this strict JSON (no markdown, no comments):

{{
  "is_non_academic": true | false,
  "company_name": "Company Name if non-academic, else null"
}}
"""
    model = genai.GenerativeModel("gemini-pro")
    response = model.generate_content(prompt)
    raw = response.text.strip()
    json_part = raw[raw.find("{"):raw.rfind("}")+1]
    return json_part


def classify_affiliation_llm(affiliation: str, debug: bool = False) -> Tuple[bool, Optional[str]]:
    try:
        json_part = classify_affiliation_llm_cached(affiliation)
        result = json.loads(json_part)

        if debug:
            logger.debug(f"LLM result for '{affiliation}': {result}")

        return result.get("is_non_academic", False), result.get("company_name")
    except Exception as e:
        logger.error(f"LLM classification failed for '{affiliation}': {e}")
        return False, None


def identify_non_academic_authors(authors, debug: bool = False, use_llm: bool = True):
    non_academic_authors = []
    companies = set()

    for author in authors:
        name = author.get("name")
        affil = author.get("affiliation")

        if not name or not affil:
            continue

        is_non_academic = is_non_academic_rule_based(affil)
        company = None

        if not is_non_academic and use_llm:
            is_non_academic, company = classify_affiliation_llm(affil, debug)

        if is_non_academic:
            non_academic_authors.append(name)
            companies.add(company or affil)

        if debug:
            logger.debug(f"Checked author: {name}")
            logger.debug(f"Affiliation: {affil}")
            logger.debug(f"→ Non-academic: {is_non_academic}")
            if company:
                logger.debug(f"→ Company: {company}")

    return non_academic_authors, list(companies)
