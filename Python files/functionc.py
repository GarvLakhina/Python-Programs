#function = a block of reusable code 
#           use () to invoke it

#print("Happy Birthday To You")
#print("You are old")
#print("Happy Birthday To You")

def happy_birthday():
    print("Happy Birthday To You")
    print("You are old")
    print("Happy Birthday To You")

#happy_birthday()

def happy_birthday_with_name(name,age):
    print(f"Happy Birthday To {name}")
    print(f"You are {age} years old")
    print("Happy Birthday To You")

#happy_birthday_with_name("Jitesh",40)

def sum(x,y):
    z=x+y
    return z

result=sum(2,3)
#print(result)