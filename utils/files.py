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


def get_pdf_path_from_name(file_name):
    current_path = os.getcwd()

    file_name = ensure_pdf_extension(file_name)
    file_path = os.path.join(current_path, file_name)

    return file_path
