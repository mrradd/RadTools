#!/usr/bin/env python3

"""
combine_context.py

This program recursively scans a directory for supported source files and combines
their contents into a single text file intended for AI context.

Supported file types:
- .kt   Kotlin files
- .sq   SQLDelight query files, or other .sq files
- .sqm  SQLDelight migration files, or other .sqm files
- .js   Javascript files.
- .jsx  React Javascript files.
- .ts   Typescript files.
- .tsx  React Typescript files.
- .html HTML files.
- .css  CSS files.

Each file's contents are separated by a header containing the file name/path.

Import statements are removed from the output to reduce noise.
"""

from pathlib import Path
import argparse

# File extensions this script should collect.
SUPPORTED_EXTENSIONS = {".kt", ".sq", ".sqm", ".js", ".jsx", ".ts", ".tsx", ".html", ".css"}

def remove_imports(text: str) -> str:
    """
    Remove import statements from the provided text.

    This is mainly intended for Kotlin files, where imports often add noise
    when preparing code for AI context.

    Any line that starts with "import " after trimming leading whitespace
    will be excluded from the output.

    Example removed lines:
        import androidx.compose.runtime.Composable
        import com.example.SomeClass
    """

    # Split the file contents into individual lines.
    lines = text.splitlines()

    # Keep only lines that are not import statements.
    filtered_lines = [
        line for line in lines
        if not line.strip().startswith("import ")
    ]

    # Join the remaining lines back into one string.
    # strip() removes extra blank space at the beginning and end of each file.
    return "\n".join(filtered_lines).strip()


def collect_supported_files(directory: Path) -> list[Path]:
    """
    Recursively collect all supported files from the given directory.

    Args:
        directory:
            The root directory to search.

    Returns:
        A sorted list of file paths matching the supported extensions.
    """

    # directory.rglob("*") recursively finds all files and folders.
    # We keep only actual files whose suffix matches SUPPORTED_EXTENSIONS.
    return sorted(
        file_path
        for file_path in directory.rglob("*")
        if file_path.is_file() and file_path.suffix in SUPPORTED_EXTENSIONS
    )


def read_file_safely(file_path: Path) -> str:
    """
    Read a file as UTF-8 text.

    If the file contains invalid UTF-8 characters, those characters are ignored
    instead of crashing the program.

    Args:
        file_path:
            The file to read.

    Returns:
        The file contents as a string.
    """

    try:
        # Try reading the file normally as UTF-8.
        return file_path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        # If decoding fails, ignore invalid characters and continue.
        return file_path.read_text(encoding="utf-8", errors="ignore")


def combine_files(directory: Path) -> str:
    """
    Combine all supported files from the directory into a single formatted string.

    Each file is written in this format:

        ----
        relative/path/to/file.kt
        ----
        file contents here

    Args:
        directory:
            The root directory to scan.

    Returns:
        A single string containing all collected file contents.
    """

    # Find all .kt, .sq, and .sqm files.
    files = collect_supported_files(directory)

    # This list will hold each formatted file section.
    output_parts = []

    for file_path in files:
        # Use a relative path so the output is cleaner and portable.
        relative_name = file_path.relative_to(directory)

        # Read the file contents.
        contents = read_file_safely(file_path)

        # Remove Kotlin-style import statements.
        contents = remove_imports(contents)

        # Add this file's section to the final output.
        output_parts.append(
            f"----\n"
            f"{relative_name}\n"
            f"----\n"
            f"{contents}"
        )

    # Separate each file section with a newline.
    return "\n".join(output_parts)


def main():
    """
    Program entry point.

    This function:
    1. Reads command-line arguments.
    2. Validates the provided directory.
    3. Combines all supported files.
    4. Writes the combined output to a text file.
    """

    # Set up command-line argument parsing.
    parser = argparse.ArgumentParser(
        description="Combine .kt, .sq, and .sqm files into one file for AI context."
    )

    # Required positional argument: the directory to scan.
    parser.add_argument(
        "directory",
        help="Directory to recursively scan for supported files."
    )

    # Optional argument: where to write the combined output.
    parser.add_argument(
        "-o",
        "--output",
        default="combined_ai_context.txt",
        help="Output file name. Defaults to combined_ai_context.txt"
    )

    # Parse the command-line arguments provided by the user.
    args = parser.parse_args()

    # Convert the provided directory path into an absolute Path object.
    directory = Path(args.directory).resolve()

    # Make sure the provided path exists.
    if not directory.exists():
        raise FileNotFoundError(f"Directory does not exist: {directory}")

    # Make sure the provided path is actually a directory.
    if not directory.is_dir():
        raise NotADirectoryError(f"Not a directory: {directory}")

    # Combine the contents of all supported files.
    combined = combine_files(directory)

    # Convert the output path into a Path object.
    output_path = Path(args.output)

    # Write the combined content to the output file using UTF-8 encoding.
    output_path.write_text(combined, encoding="utf-8")

    # Let the user know where the output was written.
    print(f"Combined files written to: {output_path}")

if __name__ == "__main__":
    main()