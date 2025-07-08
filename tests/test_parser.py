import xml.etree.ElementTree as ET
from pubmed_affiliation_finder.parser import parse_pubmed_xml

def test_parse_pubmed_xml_valid_article():
    xml = """
    <PubmedArticleSet>
        <PubmedArticle>
            <MedlineCitation>
                <PMID>123456</PMID>
                <Article>
                    <ArticleTitle>Sample Title</ArticleTitle>
                    <AuthorList>
                        <Author>
                            <LastName>Smith</LastName>
                            <ForeName>Jane</ForeName>
                            <AffiliationInfo>
                                <Affiliation>Test Pharma Inc., California, USA. jane.smith@testpharma.com</Affiliation>
                            </AffiliationInfo>
                        </Author>
                    </AuthorList>
                </Article>
                <PubDate>
                    <Year>2023</Year>
                </PubDate>
            </MedlineCitation>
        </PubmedArticle>
    </PubmedArticleSet>
    """
    root = ET.fromstring(xml)
    articles = parse_pubmed_xml(root)

    assert len(articles) == 1
    assert articles[0]['pmid'] == "123456"
    assert articles[0]['title'] == "Sample Title"
    assert articles[0]['pub_date'] == "2023"
    assert "Jane Smith" in [a['name'] for a in articles[0]['authors']]
    assert articles[0]['email'] == "jane.smith@testpharma.com"
