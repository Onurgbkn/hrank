arr1 = list(map(int, "3 7 4 6 5".split()))      #13
arr2 = list(map(int, "2 1 5 8 4".split()))      #11
arr3 = list(map(int, "3 5 -7 8 10".split()))    #15


#185747029


#107352889

#175041179


def Calc(arr):

    result = 0

    i = 0
    while i < len(arr):

        tempar = [i if i > 0 else 0 for i in arr[i:i+4]]

        if len(tempar) == 4:
            tmax = max(tempar[0] + tempar[2], tempar[0] + tempar[3], tempar[1] + tempar[3])

            if tempar[0] + tempar[2] == tmax or tempar[0] + tempar[3] == tmax:
                result += tempar[0]
                print(result)
                i += 2
                
            elif tempar[1] + tempar[3] == tmax:
                result += tempar[1]
                print(result)
                i+=3

        if len(tempar) == 3:
            if tempar[0] + tempar[2] > tempar[1]:
                result += tempar[0] + tempar[2]
                print(result)
            else:
                result += tempar[1]
                print(result)
            break

        if len(tempar) == 2:
            result += max(tempar)
            print(result)
            break

        if len(tempar) == 1:
            result += tempar[0]
            max(tempar[0])
            break

    return result


def maxSubsetSum(coll):
    a, b = 0, 0

    for val in coll:
        a, b = b, max(a, a + val, b, val)
        print(a, b)





f = open("C:/Users/lma10ur/Desktop/input06.txt")

ar = list(map(int, f.readlines()[1].split()))

#print(Calc(ar))

maxSubsetSum(arr3)