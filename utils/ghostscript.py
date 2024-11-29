import subprocess

def compress_pdf(input_path, output_path, quality):
    subprocess.call(['gs', '-sDEVICE=pdfwrite', '-dCompatibilityLevel=1.4',
                     '-dPDFSETTINGS=/' + quality, '-dNOPAUSE', '-dQUIET', '-dBATCH',
                     '-sOutputFile=' + output_path, input_path])

