import sys
fname = sys.argv[1]
file1 = open(fname + '.txt')
lista = []
lista1 = []
for line in file1:
    parts = line.split()
    if parts[0]<parts[1]:
        s1 = (str(parts[0]) , str(parts[1]),0)
        lista.append(s1)
    else:
        s1 = (str(parts[1]) , str(parts[0]),0)
        lista.append(s1)
file1.close()
for i in lista:
    days=1
    for x in lista1:
        if days==x[2]:
            if i[0]==x[0] or i[0]==x[1] or i[1]==x[1] or i[1]==x[0]:
                days=days+1
    m = (i[0],i[1],days)
    lista1.append(m)
    lista1.sort(key=lambda st: st[2])
lista1.sort()
file2 = open(fname + '_solved.txt', 'w')
for i in lista1:
    s1 = '(' + str(i[0]) + ', ' + str(i[1]) + ') ' + str(i[2]) +'\n'
    file2.write(s1)
    print(s1)
file2.close()
