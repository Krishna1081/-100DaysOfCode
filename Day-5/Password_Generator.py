import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

password_length = nr_letters + nr_symbols + nr_numbers
easy_password = ""
char_list = []
for i in range(nr_letters):
    random_letter = random.randint(0,len(letters)-1)
    easy_password += letters[random_letter]
    char_list += letters[random_letter]

for j in range(nr_numbers):
    random_numbers = random.randint(0,len(numbers)-1)
    easy_password += numbers[random_numbers]
    char_list += numbers[random_numbers]

for k in range(nr_symbols):
    random_symbols = random.randint(0,len(symbols)-1)
    easy_password += symbols[random_symbols]
    char_list += symbols[random_symbols]

print("Easy: " + easy_password)

hard_password = ""
hard_password_len = 0
tally = []
while(hard_password_len < password_length):
    random_char = random.randint(0, len(char_list)-1)
    if char_list[random_char] not in tally :
        hard_password += char_list[random_char]
        tally.append(char_list[random_char])
        hard_password_len+=1
print("hard: " + hard_password)