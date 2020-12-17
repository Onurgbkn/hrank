f = open('C:/Users/lma10ur/Desktop/input/input12.txt', 'r')



for _ in range(int(f.readline())):
    a = [_ for _ in f.readline().strip()]
    b = [_ for _ in f.readline().strip()]


    #print(''.join(a), ''.join(b))

    if len(a) < len(b):
        print('NO')
        continue

    if [i for i in a if i.isupper()] == b:
        print('YES')
        continue

    n = list()

    i = len(a)-1
    while i >= 0:
        if a[i].upper() == b[-1]:
            b.pop()

            if a[i].islower(): n.append(a[i])

            if len(b) == 0:
                for i in a[:i]:
                    if i.isupper():
                        if n[-1].upper() == i:
                            n.pop()
                        else:
                            break
                else:
                    i = 0

        elif a[i].isupper():
            if len(n) != 0 and a[i] == n[-1].upper():
                n.pop()
            else:
                break
        i -= 1

    if i == -1:
        print('YES')
    else:
        print('NO')




f.close()