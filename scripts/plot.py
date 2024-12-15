"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import os
import sys


def export(lib_file, output_dir):

    if not os.path.exists(output_dir):
        os, makedirs(output_dir)

    command = ["kicad-cli sym export"]


if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage
