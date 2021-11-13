"""
https://www.hackerrank.com/challenges/defaultdict-tutorial/problem


"""


from collections import defaultdict

data = defaultdict(list)

group_A, group_B = list(map(int,input().split(" ")))

for i in range(group_A):
    data['group_A'].append(input())

for i in range(group_B):
    data['group_B'].append(input())

print(data['group_B'])
print(data['group_A'])

for character in data['group_B']:
    if data['group_A'].count(character) > 0:
        count = data['group_A'].count(character)
        index_pos = 0
        result = []
        for _ in range(count):
            index = data['group_A'].index(character, index_pos)
            index_pos = index
            index_pos += 1

            result.append(index +1)

        print(*result)
    else:
        print(-1)

