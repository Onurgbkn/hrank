# https://www.hackerrank.com/challenges/max-array-sum/problem

ar = [65, 74, 63, 72, 24, -32, 23, -7, -82, 62]


def Calc(arr):
    result = 0
    result2 = 0

    i = 0
    while i < len(arr)-2:

        tempar = [i if i > 0 else 0 for i in arr[i:i + 3]]

        if tempar[0] > tempar[1]:
            result += tempar[0]

            result2 = result

            i += 2
            continue

        else:
            result2 += tempar[1]

        i += 1




    return result + max(arr[i], arr[i+1])




def maxSubsetSum(coll):
    a, b = 0, 0

    for val in coll:
        a, b = b, max(a, a + val, b, val)

    return b

print(Calc(arr2))
