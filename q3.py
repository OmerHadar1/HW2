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

