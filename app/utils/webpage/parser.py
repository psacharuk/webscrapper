from bs4 import BeautifulSoup

def parse_content(content):
    soup = BeautifulSoup(content, 'html.parser')
    head = clean_text(soup.find('head').get_text()) if soup.find('head') else None
    body_headers = [clean_text(heading.text) for heading in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6']) if clean_text(heading.text) != '']

    footer = clean_text(soup.find('footer').get_text()) if soup.find('footer') else None

    return head, body_headers, footer

def clean_text(text):
    return text.replace('\n', ' ').strip()