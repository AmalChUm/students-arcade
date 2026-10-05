import random

AUTHOR = "Tyler Guest"
APP_NAME = "Random Number"

def random_num(start:int, stop:int) -> int:
  return random.randint(start, stop)

def run():
  start, stop = 1, 100
  rnum = random_num(start, stop)
  result = rnum
  return f"Your {APP_NAME} is: {result}"