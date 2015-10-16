#!/usr/bin/python

'''
The series 1^1 + 2^2 + 3^3 ... 10^10 = 10405071317.
Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def find_digits():
    count = 0

    for i in range(1,1001):
        count += i ** i
    return count % (10 ** 10)

print(find_digits())