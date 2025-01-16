import random


adjectives = ["Cool", "Happy", "Fast", "Smart", "Silly", "Brave", "Witty", "Bold"]
nouns = ["Tiger", "Dragon", "Panda", "Knight", "Phoenix", "Gamer", "Lurker", "Wizard"]

def generate_username():
    return random.choice(adjectives) + random.choice(nouns) + str(random.randint(0, 99))


def save_username_to_file(username):
    with open("usernames.txt", 'a+') as file:
        file.write(username + "\n")


def username_generator():
    print("Welcome to the Random Username Generator!")
    username = generate_username()
    print(f"Generated Username: {username}")

    while True:
        decision = input("Do you want to customize your username? (YES/NO): ").strip().lower()
        if decision == 'yes':
            extra_characters = input("Enter additional characters (numbers, special characters, or both): ").strip()
            new_username = username + extra_characters

            
            if len(new_username) > 15:
                print(f"Your username exceeds 15 characters. Truncated to: {new_username[:15]}")
                new_username = new_username[:15]
            
            print(f"Final Customized Username: {new_username}")
            save_username_to_file(new_username)
            print("Username saved successfully!")
            break
        elif decision == 'no':
            print(f"Using Generated Username: {username}")
            save_username_to_file(username)
            print("Username saved successfully!")
            break
        else:
            print("Invalid input. Please enter YES or NO.")

if __name__ == "__main__":
    username_generator()
