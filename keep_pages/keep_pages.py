import argparse

from PyPDF2 import PdfWriter


from ..utils import get_naming_string_from_pages_list
from ..utils import get_pdf_pages
from ..utils import handle_pages_range
from ..utils import parse_pages_to_list


def keep_pages(file_name, pages_to_keep: str):
    is_range = False

    pages_to_keep = parse_pages_to_list(pages_to_keep)

    if not pages_to_keep:
        raise ValueError(
            "No pages to keep on input. Please insert pages to keep. Ex: 1,2,4,7 or 1-5 (equivalent to 1,2,3,4,5)")

    pdf_pages = list(get_pdf_pages(file_name))

    if is_range:
        pages_to_keep = handle_pages_range(pages_to_keep, len(pdf_pages))

    merger = PdfWriter()

    for page_number in pages_to_keep:
        merger.add_page(pdf_pages[page_number])

    kept_pages_string = get_naming_string_from_pages_list(
        pages_to_keep, is_range)

    merger.write(
        f"./{file_name}_k{kept_pages_string}.pdf")
    merger.close()

    print(
        f"Removed pages outside range {kept_pages_string} from {file_name}.pdf")


def main():
    parser = argparse.ArgumentParser(
        description="Keep pages from PDF file and delete the rest")
    parser.add_argument("input_file", type=str,
                        help="Name of input file (file to compress)")
    parser.add_argument("pages_to_keep", type=str,
                        help="Pages to keep from the PDF")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    if args.pages_to_keep is None:
        raise ValueError("Page range or list to keep not provided.")

    keep_pages(args.input_file, args.pages_to_keep)


if __name__ == "__main__":
    main()
