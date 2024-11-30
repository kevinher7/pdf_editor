import os
import subprocess
import argparse

from ..utils import ensure_pdf_extension

def compress_pdf(input_file, output_file=None, quality="screen"):
    input_file = ensure_pdf_extension(input_file)

    if output_file is None:
        output_file = input_file.replace(".pdf", "_c.pdf")
    else:
        output_file = ensure_pdf_extension(output_file)

    
    current_path = os.getcwd()

    input_path = os.path.join(current_path, input_file)
    output_path = os.path.join(current_path, output_file)

    subprocess.call(["gswin64c", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                     f"-dPDFSETTINGS=/{quality}", "-dNOPAUSE", "-dQUIET", "-dBATCH",
                     f"-sOutputFile={output_path}", input_path], shell=True)

def main():
    parser = argparse.ArgumentParser(description="Compress PDF file")
    parser.add_argument("input_file", type=str, help="Name of input file (file to compress)")
    parser.add_argument("-o","--output_file", type=str, help="Name of output (compressed) file")
    parser.add_argument("-q","--quality", type=str, help="Quality of compressed file", default="screen")
    args = parser.parse_args()


    if args.input_file is None:
        raise ValueError("Input file not provided.")

    compress_pdf(args.input_file, args.output_file, args.quality)


if __name__ == "__main__":
    main()
