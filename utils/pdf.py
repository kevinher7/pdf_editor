from PyPDF2 import PdfReader

from .files import get_pdf_path_from_name


def get_pdf_pages(file_name):
    file_path = get_pdf_path_from_name(file_name)
    input_pdf = PdfReader(file_path)

    input_pdf_pages = input_pdf.pages

    return input_pdf_pages


def handle_pages_range(pages_range: list, total_number_of_pages: int) -> list[int]:
    if pages_range[1] == "end":
        pages_range[1] = total_number_of_pages

    return range(pages_range[0], pages_range[1] + 1, 1)
