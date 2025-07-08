import typer
import os
from pubmed_affiliation_finder.fetcher import fetch_pubmed_ids, fetch_pubmed_metadata
from pubmed_affiliation_finder.parser import parse_pubmed_xml
from pubmed_affiliation_finder.affiliation_checker import identify_non_academic_authors
from pubmed_affiliation_finder.exporter import export_to_csv, print_to_console
from pubmed_affiliation_finder.utils import setup_logging, get_logger
from dotenv import load_dotenv
from pathlib import Path
load_dotenv()
app = typer.Typer()
logger = get_logger()

# Load environment variables at the top level
load_dotenv()

@app.command()
def main(
    query: str,
    file: str = typer.Option(None, "--file", "-f", help="Output CSV filename."),
    debug: bool = typer.Option(False, "--debug", "-d", help="Enable debug output."),
    no_llm: bool = typer.Option(False, "--no-llm", help="Disable LLM fallback.")
):
    setup_logging(debug)

    # Ensure API key is set
    if not no_llm and not os.getenv("GOOGLE_API_KEY"):
        logger.error("❌ GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")
        raise typer.Exit(code=1)

    try:
        typer.echo(f"🔍 Searching PubMed for: '{query}'")
        ids = fetch_pubmed_ids(query)
        if not ids:
            logger.warning("⚠️ No PubMed IDs found. Please refine your query.")
            raise typer.Exit(code=1)

        xml_data = fetch_pubmed_metadata(ids)
        articles = parse_pubmed_xml(xml_data)

        results = []
        for article in articles:
            authors = article.get("authors", [])
            non_acad_authors, companies = identify_non_academic_authors(
                authors, debug=debug, use_llm=not no_llm
            )

            if non_acad_authors:
                results.append({
                    "PubmedID": article.get("pmid"),
                    "Title": article.get("title"),
                    "Publication Date": article.get("pub_date"),
                    "Non-academic Author(s)": "; ".join(non_acad_authors),
                    "Company Affiliation(s)": "; ".join(companies),
                    "Corresponding Author Email": article.get("email") or ""
                })

        if file:
            export_to_csv(results, file)
            typer.echo(f" Saved {len(results)} result(s) to: {file}")
        else:
            print_to_console(results)

    except KeyboardInterrupt:
        typer.echo(" Interrupted by user. Exiting.")
        raise typer.Exit(code=1)

    except Exception as e:
        logger.error(f" Unexpected error: {e}")
        raise typer.Exit(code=1)


if __name__ == "__main__":
    app()
