print(r'''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Get some gold dude!")
print("You will be going through an adventure, and you can get the treasure if you make RIGHT decisions!!!")
print("Right now you have two boats, one at your left and other at your right.\nYou have travel 500kms to an island, which boat will you choose?")
x=input("Right boat or left boat? ")
if x=='left':
    print("Nice choice! but while travelling the fuel got ended.")
    y=input("Will you wait or swim to the Island? ")
    if y=='wait':
        print("Alright! nice choice but you have to wait for a long time!!\nYou've spotted a cruise ship\n that cruise ship took you to ISLAND\n You've reached mostly lets check whether you will win or not.")
        z=input("You have three caves infront of you, one has red rocks, other has yellow rocks and the last one has blue rocks\n which colour do you want to pick??")
        if z=='yellow':
            print("yaaaaahoooooo, YOU WON THE GREAT TREASURE,,, lets see what's in there\n shit its fake gold\nblame ramu for wasting your not so precious time.")
else:
    print("Can't you win a simple game\n shame on you\n make some right decisions in life")
