#For loops
for i in range(5):
    print("Iteration:", i)
    print("Square:", i * i)
    print()


def double(number):
    """Function that returns double the input number."""
    return number * 2

print(double(4))
print(double('5'))


#foo() returns 5 because it uses its own local x.
#the global x remains 10.
#message is local to foo(), so accessing it outside the function causes a NameError.
x = 10
def foo():
    message = "Hello"
    x = 5
    return x

print(foo())
print(x)
#print(message)  # This will raise a NameError because it only exists inside the foo() function

#draw a square
"""
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
🧱🧱🧱🧱
"""

#def draw_square(size):
    #for i in range(size):
        #print("🧱" * size)
        #for j in range(size):
            #print("🧱", end="")
        #print()  # move to the next line after each row

def draw_square(size):
    for i in range(size):
        print("🧱" * size)

draw_square(4)

"""
Create a function to draw a triangle
🧱         1 = 0+1
🧱🧱       2 = 1+2
🧱🧱🧱     3 = 2+1
🧱🧱🧱🧱   4 = 3+1
"""
#for loop will go: 1, 2, 3, 4

#in row i, how many bricks are there? i+1

def draw_triangle(rows):
    for i in range(rows):
        print("🧱" * (i+1))

draw_triangle(4)

#challenge
"""
draw a triangle like this (size = 5)

   # 4 spaces + 1# = 5  5 - 0 - 1 = 4 # in row i, 4 spaces, 1 hashtag --> looking for an expression to find # of spaces --> i = 0
  ## 3 spaces +2# = 5  5 - 1 - 1 = 3
 ### 2 spaces +3# = 5  5 - 2 - 1 = 2
#### 1 space +4# = 5  5 - 3 - 1 = 1
"""

def draw_triangle(size):
    for i in range(size):
        print(" " * (size - i - 1) + "#" * (i + 1)) #need -1 because we dont want any extra spaces because # takes up one

draw_triangle(4)

#challenge 2
"""
draw a triangle like this

   #     
  ###   
 #####  
####### 
"""
def draw_triangle(size):
    for i in range(size):
        print