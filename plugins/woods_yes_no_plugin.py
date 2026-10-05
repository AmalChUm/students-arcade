import random

AUTHOR = "Moesha Woods"
APP_NAME = "Decision Helper"
def run():
      # each option probablity can me adjusted as needed
      yes_probablity= 70
      no_probablity=30

      #set string values to yes/no for better readability & easier modification
      option1="yes"
      option2="no"
      
      # helper variable for random selection count
      number_choices_selections = 1
      # different statements after yes/no probability response 
      option1_statements=[
          "you should do it.",
          "that's a good idea.",
          "go for it!",
          "I think that's a great choice."
      ]
      
      option2_statements=[
          "you probably shouldn't do it.",
          "that's not a good idea.",
          "I think that's a risky choice.", 
          "dont do it."
      ]
      # randomly select yes or no based on probability
      choice = random.choices(
          [option1, option2],
          weights=[yes_probablity, no_probablity],
          k=number_choices_selections
      )[0]

      if choice == option1:
          choice_result = random.choice(option1_statements)
          results = option1 + ", " + choice_result
      else:
          choice_result = random.choice(option2_statements)
          results = option2 + ", " + choice_result

      return f"{APP_NAME}: {results}"