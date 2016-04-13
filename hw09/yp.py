import time 

def name_log(f):
    def inner(*arg):
        x = f(*arg)
        print f 

def randList(n, lower = -100, upper = 100):
    l = []
    for i in range(n):
        l.append(random.randrange(lower,upper))
    return l

@timer
@name_log
def quicksort(g):
    if len(g) <= 1:
        return g
    pivot = random.choice(g)
    lower = [x for x in g if x < pivot]
    upper = [x for x in g if x > pivot]
    return quicksort(lower) + ([pivot] * L.count(pivot)) + quicksort(upper)

def timer( f ):
    start_time = time.time()
    def inner( *arg ):
        return f( *arg )
    end_time = time.time()
    run_time = end_time - start_time
    print "execution time: " + str(run_time)
    return inner

def f_name( f ):
    return lambda: str(f.func_name) + ": " + f()

def foo(a,b,c):
    for x in range(5):
        print(a,b,c)
    return

closure = timer(foo)
closure( -2, 3, 'hello' )


