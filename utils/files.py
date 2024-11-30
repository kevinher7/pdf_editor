import os

def get_pdfs_in_path(path):
    pdf_paths_list = []
    
    for file in os.listdir(path):
        if file.endswith("pdf"):
            pdf_paths_list.append(file)

    return pdf_paths_list

def ensure_pdf_extension(file_name):
    if file_name[-4:] != ".pdf":
        file_name += ".pdf"

    return file_name
