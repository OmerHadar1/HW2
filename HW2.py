def q1(input_file_name):
    """
    Read values from input file
    :param input_file_name: An input file name
    :return: The result of the division of the first number by the others
    """
    with open(input_file_name, 'r') as user_file:
        lst_text = user_file.read().split()  # List of al the numbers in the file
        try:  # A "try" block for dealing with exceptions like "FileNotFoundError", "ZeroDivisionError", "ValueError", and
            # "TypeError.
            div_num = float(lst_text[0])  # A variable of the first number in th string
            for i in range(1, len(lst_text)):  # That "for" loop divides al the numbers in the file
                div_num = div_num / float(lst_text[i])
            return div_num

        except FileNotFoundError:
            return -1

        except ZeroDivisionError:
            return -2

        except ValueError or TypeError:
            return -3


def q2(input_file_name):
    """
      a. Read words from input file
      b. Classify the words by length
      c. Write each word and its length to output file.
    """

    with open(input_file_name, "r") as input_file:
        word_lst = input_file.read().split()  # List of the words in the file
        sorted_lst = []
        while len(word_lst) != 0:
            shortest_word = min(word_lst, key=len)
            word_added = (shortest_word, len(shortest_word))
            sorted_lst.append(word_added)
            word_lst.remove(shortest_word)

    with open("output_" + input_file_name, "w") as output_file:
        output_file.write(str(sorted_lst))


def q3_a(n: int):
    """
    :param n: An integer number
    :return: All prime numbers up to n
    """
    if n == 1:
        print("There is no prime number")
    else:
        prime_lst = [2]
        for i in range(2, n + 1):
            test_prim = 0
            for item in prime_lst:
                if i % item != 0:
                    test_prim = 1
                else:
                    test_prim = 0
                    break
            if test_prim:
                prime_lst.append(int(i))
    return prime_lst


def q3_b(n: int):
    """
    uses the function q3_a
    :param n: An integer number
    :return: A list that contains all the three prime numbers combinations whose product is less than or equal to n.
    """
    prime_num = q3_a(n)
    prime_lst = []
    combinations_lst = []
    for i in range(len(prime_num)):
        if int(prime_num[i]) <= n/4:
            prime_lst.append(int(prime_num[i]))
        else:
            break
    for j in range(0, len(prime_lst)):
        for k in range(j, len(prime_lst)):
            for l in range(k, len(prime_lst)):
                if int(prime_lst[j]) * int(prime_lst[k]) * int(prime_lst[l]) <= n:
                    combinations_lst.append([prime_lst[j], prime_lst[k], prime_lst[l]])
    return combinations_lst


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


def q5_a(z, a, b, n):
    """
    The function returns the approximation of the root of 𝑧(𝑥) (𝑧(𝑥)=0) according to the bisection method.
    :param z: A mathematics function
    :param a: The start of thr interval
    :param b: The end of the interval
    :param n: the number of interactions that the function will do
    :return: the approximation of the root of 𝑧(𝑥) (𝑧(𝑥)=0) according to the bisection method.
    """
    sol = None
    low = a
    high = b
    for i in range(n):
        sol = (low + high) / 2
        if z(sol) * z(low) < 0:
            high = sol
        elif z(sol) * z(high) < 0:
            low = sol
        elif z(sol) == 0:
            break


def q5_b(f, g, a, b, n):
    """
    The function returns the approximation of a solution 𝑓(𝑥)=𝑔(𝑥) (using the bisection method)
    :param f: A mathematics function
    :param g: A mathematics function
    :param a: The start of thr interval
    :param b: The end of the interval
    :param n: the number of interactions that the function will do
    :return: the approximation of a solution 𝑓(𝑥)=𝑔(𝑥) (using the bisection method)
    """
    def h(x: int):
        """The function return the remainder between f(x) - g(x)
        :param x: the number we want to check
        :return : the remainder
        """
        return f(x) - g(x)
    return q5_a(h, a, b, n)


# ########### TESTING FUNCTIONS, DO NOT CHANGE THESE FUNCTIONS ################


def f(x):
    return 3 * x + 9


def g(x):
    return x ** 2 - 5

# ###############################################################################