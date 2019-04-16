h = [30, 40, 60, 10, 15, 25, 50]
l = [10, 25, 10, 15, 20, 15, 15]

#Bottom up solution
M = [0]
M.append(max(h[0],l[0])) #Best after 1st time period
for i in range(1,len(h)):
    M.append(max((M[-1]+l[i]),(M[-2]+h[i]))) #Take low, or erase previous and take high
print("Maximum value is",M[-1])


'''
opt2 = [0]  #incorrect version, as requested by book
i = 0
while i < len(h):
    if h[i+1] > l[i] + l[i+1]:
        opt2.extend([opt2[-1],opt2[-1]+h[i+1]])
        i += 2
    else:
        opt2.append(opt2[-1]+l[i])
        i += 1
print(opt2)
'''