# assignment 2 solution

def max_of_three(x1,x2,x3):
    if x1 > x2:
        intermediate_maximum = x1
    else:
        intermediate_maximum = x2
    
    if intermediate_maximum < x3:
        maximum = x3
    else:
        maximum = intermediate_maximum
    
    return maximum
    
# testing the function
print( max_of_three(1,2,3) )

print( max_of_three(4,2,3) )

print( max_of_three(1,5,3) )