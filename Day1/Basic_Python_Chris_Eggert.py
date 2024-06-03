print('Hello World!')

#this is syntax error since I didnt use the pound sign

print('Chewbacca') #this is an object of type string
print(3.4) #this is a nuber. Technically a float

order_price=23.99 #this is setting a literal (23.99) as a variable (order_price)
print(order_price) #Can print variable in order to retrieve literal

A=5
a=6

print(a) #Case matters in python
print(A)

user_name='Chris'
print('Hi my name is' + user_name + ".It's nice to meet you!")
print(f"Hi my name is  {user_name}  .It's nice to meet you!")#F srings make it so you don't need the addition signs and extra quotes\


my_name="wookie"
print(type(my_name))

my_name=1234
print(type(my_name))

#FUNCTION SYNTAX

def matts_super_cool_fun(a,b):
    output=a+b
    return output

print(matts_super_cool_fun(9,10))

print(a) #outside of the function global values will be used. Inside they can be reused

print(matts_super_cool_fun(9,10))#adds numbers
print(matts_super_cool_fun("9","10"))#Combines number to be 910
