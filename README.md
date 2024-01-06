# badfmt

A very bad formatter for any programming language with braces and semicolons (e.g., c/c++/java/javascript/rust)

## Description

`badfmt` is a command-line tool that attempts to format code files written in programming languages with braces and semicolons. It makes the code seem like it doesn't have any semicolons or braces but puts them at the very end of the line away from sight. It is designed to be a joke formatter and should not be used in production codebases.

## Installation

To install `badfmt`, you need to have Python 3.8 or higher installed. You can then use `pip` to install the package:

```shell
pip install badfmt
```

## Usage
To use badfmt, simply run the following command:
```shell
python -m badfmt [filepath]
```

Replace [filepath] with the path to the file you want to format. The tool will attempt to format the file in place.

You can also specify the maximum line length using the -l or --line-len option. For example:

```
badfmt -l 80 [filepath]
```

