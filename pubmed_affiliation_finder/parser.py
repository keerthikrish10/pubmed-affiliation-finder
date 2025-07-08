from typing import List, Dict, Optional
import xml.etree.ElementTree as ET
import re
from .utils import get_logger

logger = get_logger()

def extract_email_for_author(name: str, affiliation: str) -> Optional[str]:
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", affiliation)
    if email_match:
        email = email_match.group(0)
        name_parts = name.lower().split()
        if any(part in email.lower() for part in name_parts):
            return email
    return None

def extract_email_by_company(affiliation: str) -> Optional[str]:
    email_match = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", affiliation)
    if not email_match:
        return None

    email = email_match.group(0)
    domain_part = email.split("@")[1].split(".")[0].lower()
    user_part = email.split("@")[0].lower()

    affil_clean = re.sub(r"[^a-zA-Z0-9 ]", " ", affiliation).lower()
    affil_words = set(affil_clean.split())

    if domain_part in affil_words or user_part in affil_words:
        return email
    return None

def parse_pubmed_xml(xml_root: ET.Element) -> List[Dict]:
    articles = []

    for article in xml_root.findall(".//PubmedArticle"):
        try:
            pmid = article.findtext(".//PMID")
            title = article.findtext(".//ArticleTitle")
            pub_date = article.findtext(".//PubDate/Year") or "Unknown"
            authors = []
            corresponding_email = ""

            for author in article.findall(".//Author"):
                lastname = author.findtext("LastName") or ""
                forename = author.findtext("ForeName") or ""
                affil = author.findtext(".//AffiliationInfo/Affiliation")

                if forename and lastname and affil:
                    full_name = f"{forename} {lastname}"
                    authors.append({
                        "name": full_name,
                        "affiliation": affil
                    })

                    if not corresponding_email:
                        email = extract_email_for_author(full_name, affil)
                        if not email:
                            email = extract_email_by_company(affil)

                        if email:
                            corresponding_email = email

            articles.append({
                "pmid": pmid or "N/A",
                "title": title or "No Title",
                "pub_date": pub_date,
                "authors": authors,
                "email": corresponding_email
            })

        except Exception as e:
            logger.warning(f"Error parsing article: {e}")
            continue

    return articles
