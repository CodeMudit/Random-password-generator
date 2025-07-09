import string 
import secrets

print("Welcome to random password generator")

length = int(input("Enter the length of the password you want : "))

characters = string.ascii_letters + string.punctuation + string.digits 

password = ''.join(secrets.choice(characters) for _ in range (length))
print(f"Your password has been generated successfully : {password}")
