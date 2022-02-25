# Type Error
'''
len(12345)

num_char = len(input("What is your name?"))
print("Your name has" + num_char + " charaters.")
'''
num_char = len(input("What is your name?"))
print(type(num_char))
'''
str() funtion convert to string
'''
new_num_char = str(num_char)
print("Your name has " + new_num_char + " charaters.")


a = 123
print(type(a))
a = str(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))
