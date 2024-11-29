import os
import argparse

from ..utils import compress_pdf

def main():
    parser = argparse.ArgumentParser(description="Compress PDF file")
    parser.add_argument("-i", "--input_file", type=str, help="Name of input file (file to compress)")
    parser.add_argument("-o","--output_file", type=str, help="Name of output (compressed) file")
    args = parser.parse_args()

    current_path = os.getcwd()

    # compress_pdf(args.input_file, args.output_file, "default")
    compress_pdf("C:/Users/kevin/Downloads/output/merged.pdf", "C:/Users/kevin/Downloads/output/compressed.pdf", "default")


if __name__ == "__main__":
    main()
