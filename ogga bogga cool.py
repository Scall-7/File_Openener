open_file  = open(r"C:\Users\edsger\Desktop\Ogga bogga.txt",'r')
search = open_file.read()
uppercase = 0
lowercase = 0

for char in search:
    if (char.isupper):
        uppercase += 1

for char in search:
    if (char.islower):
        lowercase += 1

print(search)
print('amount of uppercase letters', uppercase)
print('amount of lowercase letters', lowercase)
open_file.close()