#Phillip Tracy, Steven Hall, Teddy Weaver, Austin Lu
#October 29, 2020
#Implement the Longest Common Subsequence algorithm as described during
#in in-person meeting.  As usual, if you choose this option,
#implement yoursolution inPython 3,and share your code through
#a github repository(I am going to share with submission).
#References: docs.python.org, geeksforgeeks, tutorialspoint, w3schools

#Problem: Longest Common Subsequence
#Input: Two subsequences a and b
#Output: Longest subsequence of both a and b

#Step1: Optimal solution for (a,b) contains optimal solution for (ai,bj)
#Step2: Define length of LCS recursively
#Step3: Compute maximum length bottom up, using storage
#Step4: Extract LCS

def lcs(X, Y, n1, n2):
    #Array for storing dynamic programming solutions
    S = [[0 for x in range(n2+1)] for x in range(n1+1)]
    #bottom up computation
    for i in range(n1+1):
        for j in range(n2+1):
            if i == 0 or j == 0:
                S[i][j] = 0
            elif X[i-1] == Y[j-1]:
                S[i][j] = S[i-1][j-1] + 1
            else:
                S[i][j] = max(S[i-1][j], S[i][j-1])
    #Formatting for next section
    index = S[n1][n2]
    lcs = [""] * (index+1)
    lcs[index] = ""
    i = n1
    j = n2
    #Extracting
    while i > 0 and j > 0:
        if X[i-1] == Y[j-1]:
            lcs[index-1] = X[i-1]
            i -= 1
            j -= 1
            index -= 1
        elif S[i-1][j] > S[i][j-1]:
            i -= 1
        else:
            j -= 1   
    ret = "".join(lcs)
    return ret
    
a = "AGGTAB"
b = "GXTXAYB"
print("The first string is: " + a)
print("The second string is: " + b)
print("There LCS is: " + lcs(a, b, len(a), len(b)))
