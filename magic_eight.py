import random
while True:
    userQuestion = input("Ask me a yes or no question: \n")
    
    raNum = random.randint(1, 20)
    if raNum == 1:
        print("It is certain. \n")
            
    elif raNum == 2:
        print("It is decidedly so.")
    
    elif raNum == 3:
        print("Without a doubt.")
    
    elif raNum == 4:
        print("Yes definitely. \n")

    elif raNum == 5:
        print("You may rely on it.")

    elif raNum == 6:
        print("As I see it, yes. \n")

    elif raNum == 7:
        print("Most likely.")

    elif raNum == 8:
        print("Outlook good.")

    elif raNum == 9:
        print("Yes.")

    elif raNum == 10:
        print("Signs point to yes.")

    elif raNum == 11:
        print("Reply hazy, try again. \n")

    elif raNum == 12:
        print("Ask again later.")

    elif raNum == 13:
        print("Better not tell you now.")

    elif raNum == 14:
        print("Cannot predict now.")

    elif raNum == 15:
        print("Concentrate and ask again.")

    elif raNum == 16:
        print("Don't count on it.")

    elif raNum == 17:
        print("My reply is no.")

    elif raNum == 18:
        print("My sources say no.")

    elif raNum == 19:
        print("Outlook not so good.")

    elif raNum == 20:
        print("Very doubtful.")

    ask_again = input("Ask again? (y/n): ")
    if ask_again.lower() != "y":
        break
    if ask_again.lower() == "y":
        continue
