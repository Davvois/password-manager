import random, os, time

def writePassword(social, password):
    try:
        with open("passwords.txt", 'a') as file:
            file.write(f"\n{social} : {password}")

    except Exception as e:
        print(f"Error writing to file: {e}")

def generatePassword(length):
    password = ""
    characters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Z", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "z", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "!", "?"]

    for c in range(length):
        password += random.choice(characters)
    
    print(password)
    return password

def main():
    os.system("cls")
    logo = (" ______   ______     ______     ______        ______     ______     __   __   \n"
            "/\  == \ /\  __ \   /\  ___\   /\  ___\      /\  ___\   /\  ___\   /\ -.\  \   \n"
            "\ \  _-/ \ \  __ \  \ \___  \  \ \___  \     \ \ \__ \  \ \  __\   \ \ \-.  \ \n"
            " \ \_\    \ \_\ \_\  \/\_____\  \/\_____\     \ \_____\  \ \_____\  \ \_\\  \_\ \n"
            "  \/_/     \/_/\/_/   \/_____/   \/_____/      \/_____/   \/_____/   \/_/ \/_/ \n")

    while True:
        print(logo)
        length = int(input("Enter the length of the password > "))
        social = str(input("Enter the social media associated with the password > "))
        dots = "..."

        os.system("cls")

        if length >= 30:
            print(logo + "\nPassword is too long! Try again")
            time.sleep(2)
            os.system("cls")

        else:
            print("\nPlease wait, password is generating", end="")

            for c in dots:
                print(c, end="")
                time.sleep(1)

            os.system("cls")
            print(logo + "\nGenerated Password > ", end="")
            password = generatePassword(length)

            writePassword(social, password)
            break

if __name__ == "__main__":
    main()
