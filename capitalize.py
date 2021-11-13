"""
You are asked to ensure that the first and last names of people begin with a capital letter in their passports. For example, alison heck should be capitalised correctly as Alison Heck.


Given a full name, your task is to capitalize the name appropriately.

Input Format

A single line of input containing the full name, S .


Sample Input

chris alan
Sample Output

Chris Alan
"""


def solve(s):
    s_list = list(map(str.capitalize, s.strip().split(" ")))
    print(s_list)
    return " ".join(s_list)

if __name__ == '__main__':
    

    s = input()

    result = solve(s)

    print(result)


# hello   world  lol