data = [
        ['T100',['I1','I2','I5']],
        ['T200',['I2','I4']],
        ['T300',['I2','I3']],
        ['T400',['I1','I2','I4']],
        ['T500',['I1','I3']],
        ['T600',['I2','I3']],
        ['T700',['I1','I3']],
        ['T800',['I1','I2','I3','I5']],
        ['T900',['I1','I2','I3']]
        ]

conf = 0.01

init = []
for i in data:
    for q in i[1]:
        if(q not in init):
            init.append(q)

init = sorted(init)
print(init)

sp = 0.4
s = int(sp * len(init))
print(s)

from collections import Counter
c = Counter()
for i in init:
    for d in data:
        if(i in d[1]):
            c[i]+=1

print("C1: ")
for i in c:
    print(str([i])+": "+str(c[i]))
print()

l = Counter()
for i in c:
    if(c[i] >= s):
        l[frozenset([i])]+=c[i]

print("L1: ")
for i in l:
    print(str(list(i))+": "+ str(l[i]))
print()

pl = l
pos = 1

for count in range(2,1000):
    nc = set()
    temp = list(l)
    for i in range(0, len(temp)):
        for j in range(i+1,len(temp)):
            t = temp[i].union (temp[j])
            if (len(t) == count):
                nc.add(temp[i].union (temp[j]))

    nc = list(nc)
    c = Counter()
    for i in nc:
        c[i]=0
        for q in data:
            temp = set(q[1])
            if(i.issubset (temp)):
                c[i]+=1

    print("C"+str(count)+": ")
    for i in c:
        print(str(list(i))+": "+ str(c[i]))
    print()

    l = Counter()
    for i in c:
        if(c[i]>=s):
            l[i]+=c[i]

    print("L"+str(count)+": ")
    for i in l:
        print(str(list(i))+": "+ str(l[i]))
    print()

    if(len(l)==0):
        break
    pl = l
    pos = count

    print("Result: ")
    print("L"+str(pos)+": ")
    for i in pl:
        print(str(list(i))+": "+ str(pl[i]))
    print()

l = []
for x in pl:
    temp = list(x)
    l.append(temp)

print(l)

from itertools import combinations

for i in l:
    print()
    print("For ",i)
    ab = frozenset(i)
    abfreq = pl[ab]
    print(abfreq)

    for j in range(1,len(i)):
        c = [frozenset(q) for q in combinations(i,j)]

        for a in c:
            b = ab - a
            afreq = 0
            for d in data:
                temp = set(d[1])
                if(a.issubset(temp)):
                    afreq +=1

            temp = abfreq / afreq

            if(temp >= conf):
                  print(a," -> ",b,"  :  ",(temp*100),"%")