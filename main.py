# Split string method
names_string = input("Give me everybody's names, separated by a comma. \n")
names = names_string.split(", ")
# print(names)
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

x = len(names)
num = random.randint(0, x)

print(f"{names[num]} is going to buy the meal today!")

