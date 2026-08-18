Combiner Tool README
# AI Context File Combiner

A simple Python command-line tool that recursively scans a directory, collects supported source files, removes `import` statements, and combines the file contents into one text file for use as AI context.

## Purpose

This tool is intended to make it easier to provide project code to an AI assistant by combining multiple source files into a single readable context file.

Each file is separated by a clear header using only the file name.

Example output:

```text
----
HomeScreen.kt
----
@Composable
fun HomeScreen() {
    // code here
}

----
styles.css
----
.container {
    display: flex;
}
```
### Supported File Types
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


### Features

- Recursively scans a directory
- Combines supported source files into one output file
- Removes lines that start with import
- Uses only the file name in separators
- Writes output as UTF-8 text
- Ignores invalid UTF-8 characters instead of crashing
- Useful for preparing code context for AI tools

### Requirements
Python 3.9 or newer recommended
No third-party Python packages are required.

### Installation
Clone or download the script into your project or tools directory.

### Usage
#### Basic usage:

python combine_context.py /path/to/project
This creates an output file named:

combined_ai_context.txt

#### Custom Output File
You can specify a custom output file with ```-o``` or ```--output```:

```python combine_context.py /path/to/project -o ai_context.txt```

or:

```python combine_context.py /path/to/project --output ai_context.txt```

#### Example
Given a directory like this:

project/
├── src/
│   ├── HomeScreen.kt
│   ├── Button.jsx
│   └── styles.css
└── database/
    └── queries.sq
Run:

```
python combine_context.py project -o context.txt
```

### Changing Supported File Types
To add or remove supported file types, edit this line in the script:

```SUPPORTED_EXTENSIONS = {".kt", ".sq", ".sqm", ".js", ".jsx", ".ts", ".tsx", ".html", ".css"}```

#### For example, to add CSharp files:

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

#### License
Use freely and modify as needed.