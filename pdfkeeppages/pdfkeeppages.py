import argparse

from PyPDF2 import PdfWriter

from ..utils import get_pdf_pages
from ..utils import parse_pages_range


def keep_pages(file_name, pages_range):
    # Get pages range as a list
    pages_range = parse_pages_range(pages_range)

    merger = PdfWriter()

    pdf_pages = list(get_pdf_pages(file_name))

    if pages_range[1] == "end":
        pages_range[1] = len(pdf_pages)

    for page_number in range(pages_range[0], pages_range[1], 1):
        merger.add_page(pdf_pages[page_number])

    merger.write(f"./{file_name}_k{pages_range[0]}-{pages_range[1]}.pdf")
    merger.close()

    print(
        f"Removed pages outside range [{pages_range[0]} - {pages_range[1]}] from {file_name}.pdf")

    return 0


def main():
    parser = argparse.ArgumentParser(
        description="Keep pages from PDF file and delete the rest")
    parser.add_argument("input_file", type=str,
                        help="Name of input file (file to compress)")
    parser.add_argument("pages_to_keep", type=str,
                        help="Page to Remove from the PDF")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    if args.pages_to_keep is None:
        raise ValueError("Page range to keep not provided.")

    keep_pages(args.input_file, args.pages_to_keep)


if __name__ == "__main__":
    main()
