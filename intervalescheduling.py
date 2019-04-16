#
# def cached(mem):
#     cache = dict()
#
#     def opt(lists):
#         if lists in cache:
#             cache[lists] = mem(lists)
#         return cached[lists]
#     return opt

cache = {0:0}
p = {0:0}  # So it knows there is nothing at 0
def opt(lists):
    sort = sorted(lists, key=lambda x: x[1]) # sorts the interval based on when it first finished [start,finish,value]
    for i in range(len(sort)):
        x = sort[i-(len(sort))] # makes the highest interval
        value = x[2]  # Picks the value of the highest interval

    return value
print(opt([[1,5,2],[2,4,1],[3,7,3],[2,9,6],[4,10,9],[5,7,7]]))
