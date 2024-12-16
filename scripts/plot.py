"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import os
import sys

from utils import file_changed

def export_symbol(symbol, outdir):
    command = f"kicad-cli sym export svg '{symbol}' --output {outdir}"
    exit_code = os.system(command)

    if exit_code == 0:
        print(f"Exported {symbol} to '{outdir}'\n")
    else:
        print(f"Failed to export {symbol}")


def export(symboldir, output_dir):
    """
    Export library symbols as SVGs

    lib_file - str
        Library file containing all symbols
    output_dir - str
        Directory to output the plots
    """
    
    symbol_files = [] 

    for f in os.listdir(symboldir):
        f_abs = os.path.join(symboldir, f)
        if f.endswith(".kicad_sym") and file_changed(f_abs):
            symbol_files.append(f_abs)

    if not symbol_files:
        print(f"No symbols found in '{symboldir}'")
        return False

    for symbol in symbol_files:
        export_symbol(symbol, output_dir)


    print(f"All symbols in {symboldir} exported to {output_dir}")
    return True

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

    print(f"README.md generated to {output_dir}")

def usage():
    """
    Usage

    Prints the script's usage
    """

    print("Usage: {} <symbol path> <output directory>".format(sys.argv[0]))
    sys.exit(1)

if __name__ == "__main__":

    print("Rocketry P&ID KiCAD - Plotting\n")

    if len(sys.argv) != 3:
        usage()
    else:
        symboldir = sys.argv[1]
        outdir = sys.argv[2]

        print(f"Individual Symbol Path: {symboldir}")
        print(f"Output Path: {outdir}\n")

    if not os.path.isdir(outdir):
        print(f"The output directory '{outdir}' does not exist.".format(sys.argv[0]))
        sys.exist(1)

    if not os.path.isdir(symboldir):
        print(f"The symbols directory '{symboldir}' does not exist.".format(sys.argv[0]))

    if export(symboldir, outdir):
        generate_readme(outdir)
