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

    if z(sol) != 0:
        return False
    elif sol != int(sol) and sol is not False:
        sol = round(sol, 2)
        return sol



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

print(q5_a(g, -10, 10, 10))