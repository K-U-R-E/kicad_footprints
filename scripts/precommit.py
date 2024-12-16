import os
import sys
from utils import file_changed


def main(libpath, symbolsdir):

    symbol_changes = False
    for f in os.listdir(symbolsdir):
        if f.endswith(".kicad_sym") and file_changed(os.path.join(symbolsdir, f)):
            symbol_changes = True
            break

    monolith_changes = file_changed(libpath)

    if monolith_changes and symbol_changes:
        print("There were changed to both the monolithic library and individuals")
    elif monolith_changes and not symbol_changes:
        print("Only monolith changes, decompiling, plotting etc")
        os.system("make decompile plot")
    elif not monolith_changes and symbol_changes:
        print("Only symbol changes, compiling monolith and potting etc")
        os.system("make compile plot")
    else:
        print("No changes")
        return


if __name__ == "__main__":

    if len(sys.argv) != 3:
        print("Error")
    else:
        libpath = sys.argv[1]
        symbolsdir = sys.argv[2]

    main(libpath, symbolsdir)
