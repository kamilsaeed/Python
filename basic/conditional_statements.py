age = int(input("\nEnter your age: "))

if( age >= 20 and age <= 60):
    print("You are Adult\n")
elif(age >= 13 and age <= 19):
    print("You are a Teenager\n")
elif(age >= 60):
    print("You are Senior Citizen\n")
else:
    print("You are a Child\n")


num = int(input("Enter a number: "))

if(num % 2 == 0):
    print("Even Number\n")
else:
    print("Odd Number\n")