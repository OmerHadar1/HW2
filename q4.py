def q4(n: int):
    """
    :param n: A positive number
    :return: The n-th line in the Pascal triangle
    """
    if n == int(n):
        def factorial(x: int):
            """
            :param x: a positive number
            :return: the factorial of the parameter
            """
            facto_x = 1
            for i in range(1, x + 1):
                facto_x = facto_x * i
            return facto_x

        def choose(a: int, b: int):
            """
            this function is the chose action in Combinatorics
            :param a: the line number in pascal triangle
            :param b: the location in the line
            :return: c: the number in the 'b' location in the 'a' line in the pascal triangle
            """
            c = int(factorial(a) / (factorial(b) * factorial(a - b)))
            return c

        pascal_line = []
        for j in range(n + 1):
            pascal_line.append(choose(n, j))
        return pascal_line
    else:
        return -1


d = 0
print(q4(d))
