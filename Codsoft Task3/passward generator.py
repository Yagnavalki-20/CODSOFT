import random
Letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','^','&','*',',','(',')','+','-','_','=']
print("Welcome to passward generator!")
n_letters = int(input("how many letters you want in your passward?\n"))
n_symbols = int(input("how many symbols you want in your passward?\n"))
n_numbers = int(input("how many numbers you want in your passward?\n"))
passward = " "
for i in range(1,n_letters+1):
    char = random.choice(Letters)
    passward += char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    passward += char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    passward += char
print(passward)
print("=======================================================")
passward_list = []
for i in range(1,n_letters+1):
    char = random.choice(Letters)
    passward_list += char
for i in range(1,n_symbols+1):
    char = random.choice(symbols)
    passward_list += char
for i in range(1,n_numbers+1):
    char = random.choice(numbers)
    passward_list += char
print(passward_list)
print("========================================================")
random.shuffle(passward_list)
print(passward_list)
passward = " "
for char in passward_list:                                                  
    passward += char
print(passward)

