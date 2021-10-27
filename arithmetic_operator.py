"""
The provided code stub reads two integers from STDIN, a and b. Add code to print three lines where:

The first line contains the sum of the two numbers.
The second line contains the difference of the two numbers (first - second).
The third line contains the product of the two numbers.

Example

a = 3
b = 5

answer

8
-2
15

"""


if __name__ == '__main__':
    a = int(input('Enter first number: \n'))
    b = int(input('Enter second number: \n'))

    print(' Here are the answers')
    print(a + b)
    print(a - b)
    print(a * b)
