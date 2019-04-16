import timeit

from math import factorial as f


# Top down Version 1

# pairingtdt1 = timeit.timeit('pairingtd(4)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt1)
#
# pairingtdt2 = timeit.timeit('pairingtd(5)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt2)
#
# pairingtdt3 = timeit.timeit('pairingtd(10)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt3)
#
# pairingtdt4 = timeit.timeit('pairingtd(20)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt4)
#
# pairingtdt5 = timeit.timeit('pairingtd(50)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt5)
#
# pairingtdt6 = timeit.timeit('pairingtd(90)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt6)
#
# pairingtdt7 = timeit.timeit('pairingtd(150)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt7)
#
# pairingtdt8 = timeit.timeit('pairingtd(300)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt8)
#
# pairingtdt9 = timeit.timeit('pairingtd(600)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt9)
#
# pairingtdt10 = timeit.timeit('pairingtd(900)', setup='from pairedfriends1 import pairingtd', number=1000)
#
# print(pairingtdt10)
# # Top down Version 2
#
#
# pairingtd2t1 = timeit.timeit('pairingtd2(4)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t1)
#
# pairingtd2t2 = timeit.timeit('pairingtd2(5)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t2)
#
# pairingtd2t3 = timeit.timeit('pairingtd2(10)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t3)
#
# pairingtd2t4 = timeit.timeit('pairingtd2(20)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t4)
#
# pairingtd2t5 = timeit.timeit('pairingtd2(50)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t5)
#
# pairingtd2t6 = timeit.timeit('pairingtd2(90)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t6)
#
# pairingtd2t7 = timeit.timeit('pairingtd2(90)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t7)
#
# pairingtd2t8 = timeit.timeit('pairingtd2(90)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t8)
#
# pairingtd2t9 = timeit.timeit('pairingtd2(90)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t9)
#
# pairingtd2t10 = timeit.timeit('pairingtd2(90)', setup='from pairedfriends1 import pairingtd2', number=1000)
#
# print(pairingtd2t10)
# #
# # Bottom up Version 1
#
# pairingbut1 = timeit.timeit('pairingbu(4)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut1)
#
# pairingbut2 = timeit.timeit('pairingbu(5)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut2)
#
# pairingbut3 = timeit.timeit('pairingbu(10)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut3)
#
# pairingbut4 = timeit.timeit('pairingbu(20)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut4)
#
# pairingbut5 = timeit.timeit('pairingbu(50)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut5)
#
# pairingbut6 = timeit.timeit('pairingbu(90)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut6)
#
# pairingbut7 = timeit.timeit('pairingbu(150)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut7)
#
# pairingbut8 = timeit.timeit('pairingbu(300)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut8)
#
# pairingbut9 = timeit.timeit('pairingbu(600)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut9)
#
# pairingbut10 = timeit.timeit('pairingbu(900)', setup='from pairedfriends1 import pairingbu', number=1000)
#
# print(pairingbut10)
#
# # Bottom up Version 2
#
# pairingbu2t1 = timeit.timeit('pairingbu2(4)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t1)
#
# pairingbu2t2 = timeit.timeit('pairingbu2(5)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t2)
#
# pairingbu2t3 = timeit.timeit('pairingbu2(10)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t3)
#
# pairingbu2t4 = timeit.timeit('pairingbu2(20)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t4)
#
# pairingbu2t5 = timeit.timeit('pairingbu2(50)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t5)
#
# pairingbu2t6 = timeit.timeit('pairingbu2(90)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t6)
#
# pairingbu2t7 = timeit.timeit('pairingbu(150)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t7)
#
# pairingbu2t8 = timeit.timeit('pairingbu(300)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t8)
#
# pairingbu2t9 = timeit.timeit('pairingbu(600)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t9)
#
# pairingbu2t10 = timeit.timeit('pairingbu(900)', setup='from pairedfriends1 import pairingbu2', number=1000)
#
# print(pairingbu2t10)

# Brute Force

pairingbf1 = timeit.timeit('bruteforce(4)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf1)

pairingbf2 = timeit.timeit('bruteforce(5)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf2

pairingbf3 = timeit.timeit('bruteforce(10)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf3)

pairingbf4 = timeit.timeit('bruteforce(20)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf4)

pairingbf5 = timeit.timeit('bruteforce(50)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf5)

pairingbf6 = timeit.timeit('bruteforce(90)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf6)

pairingbf7 = timeit.timeit('bruteforce(150)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf7)

pairingbf8 = timeit.timeit('bruteforce(300)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf8)

pairingbf9 = timeit.timeit('bruteforce(600)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf9)

pairingbf10 = timeit.timeit('bruteforce(900)', setup='from pairedfriends1 import bruteforce', number=1000)

print(pairingbf10)


