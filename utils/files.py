import os

def get_pdfs_in_path(path):
    pdf_paths_list = []
    
    for file in os.listdir(path):
        if file.endswith("pdf"):
            pdf_paths_list.append(file)

    return pdf_paths_list
