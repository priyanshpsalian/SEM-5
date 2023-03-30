import numpy as num

graph = {
    'b' : ['a','c','d', 'e'],
    'a' : ['d', 'c'],
    'c' : ['d','b', 'e'],
    'd' : ['b','c'],
    'e' : ['b','c','d']
}
iterationNo = 7

print("Graph")
print(graph)

# print(graph['b'].count('a'))

A = []

for i in graph.keys():
    a = []
    for j in graph.keys():
        if(graph[j].count(i)!=0):
            a.append(1/len(graph[j]))
        else:
            a.append(0)
    A.append(a)
print("Page rank Matrix")
for i in A:
    for j in i:
        print(j,' ',end=" "),
    print('')

B = []

for i in range(0,len(A)):
    B.append([1])
print("Iteration Table")
print(B)

for i in range(0,iterationNo):
    C = num.matmul(A,B)
    print(C)