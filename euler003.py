if __name__ == '__main__':
    """
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143 ?
    """

    n = 600851475143
    div = 2
    prime_factor = []

    while True:
        if n % div == 0:
            prime_factor.append(div)

        if prime_factor:
            if reduce(lambda x, y: x*y, prime_factor) == n:
                break

        div = div + 1

    print prime_factor

