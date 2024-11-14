from typing import List


def construct_html_table(
    headers: List[str], data: List[List[str]], indent: int = 4
) -> str:
    """
    Constructs an HTML table from headers and data.
    """
    if not isinstance(headers, list) or not all(isinstance(h, str) for h in headers):
        raise ValueError("Headers must be a list of strings.")
    if not isinstance(data, list) or not all(isinstance(row, list) for row in data):
        raise ValueError("Data must be a list of lists.")

    table_parts = ["<table>"]
    indent_str = " " * indent

    # Reconstruct the <thead>
    table_parts.append(f"{indent_str}<thead>")
    table_parts.append(f"{indent_str * 2}<tr>")
    for header in headers:
        table_parts.append(f"{indent_str * 3}<th>{header}</th>")
    table_parts.append(f"{indent_str * 2}</tr>")
    table_parts.append(f"{indent_str}</thead>")

    # Reconstruct the <tbody>
    table_parts.append(f"{indent_str}<tbody>")
    for row in data:
        table_parts.append(f"{indent_str * 2}<tr>")
        for cell in row:
            table_parts.append(f"{indent_str * 3}<td>{cell}</td>")
        table_parts.append(f"{indent_str * 2}</tr>")
    table_parts.append(f"{indent_str}</tbody>")
    table_parts.append("</table>")

    return "\n".join(table_parts)
