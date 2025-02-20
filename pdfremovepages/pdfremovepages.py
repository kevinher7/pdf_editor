import argparse

from PyPDF2 import PdfWriter

from ..pdfkeeppages import keep_pages

from ..utils import get_pdf_pages
from ..utils import parse_pages_list


def remove_page(file_name: str, page_number_to_remove: int):
    merger = PdfWriter()

    pdf_pages = list(get_pdf_pages(file_name))

    pdf_pages.pop(page_number_to_remove - 1)

    for page in pdf_pages:
        merger.add_page(page)

    merger.write(f"./{file_name}_r{page_number_to_remove}.pdf")
    merger.close()

    print(
        f"Removed page number {page_number_to_remove} from {file_name}.pdf")


def remove_pages(file_name: str, pages_to_remove: str):
    pages_to_remove = parse_pages_list(pages_to_remove)

    if not pages_to_remove:
        raise ValueError(
            "No pages to remove on input. Please insert pages to remove. Ex: 1, 2, 4, 7")

    if len(pages_to_remove) == 1:
        # remove_page accepts page in 1-based format
        remove_page(file_name, pages_to_remove[0] + 1)
        return

    pdf_pages = list(get_pdf_pages(file_name))

    merger = PdfWriter()

    for idx, page in enumerate(pdf_pages):
        if idx in pages_to_remove:
            continue
        merger.add_page(page)

    merger.write(f"./{file_name}_r{pages_to_remove}.pdf")
    merger.close()

    print(
        f"Removed pages {[page + 1 for page in pages_to_remove]} from {file_name}.pdf")


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
