lyst = [[1, 3, 4], [2, 7, 2], [5, 6, 8], [6, 10, 2], [8, 10, 4]]
lyst.sort(key=lambda x: x[1])  # sorts by finish times in increasing order
print(lyst)


def p(num):  # Find the interval with the latest eligible finish time
    for i in range(len(lyst) - 1, -1, -1):
        if lyst[i][1] <= num:
            return i + 1
    return 0


# Use top down (recursion w/ memoization) DP to find maximum
cache = {0: 0}


def opt(i):
    if i in cache:
        return cache[i]
    else:
        cache[i] = max(opt(i - 1), lyst[i - 1][2] + opt(p(lyst[i - 1][0])))
        return cache[i]


print("Maximum total value (TD):", opt(len(lyst)))

# Use bottom up (tabulation) DP to create the maximum of first i intervals
M = [0 for i in range(len(lyst) + 1)]
for i in range(1, len(lyst) + 1):
    M[i] = max(M[i - 1], lyst[i - 1][2] + M[p(lyst[i - 1][0])])
print("Maximum total value (BU):", M[-1])

# Now backtrack through M to find which intervals were included
sol = []
current = len(M) - 1
while current > 0:
    if M[current] != M[current - 1]:  # This means it was included in solution
        sol.append(lyst[current - 1])
        current = p(lyst[current - 1][0])  # Use p to revert to next eligible interval
    else:
        current -= 1
print("Intervals used to achieve maximum:", sol)