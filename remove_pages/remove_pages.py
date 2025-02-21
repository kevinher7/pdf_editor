import argparse

from PyPDF2 import PdfWriter


from ..keep_pages import keep_pages

from ..utils import format_page_range
from ..utils import get_pdf_pages
from ..utils import handle_pages_range
from ..utils import parse_pages_list
from ..utils import parse_pages_range


def remove_page(file_name: str, page_number_to_remove: int):

    pdf_pages = list(get_pdf_pages(file_name))

    pdf_pages.pop(page_number_to_remove - 1)

    merger = PdfWriter()

    for page in pdf_pages:
        merger.add_page(page)

    merger.write(f"./{file_name}_r{page_number_to_remove}.pdf")
    merger.close()

    print(
        f"Removed page number {page_number_to_remove} from {file_name}.pdf")


def remove_pages(file_name: str, pages_to_remove: str):
    is_range = False

    if "-" in pages_to_remove:
        pages_to_remove = parse_pages_range(pages_to_remove)
        is_range = True
    else:  # a single number or list. 例: 1 or 1,2,3
        pages_to_remove = parse_pages_list(pages_to_remove)

    if not pages_to_remove:
        raise ValueError(
            "No pages to remove on input. Please insert pages to remove. Ex: 1,2,4,7 or 1-5 (equivalent to 1,2,3,4,5)")

    if len(pages_to_remove) == 1:
        # remove_page accepts page in 1-based format
        remove_page(file_name, int(pages_to_remove[0]) + 1)
        return

    pdf_pages = list(get_pdf_pages(file_name))

    if is_range:
        pages_to_remove = handle_pages_range(pages_to_remove, len(pdf_pages))

    merger = PdfWriter()
    last_page_to_remove = max(pages_to_remove)

    for idx, page in enumerate(pdf_pages):
        if idx in pages_to_remove:
            continue
        merger.add_page(page)

    deleted_pages_string = ""
    if is_range:
        deleted_pages_string = format_page_range(pages_to_remove)
    else:
        deleted_pages_string = f"_{[page + 1 for page in pages_to_remove]}"

    merger.write(
        f"./{file_name}_r{deleted_pages_string}.pdf")
    merger.close()

    print(
        f"Removed pages {deleted_pages_string} from {file_name}.pdf")


def main():
    parser = argparse.ArgumentParser(description="Remove Page from PDF file")
    parser.add_argument("input_file", type=str,
                        help="Name of input file (file to compress)")
    parser.add_argument("pages_to_remove", type=str,
                        help="Page to Remove from the PDF")
    parser.add_argument("-k", "--keep", action="store_true",
                        help="Keep specified pages instead of removing them")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    if args.pages_to_remove is None:
        raise ValueError("Page to remove not provided.")

    if (args.keep):
        keep_pages(args.input_file, args.pages_to_remove)  # remove === keep
        return

    remove_pages(args.input_file, args.pages_to_remove)


if __name__ == "__main__":
    main()
