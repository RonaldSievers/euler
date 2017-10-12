if __name__ == '__main__':
    """
        2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
        
        What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    """

    def test_divisibility(n):
        for i in range(20, 1, -1):
            if n % i <> 0:
                return False
        return True

    i = 20
    while True:
        if test_divisibility(i):
            print i
            break
        i += 20
