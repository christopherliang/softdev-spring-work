x1 = [1,2,3]
x2 = [2,3,4]
x3 = [1,2]
x4 = ["red","white"]

def lists():
    print "x1: " + str(x1)
    print "x2: " + str(x2)
    print "x3: " + str(x3)
    print "x4: " + str(x4)
    return

lists()

# Union
def union(a,b):
    l = [ x for x in b if x not in a ]
    return a + l

print "union(x1,x2) = " + str(union(x1,x2))

# Intersection
def intersection(a,b):
    return [ x for x in a if x in b ]

print "intersection(x1,x2) = "+ str(intersection(x1,x2))

# Set Difference 
def setDiff(a,b):
    return [ x for x in a if x not in b ]
                
print "setDiff(x1,x2) = " + str(setDiff(x1,x2))

# Symmetric Difference
def symDiff(a,b):
    i = [ x for x in a if x not in b ]
    j = [ x for x in b if x not in a ]
    return i + j

print "symDiff(x1,x2) = " + str(symDiff(x1,x2))

# Cartesian Product
def cartesian(a,b):
    l = []
    for i in a:
        for j in b:
            l.append((i,j))
            return l
        
print "cartesian(x3,x4) = " + str(cartesian(x3,x4))
