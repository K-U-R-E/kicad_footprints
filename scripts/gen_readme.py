"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import os


def generate_readme(folder_path, readme_path):

    svg_files = [f for f in os.listdir(folder_path) if f.endswith(".svg")]

    if not svg_files:
        print("No SVG files found in the specified folder.")
        return

    markdown_lines = ["# PI&D KiCAD Symbols\n"]
    for svg in svg_files:
        svg_path = os.path.join(folder_path, svg)
        markdown_lines.append(f"##{svg}")
        markdown_lines.append(f"<img src = '{svg}' width = '500' height = '500'>")

    with open(readme_path, "w") as readme_file:
        readme_file.write("\n".join(markdown_lines))

    print(f"README.md generated at {readme_path}")


if __name__ == "__main__":
    folder_path = "."
    readme_path = "README.md"

    generate_readme(folder_path, readme_path)
