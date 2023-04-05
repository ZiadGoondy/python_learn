import string
import random

# create lists
s1 = list(string.ascii_lowercase)
s2 = list(string.ascii_uppercase)
s3 = list(string.digits)
s4 = list(string.punctuation)

# shuffle lists
random.shuffle(s1)
random.shuffle(s2)
random.shuffle(s3)
random.shuffle(s4)

# get length of password from user
get_num = input("enter the length of passwword : ")

# check user's input:
while True:
    try:
        get_num = int(get_num)
        if get_num < 6:
            get_num = input("enter the length of passwword should be > 6 : ")
        else:
            break
    except:
        print("you should print numbers inly")
        get_num = input("enter number : ")

# determine the percentage of letters & digits & punctuations
part1 = round(get_num * (30 / 100))
part2 = round(get_num * (20 / 100))

# create empty list for password
password = []

# start store characters in password list
for i in range(part1):
    password.append(s1[i])
    password.append(s2[i])
for i in range(part2):
    password.append(s3[i])
    password.append(s4[i])

random.shuffle(password)  # Shuffle characters

password = "".join(password)  # convert list to string

print(password)  # print final password
