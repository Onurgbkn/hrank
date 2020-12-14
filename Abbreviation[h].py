f = open('C:/Users/lma10ur/Desktop/input/input0.txt', 'r')



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
                if any([i.isupper() for i in a[:i]]):
                    break
                else:
                    i = 0

        elif a[i].isupper():
            if len(n) != 0 and a[i] == n[0].upper():
                n.pop(0)
            else:
                print(i)
                print(len(b))
                break
        i -= 1

    if i == -1:
        print('YES')
    else:
        print('NO')




f.close()