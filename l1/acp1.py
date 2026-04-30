print("Welcome to Chat Bot")

name = input("Please enter your name: ")
print(f"Nice to meet you, {name}!")

while True:
    mood = input("\nHow are you feeling today? (good/bad/okay): ").lower()

    if mood == "good":
        print("That's great to hear!  Keep smiling!")
    elif mood == "bad":
        print("I'm sorry to hear that  Hope things get better soon!")
    elif mood == "okay":
        print("Alright! Hope your day gets even better ")
    else:
        print("Invalid input! Please enter good, bad, or okay.")
        continue

    print("\nLet's talk about something!")
    print("1. Hobby")
    print("2. Study")
    print("3. Sports")

    choice = input("Choose a topic (1/2/3): ")

    if choice == "1":
        hobby = input("What is your favorite hobby? ")
        print(f"Wow! {hobby} sounds fun! ")
    elif choice == "2":
        subject = input("What is your favorite subject? ")
        print(f"{subject} is a great subject to learn! ")
    elif choice == "3":
        sport = input("Which sport do you like? ")
        print(f"{sport} is exciting! ")
    else:
        print("Invalid choice!")

    repeat = input("\nDo you want to continue chatting? (yes/no): ").lower()

    if repeat != "yes":
        print(f"\nThank you for chatting, {name}! Goodbye ")
        break