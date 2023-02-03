'''
Kristen loves playing with and comparing numbers. She thinks that if she takes two different positive numbers,
the one whose digits sum to a larger number is better than the other.
If the sum of digits is equal for both numbers, then she thinks the smaller number is better.
For example, Kristen thinks that 13 is better than 31 and that 12 is better than 11.

Given an integer, can you find the divisor of  that Kristin will consider to be the best?
0<n<=10**5
'''
import math

n = 100
max_sum = (math.ceil(math.log10(n)))*9


def get_divisors(n):
    def get_sum(d):
        return sum(list(map(int, list(str(int(d))))))

    digit_sum = 1

    divisor = 1
    for i in range(1, int(math.ceil(math.sqrt(n + 1)))):
        if not n % i:
            g = n // i
            for d in sorted([i, g]):
                # print(d)
                s = get_sum(d)
                if s > digit_sum:
                    divisor = d
                    digit_sum = s
    return divisor


def solve(a, b, c):
    if c >= (a + b):
        return '1/1'
    else:
        # c<a+b
        min_ = min(a, b)
        max_ = max(a, b)

        if c <= min_:
            deno = 2 * a * b
            nume = pow(c, 2)
        elif c <= max_:
            deno = 2 * max_
            nume = 2 * c - min_
        else:
            deno = 2 * min_
            nume = 2 * c - max_
        nume = int(nume)
        deno = int(deno)
        divisor = math.gcd(nume, deno)

        nume = nume // divisor
        deno = deno // divisor
        # print(f'{c:0}/{deno}')
        return f'{nume:.0f}/{deno:.0f}'


if __name__ == '__main__':
    n = 12
    print(get_divisors(n))