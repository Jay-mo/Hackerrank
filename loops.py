"""
Task
The provided code stub reads and integer, n, from STDIN. For all non-negative integers i< n, print n**2 .

Example
n =3
The list of non-negative integers that are less than 3 is [0,1,2]. Print the square of each number on a separate line.
"""


def square_0f_number(num):
    return [ n**2 for n in range(num)]

def print_list(num_list):
    for i in num_list:
        print (i)
        
a = square_0f_number(3)
print (a)