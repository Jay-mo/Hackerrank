
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    # answer = [list(perm) for perm in list(permutations([x,y,z])) if sum(perm) != n ]

    # print(answer)



    answer = [ [i, j, k] for i in range(x + 1) for j in range(y +1) for k in range(z + 1)  if sum([i, j, k]) != n]

    print(answer)