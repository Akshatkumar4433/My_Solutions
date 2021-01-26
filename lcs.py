def table(array):
    for i in array:
        print(i)
def lcs(X, Y):

    m = len(X)
    n = len(Y)

    L = [[None] *(n + 1)]* (m + 1)

    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0 or j == 0:
                L[i][j] = 0

            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                #add one
            else:
                #this function will take last two subsques to see which
                #one is max
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

            print("i = " + str(i), "j =" + str(j))
            table(L)
            print()
    return L[m][n]

X = "ap"
Y = "ap"
print ("Length of LCS is ", lcs(X, Y))
