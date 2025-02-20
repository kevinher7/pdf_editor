import subprocess
import argparse

from ..utils import get_pdf_path_from_name


def compress_pdf(input_file, output_file=None, quality="screen"):
    input_path = get_pdf_path_from_name(input_file)

    if output_file is None:
        output_path = input_path.replace(".pdf", "_c.pdf")
    else:
        output_path = get_pdf_path_from_name(output_file)

    subprocess.call(["gswin64c", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4",
                     f"-dPDFSETTINGS=/{quality}", "-dNOPAUSE", "-dQUIET", "-dBATCH",
                     f"-sOutputFile={output_path}", input_path], shell=True)

    print(f"Sucessfully compressed File into {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Compress PDF file")
    parser.add_argument("input_file", type=str,
                        help="Name of input file (file to compress)")
    parser.add_argument("-o", "--output_file", type=str,
                        help="Name of output (compressed) file")
    parser.add_argument("-q", "--quality", type=str,
                        help="Quality of compressed file", default="screen")
    args = parser.parse_args()

    if args.input_file is None:
        raise ValueError("Input file not provided.")

    compress_pdf(args.input_file, args.output_file, args.quality)

    return 0


if __name__ == "__main__":
    main()
