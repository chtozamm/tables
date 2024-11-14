from typing import List


def sort_table_data(
    headers: List[str], data: List[List[str]], sort_key: str, order: str
) -> str:
    """
    Sorts table data based on the specified key and order.

    order: "ASC" | "DESC"
    """

    # Check if sort_key is a valid header
    if sort_key not in headers:
        raise Exception(
            f'Invalid sort key: "{sort_key}". Available keys: {", ".join(headers)}'
        )

    reverse = order == "DESC"

    # Sort the data based on the given sort key and order
    sorted_data = sorted(
        data, key=lambda row: row[headers.index(sort_key)], reverse=reverse
    )

    return sorted_data
