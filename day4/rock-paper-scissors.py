import random

chose = int(input("what do you chose? 0 for rock?1 for paper?2 for or scissor?"))
cp_chose = random.randint(0, 2)
print(f"computer chose {cp_chose}")

if chose >= 3 or chose < 0:
  print("you typed the wrong number.")
elif chose == 0 and cp_chose == 2:
    print("user wins!")
elif cp_chose == 0 and chose == 2:
    print("you lose")
elif cp_chose > chose:
    print("you lose12!")
elif chose > cp_chose:
    print("computer wins!")
elif cp_chose == chose:
    print("it's a drew>-<")


