import sys


def F(k, s, f):
    '''
    number of Firecrackers needed if you have k mailboxes and you know that
    the mailbox can withstand s (lower bound) and that it definitely cannot
    withstand f (upper bound)
    '''
    if (k, s, f) in cache:
        return cache[(k, s, f)]
    cautious = (f * (f + 1) / 2) - (s * (s + 1) / 2)  # Start at safest and increase by 1
    if k == 1:
        cache[(k, s, f)] = int(cautious)
        return int(cautious)
    if s + 1 == f:
        cache[(k, s, f)] = f
        return f
    best = cautious
    for i in xrange(s + 1, f):  # Try i firecrackers
        current = i + max(F(k - 1, s, i - 1), F(k, i, f))  # It blows up or it doesn't
        best = min(best, current)
    cache[(k, s, f)] = int(best)
    return int(best)


def main():
    inputs = sys.stdin.read().splitlines()
    ln = int(inputs[0])
    for i in xrange(ln):
        k, f = inputs[i + 1].split()
        print(F(int(k), 0, int(f)))


cache = {}
main()