# cli.py

import typer
from dotenv import load_dotenv
from pubmed_affiliation_finder.fetcher import fetch_pubmed_ids, fetch_pubmed_metadata
from pubmed_affiliation_finder.parser import parse_pubmed_xml
from pubmed_affiliation_finder.affiliation_checker import identify_non_academic_authors
from pubmed_affiliation_finder.exporter import export_to_csv, print_to_console
from pubmed_affiliation_finder.utils import setup_logging

app = typer.Typer()

@app.command()
def main(
    query: str,
    file: str = typer.Option(None, "--file", "-f", help="Output CSV filename."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output."),
    no_llm: bool = typer.Option(False, "--no-llm", help="Disable LLM fallback.")
):
    # ✅ This is correct: configure logging level
    setup_logging(debug)

    load_dotenv()

    print("🔍 Searching PubMed for:", query)
    ids = fetch_pubmed_ids(query)
    xml_data = fetch_pubmed_metadata(ids)
    articles = parse_pubmed_xml(xml_data)

    results = []
    for article in articles:
        authors = article["authors"]
        non_acad_authors, companies = identify_non_academic_authors(authors, debug=debug, use_llm=not no_llm)

        if non_acad_authors:
            results.append({
                "PubmedID": article["pmid"],
                "Title": article["title"],
                "Publication Date": article["pub_date"],
                "Non-academic Author(s)": "; ".join(non_acad_authors),
                "Company Affiliation(s)": "; ".join(companies),
                "Corresponding Author Email": article["email"]
            })

    if file:
        export_to_csv(results, file)
        print(f"✅ Saved {len(results)} results to {file}")
    else:
        print_to_console(results)

# ✅ Typer entry point
if __name__ == "__main__":
    app()
