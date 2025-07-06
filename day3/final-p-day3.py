print("welcome to the treasure Island!!!")
print("yor mission is to find the treasure.")

chose1 = input('you are at crossroad where do you want to go? type "right" or "left "').lower()

if chose1 == "left" or chose1 == "Left":
    chose2 = input('you\'ve  come to the lake. there is an iland in the middle of the lake. type "wait" to wait for  '
                   'a boat. type "swim" to swim across.').lower()
    if chose2 == "wait":
        chose3 = input("you arrive at the island. there is 3 doors, red and blue and yellow. witch one do you chose?")
        if chose3 == "red":
            print("!!game over!!")
        elif chose3 == "yellow":
            print("**you found treasure**")
        elif chose3 == "blue":
            print("you game over bitch")
        else:
            print("you choose a door that dose\'nt exist%%")
    else:
        print("you lose")
else:
    print("you fell into a hole.game is over!!")

