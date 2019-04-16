n = 8    #Number of months
M = 15   #Moving cost
N = [1, 3, 20, 30, 5, 5, 5, 5]   #New York operating costs
S = [50, 20, 2, 4, 9, 9, 9, 9]   #San Fran operating costs

#Bottom up solution
optN = [0 for i in range(n)]  #optN[i] is best total for first i months, ending in NY
optS = [0 for i in range(n)]  #Same but for SF
optN[0], optS[0] = N[0], S[0]

for i in range(1,n):
    optN[i] = min(optN[i-1]+N[i], optS[i-1]+M+N[i])
    optS[i] = min(optS[i-1]+S[i], optN[i-1]+M+S[i])
