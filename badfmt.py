"""A very bad formatter for any programming language with braces and semicolons (eg. c/c++/java/javascript/rust)"""
import click


@click.command()
@click.argument("filepath", type=click.Path(exists=True))
@click.option(
    "-l", "--line-len", type=int, default=95, help="The length you want your lines to be"
)
def bad_fmt(filepath: str = "", line_len: int = 95):
    """A very bad formatter for any programming language with braces and semicolons (eg. c/c++/java/javascript/rust)"""
    res = []
    llens = []
    with open(filepath, "r", encoding="utf-8") as f:
        for line in f.readlines():
            llens.append(len(line))

            if len(line) > line_len:
                res.append(line)
            elif line.rstrip().endswith(";"):
                res.append(
                    line[: len(line) - 2]
                    + (" " * (line_len - len(line) - 1))
                    + ";\n"
                )
            elif line.rstrip().endswith("{"):
                res.append(
                    line[: len(line) - 2]
                    + (" " * (line_len - len(line) - 1))
                    + "{\n"
                )
            elif line.rstrip().endswith("}"):
                res.append(
                    line[: len(line) - 2]
                    + (" " * (line_len - len(line) - 1))
                    + "}\n"
                )
            elif line.rstrip().endswith("};"):
                res.append(
                    line[: len(line) - 2]
                    + (" " * (line_len - len(line) - 2))
                    + "};\n"
                )

            else:
                res.append(line)

    with open(filepath, "w", encoding="utf-8") as f:
        f.writelines(res)


if __name__ == "__main__":
    bad_fmt()
