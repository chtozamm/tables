from typing import List
from bs4 import BeautifulSoup


def parse_html_table(html_content: str) -> tuple[List, List[List[str]]]:
    headers = extract_html_table_headers(html_content)
    data = extract_html_table_data(html_content)
    return (headers, data)


def extract_html_table_headers(html_content: str) -> List[str]:
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the <table> element
    table = soup.find("table")
    if table is None:
        raise Exception("No <table> element found in the HTML.")

    # Find the <thead> element
    thead = table.find("thead")
    if thead is None:
        raise Exception("No <thead> element found in the HTML.")

    # Find the <tr> element inside the <thead> element
    tr = thead.find("tr")
    if tr is None:
        raise Exception("No <tr> element found inside the <thead>.")

    # Find all the <th> elements inside the <tr> element
    th_elements = tr.find_all("th")
    if not th_elements:
        raise Exception("No <th> elements found inside the <tr>.")

    # Extract the table headers into a list of strings
    headers = [th.get_text(strip=True) for th in th_elements]
    return headers


def extract_html_table_data(html_content: str) -> List[List[str]]:
    # Create a BeautifulSoup object to parse the HTML
    soup = BeautifulSoup(html_content, "html.parser")

    # Find the <table> element
    table = soup.find("thead")
    if table is None:
        raise Exception("No <table> element found in the HTML.")

    tbody = soup.find("tbody")
    if tbody is None:
        raise Exception("No <tbody> element found in the HTML.")

    # Find the <tr> elements inside the <tbody> element
    tr_elements = tbody.find_all("tr")
    if not tr_elements:
        raise Exception("No <tr> elements found inside the <tbody>.")

    # Extract table data
    table_data = []
    for tr in tr_elements:
        td_elements = tr.find_all("td")
        if td_elements:
            row_data = [td.get_text(strip=True) for td in td_elements]
            table_data.append(row_data)

    return table_data
