import os
import sys
import argparse

from constructors.html import construct_html_table
from parsers.html import parse_html_table
from commands.sort import sort_table_data


def main():
    # 1. Parse command-line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "action",
        type=str,
        help="The action to perform. Available actions: sort | filter | select | convert",
    )
    parser.add_argument("-s", "--source", type=str, help="Source file")
    parser.add_argument("-o", "--output", type=str, help="Output file")
    parser.add_argument("-k", "--key", type=str, help="Sorting key")
    args = parser.parse_args()

    # 2. Perform specified action
    if args.action == "sort":
        src = args.source
        if not os.path.isfile(src):
            print(f"Error: The file '{src}' does not exist.")
            return

        _, file_extension = os.path.splitext(src)

        with open(src, "r") as file:
            file_content = file.read()
            if file_extension == ".html":
                headers, data = parse_html_table(file_content)
                sorted_data = sort_table_data(headers, data, args.key, "ASC")
                sorted_table = construct_html_table(headers, sorted_data)

                # Write the sorted table to the output file if specified
                if args.output:
                    with open(args.output, "w") as output_file:
                        output_file.write(sorted_table)
                        print(f"Sorted table has been written to '{args.output}'.")
                else:
                    print(sorted_table)

    else:
        print("Not implemented yet")
        sys.exit(1)


if __name__ == "__main__":
    main()
