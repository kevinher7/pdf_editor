import argparse

from PyPDF2 import PdfWriter, PdfReader

from ..utils import get_pdf_pages


def remove_page(file_name, page_number_to_remove):
    merger = PdfWriter()

    pdf_pages = list(get_pdf_pages(file_name))

    pdf_pages.pop(page_number_to_remove - 1)

    for page in pdf_pages:
        merger.add_page(page)

    merger.write(f"./{file_name}_r{page_number_to_remove}.pdf")
    merger.close()

    print(f"Removed page number {page_number_to_remove} from {file_name}.pdf")

    return 0

def main():
    parser = argparse.ArgumentParser(description="Remove Page from PDF file")
    parser.add_argument("input_file", type=str, help="Name of input file (file to compress)")
    parser.add_argument("page_to_remove", type=int, help="Page to Remove from the PDF")
    args = parser.parse_args()


    if args.input_file is None:
        raise ValueError("Input file not provided.")
    
    if args.page_to_remove is None:
        raise ValueError("Page to remove not provided.")
    
    remove_page(args.input_file, args.page_to_remove)

if __name__ == "__main__":
    main()
