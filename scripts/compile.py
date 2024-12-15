"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import sys
import os
import sexp


def combine_libs(libdir, outlib):

    combined_data = [
        "kicad_symbol_lib",
        ["version 20231120"],
        ['generator "kicad_symbol_editor"'],
        ['generator_version "8.0"'],
    ]
    for lib_file in os.listdir(libdir):
        if lib_file.endswith(".kicad_sym"):
            lib_path = os.path.join(libdir, lib_file)
            print("Reading: " + lib_path)

            with open(lib_path, "r") as f:
                lib_data = sexp.parse(f.read(), parse_nums=True)

            combined_data += lib_data[4:][0]

    with open(outlib, "w") as f:
        f.write(sexp.generate(combined_data))


def usage():
    print("Usage: {} <input directory> <output lib path>".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    else:
        libdir = sys.argv[1]
        outlib = sys.argv[2]

        if not os.path.isdir(libdir):
            print(f"Error: The directory {libdir} does not exist.", file=sys.stderr)
            sys.exit(1)

        combine_libs(libdir, outlib)
        print(f"Libraries have been combined and saved to {outlib}")
