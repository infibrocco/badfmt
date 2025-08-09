# vertfmt

A vertical formatter for any programming language with braces and semicolons (e.g., c/c++/java/javascript/rust)

## Description

`vertfmt` is a command-line tool that formats code written in programming languages with braces and semicolons (e.g., c/c++/java/javascript/rust/...). It shifts all your semicolons and braces to the very end of the line away from sight. It is designed to be used in less serious codebases.

## Installation

To install `vertfmt`, you need to have Python 3.8 or higher installed. You can then use `pip` to install the package:

```shell
pip install pip install git+https://github.com/infibrocco/vertfmt.git
```

## Usage
To use vertfmt, simply run the following command:
```shell
python -m vertfmt [filepath]
```

Replace [filepath] with the path to the file you want to format. The tool will attempt to format the file in place.

You can also specify the maximum line length using the -l or --line-len option. For example:

```sh
python -m vertfmt -l 80 [filepath]
```

