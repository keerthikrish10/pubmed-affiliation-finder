from pubmed_affiliation_finder.affiliation_checker import (
    is_non_academic_rule_based,
    identify_non_academic_authors
)

def test_is_non_academic_rule_based():
    assert is_non_academic_rule_based("Moderna Therapeutics Inc.") is True
    assert is_non_academic_rule_based("Harvard University") is False

def test_identify_non_academic_authors_mixed():
    authors = [
        {"name": "Alice Johnson", "affiliation": "Moderna Inc., Boston"},
        {"name": "Bob Lee", "affiliation": "Stanford University, CA"}
    ]
    non_acads, companies = identify_non_academic_authors(authors, use_llm=False)
    assert "Alice Johnson" in non_acads
    assert "Bob Lee" not in non_acads
    assert any("Moderna" in c for c in companies)
