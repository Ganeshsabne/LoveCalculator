import random

print("💖 Love Calculator 💖\n")

name1 = input("Enter your name: ")
name2 = input("Enter partner name: ")

score = random.randint(50, 100)

print(f"\n{name1} ❤️ {name2} = {score}%")

if score > 80:
    print("Perfect match 💕")
elif score > 60:
    print("Good compatibility 😊")
else:
    print("Needs more understanding 🌸")
