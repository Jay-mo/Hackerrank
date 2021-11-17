"""

https://www.hackerrank.com/challenges/py-set-intersection-operation/problem

"""


if __name__ == "__main__":
    english_students = int(input())

    set_of_english_students = set(map(int ,input().split(" ")))

    french_students = int(input())

    set_of_french_students = set(map(int ,input().split(" ")))

    intersection_english_french_students = set_of_english_students & set_of_french_students

    print(len(intersection_english_french_students))