arr1 = list(map(int, "3 7 4 6 5".split()))      #13
arr2 = list(map(int, "2 1 5 8 4".split()))      #11
arr3 = list(map(int, "3 5 -7 8 10".split()))    #15

arr4 = list(map(int, "5 -1 -1 3 -2 5".split()))    #15


#185747029


#107352889

#175041179

def find_max_sum(arr):
    incl = 0
    excl = 0

    for i in arr:
        # Current max excluding i (No ternary in
        # Python)
        new_excl = excl if excl > incl else incl

        # Current max including i
        incl = excl + i
        excl = new_excl

        # return max of incl and excl
    return (excl if excl > incl else incl)


def Calc(arr):

    result = 0

    i = 0
    while i < len(arr):

        tempar = [i if i > 0 else 0 for i in arr[i:i+4]]

        if len(tempar) == 4:
            tmax = max(tempar[0] + tempar[2], tempar[0] + tempar[3], tempar[1] + tempar[3])

            if tempar[0] + tempar[2] == tmax or tempar[0] + tempar[3] == tmax:
                result += tempar[0]
                i += 2

            elif tempar[1] + tempar[3] == tmax:
                result += tempar[1]
                i+=3

        if len(tempar) == 3:
            if tempar[0] + tempar[2] > tempar[1]:
                result += tempar[0] + tempar[2]
            else:
                result += tempar[1]
            break

        if len(tempar) == 2:
            result += max(tempar)
            break

        if len(tempar) == 1:
            result += tempar[0]
            break

    return result


def maxSubsetSum(coll):
    a, b = 0, 0

    for val in coll:
        a, b = b, max(a, a + val, b, val)

    return b





f = open("C:/Users/lma10ur/Desktop/test1.txt")

ar = list(map(int, f.readlines()[1].split()))

#print(Calc(ar))
#print(find_max_sum(ar))
#print(maxSubsetSum(ar))

for i in range(len(ar)):
    if Calc(ar[:i]) != find_max_sum(ar[:i]):
        print(Calc(ar[:i]), find_max_sum(ar[:i]), i)
        print("The Difference: ",Calc(ar[:i]) - find_max_sum(ar[:i]))
        print(ar[i])

        temp = ar[i-5:i+5]
        print(temp)
        print(Calc(temp))
        print(find_max_sum(temp))

        break

#maxSubsetSum(arr3)