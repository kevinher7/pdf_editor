import subprocess

def compress_pdf(input_path, output_path, quality):
    subprocess.call(["gswin64c", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                     f"-dPDFSETTINGS=/{quality}", "-dNOPAUSE", "-dQUIET", "-dBATCH",
                     f"-sOutputFile={output_path}", input_path], shell=True)

