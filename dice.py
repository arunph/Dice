import random
import time

def dice():
      
       print("Rolling Dice....")
       time.sleep(random.randint(1,4))
       roll=random.randint(1,6)
       print(f'{roll}')
       return roll
roll=dice()
if roll==6:
    print("Roll One more time")
    dice()
else:
    print("continue")
