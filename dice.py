#importing random module
import random
#importing time module
import time

#defining dice function
def dice():
      #printing Rolling Dice
       print("Rolling Dice....")
      #using time.sleep for waiting dice to roll upto 4 seconds
       time.sleep(random.randint(1,4))
      #generating random numbers of the dice and storing it in 'roll' variable
       roll=random.randint(1,6)
      #printing the stored random value in 'roll' variable
       print(f'{roll}')
       return roll
roll=dice()
#checking the condition for the number 6. As to get one more chance for roll, if user got number 6
if roll==6:
    print("Roll One more time")
#calling dice function to repeat the sequence
    dice()
else:
    print("continue")
