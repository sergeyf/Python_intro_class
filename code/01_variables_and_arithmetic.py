'''
These notes and examples are based on 
a (much longer) Coursera Python class.
So you can go re-learn this when necessary.
https://class.coursera.org/programming1-002/
'''

# the python console is sort of like a calculator
10*15
114/12
114//12
114%12
12**2



# correct statements only!
3) - 2
45/0




# we can assign values to variables
base = 20
height = 12
area = base * height / 2




# and then we can print them out
print(area)




# and we can assign multiple values at the same time
x,y = 10,20
# and print them both
print(x,y)





# we can also check if two values are the same or not
x == 10
z = (x == 10.000)
print(z)





# there are other built-in functions
print( round(125.0925) )
print( abs(-124) )
print( pow(3,2) ) # same as 3**2
# how do look up what functions do?
# what other functions are there? let's google for it




# other types of data
print(type(3))

print(type(3.0))

print(type('a dog'))

print(type([3,3.0,'dog']))

print(type((1,2,3)))

print(type(True))

print(type(None))

print(type(print))





# strings in more detail!
x_string = 'one hundred years'
print(x_string)

y_string = '''now we can add
newlines and even apostrophes
and there won't be a problem.
see?'''
print(y_string)





# we can do all sorts of great things with strings
print( str.capitalize('dog') )

# and there are two ways to call the string functions
print( 'dog'.capitalize() )
# why? the Python intrepreter figured out that 'dog' 
# is a string and automatically references the library 
# that applies to its type so it replaces str with 'dog' 
# and then you don't need an input

# also functions have to have () or they aren't called
# it's like the period of a function.





# another string example 
first_name, second_name = str.split("James Joyce")
print(first_name)

# same thing but now the output is in a list
both_names = str.split("James Joyce")
print(both_names)

# and, just to get more practice
both_names_again = "James Joyce".split()
print(both_names == both_names_again)








# lists!?
x_list = [0,1,2,5]
print(x_list)

x_list.append(9)
print(x_list)

print(x[0])

print(x[100])

print(x[-1])



# you can get subsets of lists
print(x_list)

print(x_list[0:2])

print(x_list[1:])

print(x_list[:-1])







# and it turns out that strings are lists of characters
x_str = "Why not?"

print(x_str)

print(x_str[0:2])

print(x_str[1:])

print(x_str[:-1])





# what other types are there? google again