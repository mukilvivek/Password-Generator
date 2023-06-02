print("RULES")
print("Password must be 10 digits")
print("Password must start with a capital letter")
print("Password must contain one lowercase letter")
print("Password must contain one special character")
print("Password must contain one number")

password = input("Please enter your password: ")

for char in password:
    k = char.islower()
    if k == True:
        lower = True
        break
if (k != 1):
    lower = False

if(password[0].isupper()):
       capital = True
elif(password[0].islower()):
       capital = False

while True:
    if (any(char.isdigit() for char in password) and any(not c.isalnum() for c in password) and (len(password)==10) and capital and lower):
        print("Password accepted")
        break
    else:
        print("Password denied")
        password = input("Please try a different password: ")

