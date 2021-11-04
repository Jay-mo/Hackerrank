"""
Task
You are given a string. Split the string on a " " (space) delimiter and join using a - hyphen.


Input Format
The one line contains a string consisting of space separated words.

Sample Input

this is a string   
Sample Output

this-is-a-string

"""


def split_and_join(line):
    line_list = line.split(" ")

    return "-".join(line_list)

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)