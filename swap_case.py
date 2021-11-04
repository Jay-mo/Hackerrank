"""
You are given a string and your task is to swap cases. In other words, convert all lowercase letters to uppercase letters and vice versa.

Example

Www.HackerRank.com → wWW.hACKERrANK.COM
Pythonist 2 → pYTHONIST 2  


Sample Input 0

HackerRank.com presents "Pythonist 2".
Sample Output 0

hACKERrANK.COM PRESENTS "pYTHONIST 2".

"""


def swap_case(s):
    swapped_string = s.swapcase()
    return swapped_string

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)