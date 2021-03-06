# if statements
x = 'not pie'
if x == "pie":
    print("i am hungry")





# if-else statements
y = 5.0000001
if y > 5:
    print(y,'is larger than 5')
else:
    print(str(y) + ' is smaller than or equal to 5')
    
    
    
    
    
    
# in python, proper indentention is mandatory
x = 'pie'
if x == 'pie':
    print('this will never be printed')
    if x == 'pie':
        print('this will also never be printed')






# compound statements
x = 'cake'
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
for stuff in list_variable:
    output = stuff**2 - stuff/4    
    print(output)





# while statements
z = 1024
while z > 1:
    print(z,'is still greater than zero...')
    z = z/2






# nesting control flow 
g = 10
counter = 0
while g > 0:
    print(g,'is still greater than zero...')
    for i in range(g):
        counter += i
    print("counter is up to",counter)
    g = g - 1
    




# for loops!
for i in [0,1,2,3]:
    print(i)
    
    



# the "range" function is very useful
for i in range(4):
    print(i)





# we have more flexibility with range
for i in range(1,100,25):
    print(i)
    
    




# example: writing a string backwards
x = "The forest and the trees."
for i in range(len(x)-1,-1,-1):
    print(x[i],end='')
    
    
    



# we probably should have just done this:
print(x[-1::-1])