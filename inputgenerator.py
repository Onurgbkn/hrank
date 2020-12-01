import  random


def Generate(n):

    for _ in range(int(n)):
        yield random.randint(-10000, 10000)


s = " ".join(map(str, (Generate(1000))))




f = open("C:/Users/lma10ur/Desktop/test1.txt", "w")

f.writelines("0\n")
f.writelines(s)

f.close()



