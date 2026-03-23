# Dice Game
# j dotse
# 11/12/24
# roll the dice and pair the matches

import random
# function for the match





# my roll
my_list = []
count = 0
for i in range (1, 6):
    num = random.randint(1, 6)
    give_number = input("Press for roll:")
    print ("You rolled", num, "\n")
    my_list.append(num)
    target = num
    if target in my_list:
        count += 1

print ("You rolled", my_list)
print (count - 1)



# computer's roll
computer_list = []
for i in range (1, 6):
    num1 = random.randint(1, 6)
    #give_number = input("Press for roll:")
    #print ("You rolled", num, "\n")
    computer_list.append(num1)

print ("\nThe computer rolled", computer_list)

