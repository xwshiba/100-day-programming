def split(n):
    return n // 10, n % 10


def switch_T_F(x):
    return not x


def luhn_sum_iter(n):
    is_odd = True
    sum = 0
    while n > 0:
        n, last = split(n)
        if is_odd:
            sum = sum + last
        else:
            sum = sum + sum_digit(last * 2)
        is_odd = switch_T_F(is_odd)
    return sum


def luhn_sum_rec(n, sum=0, is_odd=False):
    if n == 0:
        return sum
    else:
        switch_T_F(is_odd)
        n, last = split(n)
        if is_odd:
            return luhn_sum_rec(n, sum + last, is_odd)
        else:
            return luhn_sum_rec(n, sum + sum_digit(last * 2), is_odd)


def sum_digit(n):
    if n < 10:
        return n
    else:
        n, last = split(n)
        return sum_digit(n) + last


luhn_sum_iter(321)


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    result = 0
    if x == 8:
        result += 1
        return result
    elif x < 10 and x != 8:
        return result
    x, last = split(x)
    return num_eights(x) + num_eights(last)


def split(n):
    return n // 10, n % 10


def num_eights(x):
    """Returns the number of times 8 appears as a digit of x.

    >>> num_eights(3)
    0
    >>> num_eights(8)
    1
    >>> num_eights(88888888)
    8
    >>> num_eights(2638)
    1
    >>> num_eights(86380)
    2
    >>> num_eights(12345)
    0
    >>> from construct_check import check
    >>> # ban all assignment statements
    >>> check(HW_SOURCE_FILE, 'num_eights',
    ...       ['Assign', 'AugAssign'])
    True
    """
    result = 0
    if x == 8:
        result += 1
        return result
    elif x < 10 and x != 8:
        return result
    x, last = split(x)
    return num_eights(x) + num_eights(last)


def pingpong(n):
    """Return the nth element of the ping-pong sequence.
    The ping-pong sequence counts up starting from 1
    and is always either counting up or counting down.
    At element k, the direction switches if k is a multiple of 8 or contains the digit 8.
    The first 30 elements of the ping-pong sequence are listed below,
    with direction swaps marked using brackets at the 8th, 16th, 18th, 24th, and 28th elements
    """
    if n == 1:
        return 1
    else:
        if add_or_minus(n) % 2 != 0:
            return pingpong(n-1) + 1
        return pingpong(n-1) - 1


def add_or_minus(index):
    num = 0
    for i in range(index):
        if i % 8 == 0 or num_eights(i) > 0:
            num += 1
    return num


def missing_digits(n):
    """Given a number a that is in sorted, increasing order,
    return the number of missing digits in n. A missing digit is
    a number between the first and last digit of a that is not in n.

    Write the recursive function missing_digits that takes a number n 
    that is sorted in increasing order 
    (for example, 12289 is valid but 15362 and 98764 are not). 
    It returns the number of missing digits in n. 
    A missing digit is a number between the first and last digit of n of a that is not in n. 


    >>> missing_digits(1248) # 3, 5, 6, 7
    4
    >>> missing_digits(1122) # No missing numbers
    0
    >>> missing_digits(123456) # No missing numbers
    0
    >>> missing_digits(3558) # 4, 6, 7
    3
    >>> missing_digits(35578) # 4, 6
    2
    >>> missing_digits(12456) # 3
    1
    >>> missing_digits(16789) # 2, 3, 4, 5
    4
    >>> missing_digits(19) # 2, 3, 4, 5, 6, 7, 8
    7
    >>> missing_digits(4) # No missing numbers between 4 and 4
    0
    """
    all_but_last, second_last, last = n // 10, n // 10 % 10, n % 10
    cond = last - second_last - 1
    if all_but_last == 0:
        return 0
    else:
        if cond <= 0:
            return missing_digits(all_but_last)
        else:
            return cond + missing_digits(all_but_last)
