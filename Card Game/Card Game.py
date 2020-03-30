def welcome():
    c1 = input ("Player1: Do you want to log in or sign up? ")
    c1 = c1.lower()
    if "log" in c1:
        login1()
    if "sign" in c1:
        signup1()
    else:
        print ("Invalid answer. Please input \"log in\" if you have already have an existing accound or \"sign up\" to creat an account.\n")
        welcome()

def login1():
    username1 = input ("\nUsername: ")
    password1 = input ("Password: ")
    users = []
    file = open ("Users.txt", "r")
    contents = file.readlines()
    file.close()
    for lines in contents:
        users.append (lines.split("`"))
    for i in users:
        if i[0] == username1:
            if i[1] == password1:
                print("You have successfully logged in.\n")
                play2()
    print ("Incorrect username or password.\n")
    welcome()

def play2():
    c1 = input ("Player2: Do you want to log in or sign up? ")
    c1 = c1.lower()
    if "log" in c1:
        login2()
    if "sign" in c1:
        signup2()
    else:
        print ("Invalid answer. Please input \"log in\" if you have already have an existing accound or \"sign up\" to creat an account.\n")
        welcome()

def signup1():
    username = input ("\nCreate a username: ")
    password = input ("Create a password containing\n• 7 or more characters\n• an uppercase letter\n• a lowercase letter\n• a number\n• a special character: ")
    users = []
    file = open ("Users.txt", "r")
    contents = file.readlines()
    file.close()
    for lines in contents:
        users.append (lines.split("`"))
    for i in users:
        if i[0] == username:
            print ("Username already exists. Please create another.")
            signup1()
    num = False
    up = False
    low = False
    spe = False
    leng = False
    for char in password:
        if char.isdigit():
            num = True
        if char.isupper():
            up = True
        if char.islower():
            low = True
        if char.islower() != True and char.isupper() != True and char.isdigit() != True:
           spe = True
        if (len(password)) >=7:
           leng = True
    if num == True and up == True and low == True and spe == True and leng == True:
        file = open ("Users.txt", "a")
        file.write(username+"`"+password+"`\n")
        file.close()
        print ("You have successfully created an account.\n")
        play2()
    print ("Password is not strong another. Create another one.")
    signup1()

def login2():
    username2 = input ("\nUsername: ")
    password2 = input ("Password: ")
    users = []
    file = open ("Users.txt", "r")
    contents = file.readlines()
    file.close()
    for lines in contents:
        users.append (lines.split("`"))
    for i in users:
        if i[0] == username2:
            if i[1] == password2:
                print("You have successfully logged in.")
                instructions()
    print ("Incorrect username or password.\n")
    play2()

def signup2():
    username = input ("\nCreate a username: ")
    password = input ("Create a password containing\n• 7 or more characters\n• an uppercase letter\n• a lowercase letter\n• a number\n• a special character: ")
    users = []
    file = open ("Users.txt", "r")
    contents = file.readlines()
    file.close()
    for lines in contents:
        users.append (lines.split("`"))
    for i in users:
        if i[0] == username:
            print ("Username already exists. Please create another.")
            signup2()
    num = False
    up = False
    low = False
    spe = False
    leng = False
    for char in password:
        if char.isdigit():
            num = True
        if char.isupper():
            up = True
        if char.islower():
            low = True
        if char.islower() != True and char.isupper() != True and char.isdigit() != True:
           spe = True
        if (len(password)) >=7:
           leng = True
    if num == True and up == True and low == True and spe == True and leng == True:
        file = open ("Users.txt", "a")
        file.write(username+"`"+password+"`\n")
        file.close()
        print ("You have successfully created an account.")
        instructions()
    print ("Password is not strong another. Create another one.")
    signup2()

def play():
    cards = []
    player1 = 0
    player2 = 0
    for i in range (0,10):
        num = str(i)
        cards.append("R"+num)
        cards.append("B"+num)
        cards.append("Y"+num)
    random.shuffle (cards)
    for i in range (0,15):
        input ("\nPlayer 1: Press 'Return' to pick up a card.")
        current1 = cards[0]
        if "R" in current1:
            colour1 = "Red"
        elif "Y" in current1:
            colour1 = "Yellow"
        elif "B" in current1:
            colour1 = "Black"
        number1 = int(current1[len(current1)-1])+1
        number1 = str(number1)
        card1 = str(colour1+number1)
        number1 = int(number1)
        print ("Player 1: Your card is",card1+".\n")
        cards.remove(cards[0])
        input ("Player 2: Press 'Return' to pick up a card.")
        current2 = cards[0]
        if "R" in current2:
            colour2 = "Red"
        elif "Y" in current2:
            colour2 = "Yellow"
        elif "B" in current2:
            colour2 = "Black"
        number2 = int(current2[len(current2)-1])+1
        number2 = str(number2)
        card2 = str(colour2+number2)
        number2 = int(number2)
        print ("Player 2: Your card is",card2+".\n")
        cards.remove(cards[0])
        if colour1 == colour2:
            if number1 > number2:
                print("Player 1 wins the cards this round!")
                player1 = player1 + 2
            elif number2 > number1:
                print("Player 2 wins the cards this time!")
                player2 = player2+2
        else:
            if colour1 == "Yellow":
                if colour2 == "Black":
                    print("Player 2 wins the cards this time!")
                    player2 = player2+2
                elif colour2 == "Red":
                    print("Player 1 wins the cards this round!")
                    player1 = player1 + 2
            elif colour1 == "Black":
                if colour2 == "Yellow":
                    print("Player 1 wins the cards this round!")
                    player1 = player1 + 2
                elif colour2 == "Red":
                    print("Player 2 wins the cards this time!")
                    player2 = player2+2
            elif colour1 == "Red":
                if colour2 == "Yellow":
                    print("Player 2 wins the cards this time!")
                    player2 = player2+2
                elif colour2 == "Black":
                    print("Player 1 wins the cards this round!")
                    player1 = player1 + 2
    print ("\nThose were the last cards.\nPlayer 1 accumulated",player1,"cards.\nPlayer 2 accumualted",player2,"cards.")
    if player1 > player2:
        print("\nPlayer 1 is the winner!")
        again()
    else:
        print("\nPlayer2 is the winner!")
        again()

def again():
    ag = input ("\nWould you like to play again? ")
    ag = ag.lower()
    if "y" in ag:
        print("Great!")
        play()
    if "n" in ag:
        print ("Thanks for playing, goodbye!")
        exit()
    else:
        print ("Please input \"Yes\" to play again or \"No\" to exit the game.")
        again()

def instructions():
    print("\nHow to play:\n• This is a two player card game.\n• A deck will be shuffled.\n• The deck of cards each contains 30 cards, 10 which are yellow, 10 which are black and 10 which are red.\n• Each card has a number 1-10 for each colour.\n• Each card is unique.\n• Each player draws a card from the deck.\n• If the card is the same colour, the card with the highest number wins.\n• If the cards are different colours, the winning card is:\nBlack + Red = Red\nYellow + Red = Yellow\nBlack + Yellow = Black\n• The person who drew the winning card gets to keep both cards.\n• The winner is the player who has the most cards after all 30 cards have been drawn.")
    under = input ("\nAre you ready to play? ")
    under = under.lower()
    if "y" in under:
        print("Okay then. Let's go!")
        play()
    if "n" in under:
        instructions()
    else:
        print ("Please input \"yes\" to start the game or \"no\" for the instructions to repeated.")
        instructions()

import random
print ("Welcome to the card game!")
welcome()