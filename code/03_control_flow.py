# if statements
x = 'pie'
if x == "pie":
    print("i am hungry")





# if-else statements
y = 5
if y > 5:
    print(y,'is larger than 5')
else:
    print(y + ' is smaller than or equal to 5')
    
    
    
    
    
    
# in python, proper indentention is mandatory
if x == 'pie':
print('this will never be printed')






# compound statements
if x == 'pie' or x == 'cake':
    y = x + ' ' + x
    print (y)





# if-elif-else statement 
x = 'dried goods'
if x == 'pie':
    x = x + ' ' + x
    print('key lime',x)
elif x == 'cake' or x == 'croissant':
    print('chocolate ' + x)
else:
    print('no dessert for anyone ever again')





# for statements
list_variable = range(10)
print(list_variable)
for thingie in list_variable:
    output = thingie**2 - thingie/4    
    print(output)
    





# while statements
z = 10
while z > 0:
    print(z,'is still greater than zero...')
    z = z - 1






# nesting control flow 
g = 10
counter = 0
while g > 0:
    print(z,'is still greater than zero...')
    for i in range(g):
        counter += i
    print("counter is up to",counter)
    z = z - 1
    




# for loops!
for i in [0,1,2,3]:
    print(i)
    
    



# the "range" function is very useful
for i in range(4):
    print(i)


    



# we have more flexibility with range
for i in range(1,10,3):
    print(i)
    
    




# example: writing a string backwards
x = "The forest and the trees."
for i in range(len(x)-1,-1,-1):
    print(x[i],sep='',end='')
    
    
    



# we probably should have just done this:
print(x[-1::-1])