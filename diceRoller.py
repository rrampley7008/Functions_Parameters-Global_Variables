

import random,time#import was spelt wrong and the semi-colon to a comma

s1 = "- - - - -\n|       |\n|   O   |\n|       |\n- - - - -\n"# Shows what it will display if the die is 1
s2 = "- - - - -\n| O     |\n|       |\n|     O |\n- - - - -\n"# Shows what it will display if the die is 2
s3 = "- - - - -\n| O     |\n|   O   |\n|     O |\n- - - - -\n"# Shows what it will display if the die is 3
s4 = "- - - - -\n| O   O |\n|       |\n| O   O |\n- - - - -\n"# Shows what it will display if the die is 4
s5 = "- - - - -\n| O   O |\n|   O   |\n| O   O |\n- - - - -\n"# Shows what it will display if the die is 5
s6 = "- - - - -\n| O   O |\n| O   O |\n| O   O |\n- - - - -\n"# Shows what it will display if the die is 6

def roll():  #Function for the actual rolling of the dice
    user = input("Would you like to roll?(yes/ no")
    if user == "yes":
        print("rolling.....")
        roll = random.randint(1,6)#tells the program to pick a random number between 1 and 6
        return roll
    elif print("You can now close the program"):
        4 == 4
def show_dice(roll):#Function to show which one of the six variables above it will display
    if roll == 1:
        print(s1)
    if roll == 2:
        print(s2)
    if roll == 3:
        print(s3)
    if roll == 4:
        print(s4)
    if roll == 5:
        print(s5)
    elif roll == 6:
        print(s6)

roll = roll()  #Calls the function and will store it as an variable
time.sleep(3)
show_dice(roll)
