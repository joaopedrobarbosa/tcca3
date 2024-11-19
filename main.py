from parser import parser
import os


if __name__ == "__main__":
    with open("./program.bahia") as program:
        lines = program.readlines()

        # Test input
        output = parser.parse("\n".join(lines))

    with open("./output.py", "w") as py_output:
        py_output.write(output)
