"""
Copyright 2024 Kingston University Rocket Engineering

MIT License - See license file

Generates library from symbols
"""

import subprocess


def file_changed(filepath):
    """
    Check if a file has had any changes in the Git repository.

    Argumnets:
        filepath - str
            The path to the file to check.
    """

    try:
        result = subprocess.run(
            ["git", "status", "--porcelain", filepath],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
        )
        return bool(result.stdout.strip())
    except FileNotFoundError:
        raise RuntimeError("Git is not installed or not in the system PATH.")
    except Exception as e:
        raise RuntimeError(f"An error occurred: {e}")
