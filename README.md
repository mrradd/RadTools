# AI Context File Combiner Tool

A simple Python command-line tool that recursively scans a directory, collects supported source files, removes `import` statements, and combines the file contents into one text file for use as AI context.

## Purpose

This tool is intended to make it easier to provide project code to an AI assistant by combining multiple source files into a single readable context file.

Each file is separated by a clear header using the path and file name.

Example output:

```text
----
path/to/code/HomeScreen.kt
----
@Composable
fun HomeScreen() {
    // code here
}

----
path/to/code/styles.css
----
.container {
    display: flex;
}
```

## Supported File Types
The tool currently collects files with the following extensions:

- .kt
- .sq
- .sqm
- .js
- .jsx
- .ts
- .tsx
- .html
- .css


## Features

- Recursively scans a directory
- Combines supported source files into one output file
- Removes lines that start with import
- Uses the path and file name in separators
- Writes output as UTF-8 text
- Ignores invalid UTF-8 characters instead of crashing
- Useful for preparing code context for AI tools

## Requirements
Python 3.9 or newer recommended
No third-party Python packages are required.

## Installation
Clone or download the script into your project or tools directory.

## Usage
### Basic usage:

```python combine_context.py /path/to/project```

This creates an output file named:

```combined_ai_context.txt```

### Custom Output File
You can specify a custom output file with ```-o``` or ```--output```:

```python combine_context.py /path/to/project -o ai_context.txt```

or:

```python combine_context.py /path/to/project --output ai_context.txt```

### Using the ```code_combiner``` Script
Change ```C:\path\to\code\directory``` in the script to match the path to your desired directory:

```python code_combiner_tool.py C:\path\to\code\directory -o combined_code_%mydate%_%Hour%_%Minute%.txt```

You may also change the name of the output file if desired by changing:

```combined_code_%mydate%_%Hour%_%Minute%.txt```

By default the result is a file named in the following way ```combined_code_yyyy-mm-dd_HH_MM.txt``` where the time is in 24 hour format.

A ```.sh``` version of the script is also provided.

#### Example Output File's Name

```combined_code_2026-08-20_15_32.txt```

## Changing Supported File Types
To add or remove supported file types, edit this line in the ```code_combiner_tool.py``` script:

```SUPPORTED_EXTENSIONS = {".kt", ".sq", ".sqm", ".js", ".jsx", ".ts", ".tsx", ".html", ".css"}```

#### For example, to add CSharp file support:

```
SUPPORTED_EXTENSIONS = {
    ".kt",
    ".sq",
    ".sqm",
    ".js",
    ".jsx",
    ".tsx",
    ".ts",
    ".html",
    ".css",
    ".cs" # This adds support for CSharp files.
}
```

## License
Use freely and modify as needed.