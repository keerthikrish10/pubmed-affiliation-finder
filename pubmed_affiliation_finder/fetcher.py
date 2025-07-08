from typing import List
import requests
from xml.etree import ElementTree as ET
from .utils import get_logger

logger = get_logger()

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    try:
        res = requests.get(f"{BASE_URL}/esearch.fcgi", params=params, timeout=10)
        res.raise_for_status()
        return res.json().get("esearchresult", {}).get("idlist", [])
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch PubMed IDs: {e}")
        return []

def fetch_pubmed_metadata(pubmed_ids: List[str]) -> ET.Element:
    if not pubmed_ids:
        return ET.Element("Empty")

    id_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": id_str,
        "retmode": "xml"
    }
    try:
        res = requests.get(f"{BASE_URL}/efetch.fcgi", params=params, timeout=10)
        res.raise_for_status()
        return ET.fromstring(res.content)
    except requests.exceptions.RequestException as e:
        logger.error(f"Failed to fetch PubMed metadata: {e}")
    except ET.ParseError as e:
        logger.error(f"Failed to parse PubMed XML: {e}")

    return ET.Element("Empty")
