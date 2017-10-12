if __name__ == '__main__':
    """
        A palindromic number reads the same both ways.
        The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.
        
        Find the largest palindrome made from the product of two 3-digit numbers.
    """

    results = dict()

    for a in range(100, 1000):
        for b in range(100, 1000):
            results[a * b] = (a, b)

    for r in sorted(results, reverse=True):
        if str(r) == str(r)[::-1]:
            print r
            break
