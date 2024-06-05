print('hello world')

print("one is equal to 2:",int(1==2))# in the quotes is what will print. Brackets/int will give response
print("one is equal to 1:",int(1==1))

print(f"a: {20>9}") 
print(f"b: {5==6}")
print(f"c: {1==0}")
print(f"d: {1==1}")


x=4
print(f"x<5 and x<10: {x<5 and x<10}")
print(f"x<5 and x<-4: {x<5 and x<-4}")
print(f"x<5 or x<4: {x<5 or x<4}")
print(f"x<5 or x<-4 {x<5 or x<-4}")

print(f"is 'matt' '==' 'matt'? {'matt'=='matt'}")

my_name="Chris"
print("assignment: ",my_name)
print("equality: ",my_name == "Chris")

print("comparison:","aa" < "b")
print("comparison:",5<6)

bank_balance = 50
print(f"bank balance before = {bank_balance}")

if bank_balance < 100:#This is a conditional. It will only run the next 2 lines if it finds this to be true
    money = 1000
    bank_balance += money   

print(f"bank balance after = {bank_balance}")


bank_balance =50
print(f"bank_balance = {bank_balance}")

if bank_balance <100:
    money=1000
    bank_balance +=money

print(f"bank_balance = {bank_balance}")


message_user = "no more money!"
if bank_balance <100:
    money=1000
    bank_balance +=money
    message_user = "you got paid!"

print(f"bank_balance = {bank_balance} message:{""}")

bank_balance= 50 
if bank_balance > 100:
    money=1000
    bank_balance += money
    print("balance is greater than or equal to 100")
else:
    print("balance is less than or equal to 100")

    books = ['harry potter', 'lord of the rings', 'matts autobiography']
    for book in books:
        print(f"book: {book}")

my_list = ['A','B','C']

my_tuple = ('X','Y','Z')

my_dict = {
    'first_name': 'Chris',
    'last_name': 'Eggert',
    'customer_id': 5
}

print(my_list[2])
print(my_tuple[2])
print(my_dict['customer_id'])

class vehicle():
    def __init__(self, make, model):
        self.make = make
        self.model = model
class car(vehicle):
    def __init__ (self, make, model, doors):
        super().__init__(make,model)
        self.doors = doors
        self.wheels = 4
    
class plane(vehicle):
    def __init__(self, make, model,doors):
        super().__init__(make, model)
        self.wings = True
        self.doors = doors

car = car(make='Hyundai',model='EV6',doors=4)
plane = plane(make='Gulfstream',model='g700',doors=2)

print(f'Car has Wheels: {car.wheels}')
print(f'Plane has Wings: {plane.wings}')




