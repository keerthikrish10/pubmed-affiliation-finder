# pubmed_affiliation_finder/fetcher.py

from typing import List
import requests
from xml.etree import ElementTree as ET

BASE_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"

def fetch_pubmed_ids(query: str, max_results: int = 20) -> List[str]:
    params = {
        "db": "pubmed",
        "term": query,
        "retmax": max_results,
        "retmode": "json"
    }
    res = requests.get(f"{BASE_URL}/esearch.fcgi", params=params)
    res.raise_for_status()
    return res.json()["esearchresult"]["idlist"]

def fetch_pubmed_metadata(pubmed_ids: List[str]) -> ET.Element:
    id_str = ",".join(pubmed_ids)
    params = {
        "db": "pubmed",
        "id": id_str,
        "retmode": "xml"
    }
    res = requests.get(f"{BASE_URL}/efetch.fcgi", params=params)
    res.raise_for_status()
    return ET.fromstring(res.content)
