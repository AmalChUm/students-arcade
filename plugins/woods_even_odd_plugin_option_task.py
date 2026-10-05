import random

AUTHOR = "Moesha Woods"
APP_NAME = "Even or Odd Helper"

def run():
      # each option probability can be adjusted as needed
      even_probability= 70
      odd_probability=30

      # integer range can be adjusted as needed
      minimum_integer=1
      maximum_integer=100

      #set string values to even/odd for better readability & easier modification
      option1="even"
      option2="odd"
      
      # helper variable for random selection count
      number_choices_selections = 1

      # different statements after even/odd probability response 
      option1_statements=[
          "this number is even.",
          "you got an even number.",
          "this is an even number!",
          "the number you selected is even."
      ]
      
      option2_statements=[
          "this number is odd.",
          "you got an odd number.",
          "this is an odd number!",
          "the number you selected is odd."
      ]

      # randomly select even or odd based on probability
      choice = random.choices(
          [option1, option2],
          weights=[even_probability, odd_probability],
          k=number_choices_selections
      )[0]

      # select an integer based on the selected category
      if choice == option1:
          # ensure the selected integer is within the specified range and even
          selected_integer = random.randrange(2, maximum_integer + 1, 2)
          choice_result = random.choice(option1_statements)
          results = str(selected_integer) + ", " + choice_result
      else:
          # ensure the selected integer is within the specified range and odd
          selected_integer = random.randrange(1, maximum_integer + 1, 2)
          choice_result = random.choice(option2_statements)
          results = str(selected_integer) + ", " + choice_result

      return f"{APP_NAME}: {results}"
