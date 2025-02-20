from PyPDF2 import PdfReader

from .files import get_pdf_path_from_name


def get_pdf_pages(file_name):
    file_path = get_pdf_path_from_name(file_name)
    input_pdf = PdfReader(file_path)

    input_pdf_pages = input_pdf.pages

    return input_pdf_pages
