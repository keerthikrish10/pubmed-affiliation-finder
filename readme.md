# PubMed Affiliation Finder 🔬

A CLI tool to fetch PubMed research papers with at least one non-academic author (pharma/biotech). Uses Gemini Pro LLM + heuristics.

## 🚀 Features
- Fetches data from PubMed using query
- Extracts author affiliations
- Detects biotech/pharma companies using rules + Gemini LLM
- Outputs as CSV or table

## 🧪 Setup
```bash
poetry install
touch .env  # Add GEMINI_API_KEY=your-key-here
