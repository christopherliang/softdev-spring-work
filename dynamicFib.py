#dynamic fib
def memoize(f):
    memo = {} #hashmap/dict for O(1) lookup
    def inner(x):
        if x not in memo:
            memo[x] = f(x)
        return memo[x]
    return inner

@memoize
#regular fib
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)

print "fib(4): " + str(fib(4))
