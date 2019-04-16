
#Top Down

def pairingtd(n):
    paired = [1]*1000  # array of all 1s to 1000

    if paired != [1]: # if paired does not index 1 return paired at index input n
        return paired[n]
    if (n > 2):   # when n is more than to calculate paired at index of input n
        paired[n] = (pairingtd(n-1) + (n-1) * pairingtd(n-2))
        return paired[n]
    else:
        paired[n] = n
        return paired[n]
#Top Down v2

def pairingtd2(n):
    for i in range(1, n+1):
        paired = [i]*1000  # array from 1 to n * 1000 creating paired arrays of all numbers to n
        if paired[i] != 1:
            return paired[n]
        if paired[i] == n:
            return paired[i]
        if (i > 2):
            paired[i] = (pairingtd(n-1) + (n-1) * pairingtd(n-2))
            return paired[i]
#Bottom Up

def pairingbu(n):
    paired = [1 for i in range(n+1)]  #array of 1s to n+1
    for i in range(n+1):
        if (i <= 2):
            paired[i] = i  # stores 0 1 2 in the first 3 parts of the array
        else:
            paired[i] = paired[i-1] + (i-1) * paired[i-2]  # updates the array at index i with new value
    return paired[i]

def pairingbu2(n):

    for i in range(n+1):
        paired = [1 for n in range(n+1)]
        if (n <= 2):
            paired[n] = n
        else:
            paired[n] = pairingbu2(n-1) + (n-1) * pairingbu2(n-2)
    return paired[n]
#Brute Force

from math import factorial as f


def bruteforce(n):   #n total students, where n is at least 1
    total = 1  #include the one case where no students are in pairs
    for i in range(2,n+1,2):  #i is how many students are in pairs
        loners = n - i  #number of loners
        lonerposs = f(n)//f(i)//f(n-i)  #ways to choose loners n choose k n equals friends k number you can choose each time for loners n choose loners
        partnerposs = 1 #next three lines build ways to arrange pairs
        for j in range(i-1,0,-2):
            partnerposs *= j
        total += lonerposs*partnerposs  #total arrangements with i in pairs
    return int(total)

# Provided by Daniel Showalter