from parser import parser


if __name__ == "__main__":

    # Parse an expression
    ast = parser.parse(
        """
    x = 2 * 3 + 4 * (5 - x)

    if x > 5:
        print("x is greater than 5")
    else:
        print("x is less than or equal to 5")
    """
    )
    print(ast)
