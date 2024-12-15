"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import os
import sys


def export(lib_file, output_dir):
    """
    Export library symbols as SVGs

    lib_file - str
        Library file containing all symbols
    output_dir - str
        Directory to output the plots
    """

    command = f"kicad-cli sym export svg {lib_file } --output {output_dir}"

    exit_code = os.system(command)

    if exit_code == 0:
        print(f"Exported symbols to '{output_dir}'")
    else:
        print(f"Failed to export symbols")
        sys.exit(1)


def generate_readme(symbols_dir, output_dir = None):
    """
    Generates README showing current symbols
    
    symbols_dir - str
        Directory containing the source SVGs
    output_dir - str
        Directory to output README into (Defaults to the same path as the source SVGs
    """

    output_dir = output_dir or symbols_dir

    svg_files = [f for f in os.listdir(symbols_dir) if f.endswith(".svg")]

    if not svg_files:
        print("No SVG files found in the specified folder.")
        return

    markdown_lines = ["# PI&D KiCAD Symbols\n"]
    for svg in svg_files:
        svg_path = os.path.join(output_dir, svg)
        markdown_lines.append(f"## {svg}")
        markdown_lines.append(f"<img src = '{svg}' width = '500' height = '500'>")

    readme_path = os.path.join(output_dir, "README.md")
    with open(readme_path, "w") as readme_file:
        readme_file.write("\n".join(markdown_lines))

    print(f"README.md generated at {output_dir}")

def usage():
    """
    Usage

    Prints the script's usage
    """

    print("Usage: {} <compiled lib path> <output directory>".format(sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 3:
        usage()
    else:
        libpath = sys.argv[1]
        outdir = sys.argv[2]

    if not os.path.exists(libpath):
        print(f"The library file '{libpath}' does not exist".format(sys.argv[0]))
        sys.exit(1)

    if not os.path.isdir(outdir):
        print(f"The output directory '{outdir}' does not exist.".format(sys.argv[0]))
        sys.exist(1)

    export(libpath, outdir)
    generate_readme(outdir)
