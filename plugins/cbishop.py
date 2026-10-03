import random

AUTHOR = "Connor Bishop"
APP_NAME = "Dice summing"

def run():
  die_size = [1,2,3,4,5,6]
  die1 = random.choice(die_size)
  die2 = random.choice(die_size)
  result = die1 + die2
  return f"{APP_NAME}: Die 1: {die1} + Die 2: {die2} = {result}"
