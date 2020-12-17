def func(a, b):
    if (len(a) < len(b)):
        return False

    if (len(b) == 0):
        for c in a:
            if (ord(c) < 97):
                return False
        return True

    if (a[0] != b[0]):
        if (ord(a[0]) >= 97):
            return func(a[1:], b) or func(a[0].capitalize() + a[1:], b)
        else:
            return False
    else:
        return func(a[1:], b[1:])


def abbreviation(a, b):
    if (func(a, b)):
        return "YES"
    else:
        return "NO"


f = open('C:/Users/lma10ur/Desktop/input/input08.txt', 'r')
for _ in range(int(f.readline())):
    a = f.readline()
    b = f.readline()

    print(abbreviation(a, b))


f.close()