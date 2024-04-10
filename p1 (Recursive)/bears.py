# int -> booelan
# Given integer n, returns True or False based on reachabilty of goal
def bears(n):
    '''If n is even, then you may give back n/2 bears.
    2. If n is divisible by 3 or 4, then you may multiply the last two digits of n and give back this many bears.
    3. If n is divisible by 5, then you may give back 42 bears.'''

    # base cases
    if (n == 42):
        return True

    if (n <= 0):
        return False

    # recursion to get closer to base cases
    if (n % 2) == 0:
        if bears(n // 2):
            return True

    if ((n % 3) == 0) or (n % 4 == 0):
        x = ((n % 10) * ((n // 10) % 10))
        if (x > 0) and bears(n - x):
            return True

    if (n % 5 == 0):
        if bears(n - 42):
            return True

    return False

