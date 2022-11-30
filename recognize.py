num1 = 42 # number
num2 = 2.3 # number
boolean = True # boolean
string = 'Hello World' # string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # dictionary
fruit = ('blueberry', 'strawberry', 'banana') # tuple
print(type(fruit)) # initialize
print(pizza_toppings[1]) # access value
pizza_toppings.append('Mushrooms') # add value
print(person['name']) # accesss value
person['name'] = 'George' # change value
person['eye_color'] = 'blue' # add value
print(fruit[2]) # access value

if num1 > 45: # if statement
    print("It's greater")
else:                       # else statement
    print("It's lower")

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:         # else if statement
    print("It's a long word!")
else:
    print("Just right!")

for x in range(5): # for loop start
    print(x)
for x in range(2,5): # continue
    print(x)
for x in range(2,10,3): # continue
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1 # increment

pizza_toppings.pop() # removes the last index in list
pizza_toppings.pop(1) # removes the index of [1]

print(person)
person.pop('eye_color') # removes the eye_color value from dictionary
print(person)

for topping in pizza_toppings: # for loop start
    if topping == 'Pepperoni': # if statement
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break

def print_hello_ten_times(): # function parameter
    for num in range(10): # argument    
        print('Hello') # return

print_hello_ten_times()

def print_hello_x_times(x): 
    for num in range(x):
        print('Hello')

print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)