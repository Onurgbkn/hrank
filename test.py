ar = [65, 74, 63, 72, 24, -32, 23, -7, -82, 62]
ar1 = [-64, -67, -7, -76, 60, 86, 49, -49, 63, 89, 91, 0, -41, 68]
ar2 = [91, 0, -41, 68, 95, 58, 34, -78, -76, -70, 33, 88, -50, -97]


def maxSubsetSum(arr):


    dp = len(arr) * [0]

    dp[0] = arr[0]
    dp[1] = max(arr[0], arr[1])

    for i in range(2, len(arr)):
        dp.append(max(arr[i]+dp[i-2], dp[i-1], arr[i]))

    print(dp[-1])



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





f = open("C:/Users/lma10ur/Desktop/test1.txt")

ar = list(map(int, f.readlines()[1].split()))
f.close()

maxSubsetSum(ar)
print("Result: ", find_max_sum(ar))
