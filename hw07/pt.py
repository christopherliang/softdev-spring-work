# regular python list operations
def pt(n):
    retL = []
    for num in range(1,n):
        for num2 in range(1,n):
            for num3 in range(1,n):
                if (num**2 + num2**2) == num3**2:
                    retL.append([num,num2,num3])
    return retL

# list comprehensions
def pt2(n):
    return [(a,b,c) 
            for a in range(1,n)
            for b in range(1,n)
            for c in range(1,n)
            if a*a + b*b == c*c]

# list comprehensions w/ quicksort
def pt3(n):
    return 


print("pt2(3) = " + str(pt2(2)) ) 
print("pt2(5) = " + str(pt2(5)) ) 
print("pt2(27) = " + str(pt2(27)) ) 
