import random
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstvuwxyz!@#%^&*()_+=-*/."
length_password = int(input("Enter The Length of Password: "))
a = "".join(random.sample(password,length_password))
print("Your Password is: ",a)
