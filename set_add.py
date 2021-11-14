"""
https://www.hackerrank.com/challenges/py-set-add/problem
"""


if __name__ == "__main__":
    input_N = int(input())

    set_result = set()

    for i in range(input_N):
        set_result.add(input())


    print(len(set_result))
