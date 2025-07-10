# 🧠 PubMed Affiliation Finder CLI Tool

<div align="center">
  <a href="https://github.com/your_username/pubmed-affiliation-finder">
    <img src="https://img.shields.io/badge/PubMed-Parser-blue?style=for-the-badge&logo=pubmed" alt="PubMed Logo">
  </a>

  <h3 align="center">🔬 Identify Industry Contributors in Scientific Papers</h3>

  <p align="center">
    A Fast and Intelligent CLI tool to search PubMed, extract author affiliations, and detect non-academic contributors using rule-based heuristics + Google Gemini LLM.
    <br />
    <a href="https://github.com/your_username/pubmed-affiliation-finder"><strong>📚 Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/your_username/pubmed-affiliation-finder">🚀 Run Demo</a>
    ·
    <a href="https://github.com/your_username/pubmed-affiliation-finder/issues">🐛 Report Bug</a>
    ·
    <a href="https://github.com/your_username/pubmed-affiliation-finder/issues">💡 Request Feature</a>
  </p>
</div>

---

## 📋 Table of Contents

<details>
<summary>Click to expand</summary>

- [🎯 About The Project](#-about-the-project)
  - [✨ Key Features](#-key-features)
  - [🏗️ Built With](#-built-with)
- [🚀 Getting Started](#-getting-started)
  - [✅ Prerequisites](#-prerequisites)
  - [⚙️ Installation](#️-installation)
- [🧠 Usage](#-usage)
- [🧪 Run From TestPyPI](#run-from-testpypi)
- [📄 Project Structure](#-project-structure)
- [🛠️ Roadmap](#-roadmap)
- [🤝 Contributing](#-contributing)
- [📬 Contact](#-contact)
- [📄 License](#-license)

</details>

---

## 🎯 About The Project

This tool allows researchers and analysts to:

- Query PubMed with keywords  
- Fetch metadata and author affiliations  
- Use **rule-based heuristics** + **Google Gemini Pro** to detect pharma, biotech, or healthcare contributors  
- Export the results to a **CSV** or print to console
- Published to testPYPI as a package
- Git for version control
- Pytest for unit testing
- Fine tuned LLM using one-shot prompt tuning

### ✨ Key Features

| Feature | Description |
|--------|-------------|
| 🔍 PubMed Search | Query papers using any keyword |
| 🧠 LLM Integration | Uses Google Gemini API to classify affiliation |
| GIT | For version control |
| 🏥 Industry Detector | Identifies Public and  private sector companies in research |
| 📊 CSV Export | Save structured results for analysis |
| 🐍 CLI Powered | Fast and customizable Typer-based CLI |
| 📄 .env Support | Gemini API key via environment variables |
| PYPI | Publishd to testPYPI as a package|
| PYTest | for unit testing |
|-h or --help| Display usage instructions|
|-d or --debug| Print debug information during execution|
|-f or --file| Specify the lename to save the results|
|One-shot prompt tuning | fine tuning of LLM |

---

## 🏗️ Built With

<div align="center">

| Tool | Purpose | Badge |
|------|---------|-------|
| [**Typer**](https://typer.tiangolo.com/) | CLI Framework | ![Typer](https://img.shields.io/badge/Typer-FastAPI%20CLI-teal?logo=fastapi&logoColor=white) |
| [**Google Gemini API**](https://ai.google.dev/gemini-api/docs) | LLM for classification | ![Gemini](https://img.shields.io/badge/Gemini-LLM-yellow?logo=google) |
| [**Pandas**](https://pandas.pydata.org/) | CSV handling | ![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-blue) |
| [**Requests**](https://requests.readthedocs.io/) | API calls | ![Requests](https://img.shields.io/badge/HTTP-requests-green) |
| [**python-dotenv**](https://pypi.org/project/python-dotenv/) | Env var loader | ![dotenv](https://img.shields.io/badge/Env-python--dotenv-lightgrey) |

</div>

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.11 or higher
- A [Google Gemini API Key](https://ai.google.dev/gemini-api/docs)
-  [Poetry](https://python-poetry.org/)

### ⚙️ Installation

#### step -1: With `pip`

```bash
git clone https://github.com/your_username/pubmed-affiliation-finder.git
cd pubmed-affiliation-finder
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt

#### step -2: With 'Poetry'

poetry install
poetry shell
Create a .env file at the root:
GOOGLE_API_KEY=your_google_api_key

#### 🧠 Usage from local machine

#### with Poetry:

poetry run get-papers-list "covid vaccine 2023" --file results.csv --debug

#### 🧪 Run From TestPyPI
#### To test from the cloud:

pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple pubmed-affiliation-finder
Then run:

python -m pubmed_affiliation_finder.cli "covid vaccine 2023" --file result.csv
                (OR)
get-papers-list "cancer vaccine 2024" --file result.csv --debug

#### Unit Testing iwth PYTEST:

From your terminal, run:

pip install -e .

 Run All Tests:

set PYTHONPATH=.
pytest tests/

#### Version Control using GIT commands:

cd C:\Users\KEERTHI KRISHANA\OneDrive\Documents\Pubmed_paper_fetcher_tool
git init

Create a .gitignore file

git remote add origin https://github.com/your-username/pubmed-affiliation-finder.git

git add .
git commit -m "Initial commit: PubMed affiliation finder tool"

git branch -M main
git push -u origin main


#### Flag	Description:

--debug	Show detailed logs
--no-llm	Disable Gemini fallback
--file	Save results to CSV

#### 📄 Project Structure

Pubmed_paper_fetcher_tool/
├── pubmed_affiliation_finder/
│   ├── __init__.py
│   ├── parser.py
│   ├── fetcher.py
│   ├── affiliation_checker.py
│   ├── utils.py
├── tests/
│   ├── __init__.py
│   ├── test_parser.py
│   ├── test_fetcher.py
│   ├── test_checker.py
├── pyproject.toml or requirements.txt


#### 🛠️ Roadmap:

 Fetch and parse PubMed metadata

 Rule-based affiliation filtering

 Gemini API fallback integration

 CLI tool with Typer

 Export to CSV

 Test suite & coverage

 Test PYPI deployment

#### 🤝 Contributing:

Contributions are welcome!

Fork the repo

Create your feature branch (git checkout -b feature/new-feature)

Commit changes (git commit -m 'Add new feature')

Push to GitHub (git push origin feature/new-feature)

Create a pull request

#### 📬 Contact
<div align="center">
Keerthi Krishna
🎓 AI/ML Engineer — VIT Chennai
📧 skeerthi.krish@gmail.com

</div>

#### 📄 License
Distributed under the MIT License.

<div align="center"> <strong>⭐ If you found this tool helpful, give it a star on GitHub!</strong><br/> <img src="https://api.star-history.com/svg?repos=your_username/pubmed-affiliation-finder&type=Date" width="600"/> </div> ```
