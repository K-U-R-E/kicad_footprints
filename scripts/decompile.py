"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import sys
import os
import sexp


def split_lib(libpath, outdir):

    with open(libpath, "r") as f:
        lib_data = sexp.parse(f.read(), parse_nums=True)

    header = lib_data[:4]

    components = []
    current_lib = None

    for entry in lib_data[4:]:
        if isinstance(entry, list) and entry[0] == "symbol":
            symbol = entry[1]
            if current_lib and current_lib != symbol:
                save_lib(header, current_lib, components, outdir)
                components.clear()
            current_lib = symbol
            components.append(entry)
        else:
            components.append(entry)

    if components:
        save_lib(header, current_lib, components, outdir)


def save_lib(header, lib_name, components, outdir):
    # Create the library file with the specified name
    lib_file = os.path.join(outdir, f"{lib_name}.kicad_sym")
    os.makedirs(os.path.dirname(lib_file), exist_ok=True)

    print("Writing: " + lib_file)
    with open(lib_file, "w") as f:
        f.write(sexp.generate([*header, components]))


def usage():
    print("Usage: {} <compiled lib path> <output directory>".format(sys.argv[0]))
    sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        usage()
    else:
        libpath = sys.argv[1]
        outdir = sys.argv[2]

        if not os.path.exists(libpath):
            print(f"Error: The file {libpath} does not exist.", file=sys.stderr)
            sys.exit(1)

        if not os.path.isdir(outdir):
            print(f"Error: The directory {outdir} does not exist.", file=sys.stderr)
            sys.exit(1)

        split_lib(libpath, outdir)
        print(f"Library has been split and saved to {outdir}")
