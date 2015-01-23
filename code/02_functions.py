# functions are a way to encapsulate code and reuse it later
def square(a):
    return a**2

    


# functions can have multiple inputs
def hypotenuse(a,b):
    return ( a**2 + b**2 )**0.5





# functions can have multiple outputs
# outputs come out as tuples
def quadratic_formula(a,b,c):
    output1 = ( -b + (b**2 - 4*a*c)**0.5 ) / ( 2*a )
    output2 = ( -b - (b**2 - 4*a*c)**0.5 ) / ( 2*a )
    return output1,output2
    



# we can pass parameters in a list in this special way
input_variable = [1,2,3]
print( quadratic_formula(*input_variable) )


