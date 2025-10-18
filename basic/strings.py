# str1 = "This is a string1"
# str2 = 'This is a string2'
# str3 = """This is a string3"""

str = "\nThis is a string.\nWe are creating it in python\n"
print(str)

str1 = "\nKamil"
str2 = "saeed"
final_str = str1 + str2

print(final_str)
print(len(final_str))

print(str1[0:4])
print(str2[-5:-2])

print()

print(str1.endswith("il"))
print(str2.capitalize())

print(str.replace("a","@"))
print(str.find("e"))
print(str.count("i"))


var = input("\nEnter first name: ")
print(len(var))