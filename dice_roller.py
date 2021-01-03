import random
def main():
  dice_rolls = random.randint(1,100)
  dice_sum = 0
  for i in range(0,dice_rolls):
    roll = random.randint(1,6)
    #print(f'You rolled a {roll}')
    if roll==1:
      print(f'You rolled a {roll}! Critical Fail')
    elif roll==6:
      print(f'You rolled a {roll}! Critical Success!')
    else:
      dice_sum+=roll
  print(f'Your score is {dice_sum}')


if __name__== "__main__":
  main()