import os
import subprocess
import argparse

def compress_pdf(input_path, output_path, quality):
    subprocess.call(["gswin64c", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                     f"-dPDFSETTINGS=/{quality}", "-dNOPAUSE", "-dQUIET", "-dBATCH",
                     f"-sOutputFile={output_path}", input_path], shell=True)

def main():
    parser = argparse.ArgumentParser(description="Compress PDF file")
    parser.add_argument("-i", "--input_file", type=str, help="Name of input file (file to compress)")
    parser.add_argument("-o","--output_file", type=str, help="Name of output (compressed) file")
    args = parser.parse_args()

    current_path = os.getcwd()

    # compress_pdf(args.input_file, args.output_file, "default")
    compress_pdf("C:/Users/kevin/Downloads/output/2273141s_soryuusi5.pdf", "C:/Users/kevin/Downloads/output/compressed.pdf", "default")


if __name__ == "__main__":
    main()
