#!/usr/bin/python3
""" FizzBuzz
"""
import sys

def fizzbuzz(n):
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3) == 0 and (i % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (i % 3) == 0:
            tmp_result.append("Fizz")
        elif (i % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./0-fizzbuzz.py <number>")
        sys.exit(1)
    
    try:
        number = int(sys.argv[1])
    except ValueError:
        print("The argument should be an integer")
        sys.exit(1)

    fizzbuzz(number)
