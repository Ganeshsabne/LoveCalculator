import time

print("\n💖 Welcome to Heart Proposal Program 💖\n")
time.sleep(1)

name = input("Enter your name: ")
time.sleep(1)

crush = input("Enter your crush name: ")
time.sleep(1)

print("\nLoading your proposal...")
time.sleep(2)

print("""
      ❤️     ❤️
   ❤️    ❤️ ❤️    ❤️
 ❤️        ❤️        ❤️
   ❤️               ❤️
      ❤️           ❤️
         ❤️       ❤️
            ❤️ ❤️
              ❤️
""")

time.sleep(1)

print(f"\nHey {crush} 💕")
time.sleep(1)
print(f"{name} wants to say something special to you...\n")
time.sleep(2)

choice = input("Will you be mine? (yes/no): ").lower()

if choice == "yes":
    print("\n🥰 Yayyy! You made my heart so happy ❤️")
    print("Forever starts now 💍💕")
else:
    print("\n💔 Oh no! Still wishing you happiness 🌸")
