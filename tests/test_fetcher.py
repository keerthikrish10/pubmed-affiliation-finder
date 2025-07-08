from pubmed_affiliation_finder.fetcher import fetch_pubmed_ids

def test_fetch_pubmed_ids_returns_list():
    ids = fetch_pubmed_ids("covid vaccine", max_results=5)
    assert isinstance(ids, list)
    assert len(ids) <= 5
