# assignment 3 solution

def max_of_list(x_list):
    intermediate_maximum = x_list[0]
    
    for i in x_list[1:]:
        if i > intermediate_maximum:
            intermediate_maximum = i
            
    return intermediate_maximum

print( max_of_list([-1,2,3,10,9]) )

print( max_of_list([-1,20,3,10,9]) )

print( max_of_list([-1,2,30,10,9]) )