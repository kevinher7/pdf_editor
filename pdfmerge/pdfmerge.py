import os

from PyPDF2 import PdfWriter

from ..utils import get_pdfs_in_path

def main():
    current_path = os.getcwd()
    pdf_files = get_pdfs_in_path(current_path)

    merger = PdfWriter()

    for pdf in pdf_files:
        merger.append(pdf)

    os.makedirs("./output", exist_ok=True) 
    merger.write("./output/merged.pdf")
    merger.close()

    print(f"Merged {len(pdf_files)} files!")

    return 0


if __name__ == "__main__":
    main()
