# Answers to Questions
#   Q1: How would you explain to your ducky what this Scheme code does?
#       (lambda (a b) (+ a b))
#   A1: A function that adds the two variables given
#   Q2: How would you explain to your ducky what this Scheme code does?
#       (define foo (lambda (a b) (+ a b)))
#   A2: Defines foo as the function mentioned in the previous answer  
#   Q3: Which of the four h() calls above would you say also created closures?
#   A3: h(1) and h(2) because they define functions that can be assigned to variables

def repeat(x):
    return lambda y: x * y

r1 = repeat("hello")
r2 = repeat("goodbye")

print r1(2) 
print r2(2) 
print repeat('cool')(3)

