import time 

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


