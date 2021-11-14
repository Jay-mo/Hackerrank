"""

https://www.hackerrank.com/challenges/symmetric-difference/problem?
"""


if __name__ == "__main__":
    input_M = int(input())
    set_a = set(list(map(int, input().split(" "))))

    input_N = int(input())
    set_b = set(list(map(int, input().split(" "))))


    set_c = set_a.symmetric_difference(set_b)

    for i in sorted(set_c):
        print(i)
