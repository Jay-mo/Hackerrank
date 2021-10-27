import numpy

n, m, p = map(int, input().split())


rows = m + n
ouput = []


for i in range(rows):
    ouput.append( [int(x) for x in input().split()])

print(numpy.array(ouput))