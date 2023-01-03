print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome To Treasure Island \n Your mission is to find the treasure.")

ch_1 = input("You're at a cross road. Where do you want to go? Type 'left' or 'right'").lower
if(ch_1 == "right"):
    print("Fall into a hole. Game Over.")
else:
    ch_2 = input("You can either swim to the other side or wait for the boat to pick you up.What do you want to do \n Type 'swim' or 'boat'").lower()
    if ch_2 == "swim":
        print("You were attacked a trout while you were swimming \n Game Over.")
    else:
        print("You were taken across to the other side via a ferryman on a boat. You went to the other side safely.")
        ch_3 = input("After walking some distance you see 3 doors. Which door do you want to enter? Type 'blue' or 'yellow' or 'red'").lower()
        if(ch_3 == "red"):
            print("You were burned by fire as soon as you entered. \n Game Over.")
        elif(ch_3 == "blue"):
            print("You were eaten by beasts as soon as you entered through the door. \n Game Over.")
        elif(ch_3 == "yellow"):
            print("You Win!")
        else:
            print("Game Over.")