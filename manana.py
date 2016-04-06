import random

#def dble(f):
#   name = f()
#   return name * 2

#get_name = dble()

def doubler(f):
    def inner():
        name = f()
        return name * 2
    return inner

@doubler
def get_name():
    names = ['tom','sue','harry','lisa','sarah','horatio']
    return random.choice(names)

print get_name()


#for x in range(10):
#   print dble(get_name)

def htmler(f):
    def inner():
        name = f()
        return "<html>" + name + "</html>"
    return inner

@htmler
def get_name():
    names = ['tom','sue','harry','lisa','sarah','horatio']
    return random.choice(names)

print get_name()

# equiv to:
# get_name = double(get_name)
#
# Takeaway:
#    You can write fxns that transform fxns
# A python decorator is shorthand
#   
#
#
#
#
#
#
#
#
