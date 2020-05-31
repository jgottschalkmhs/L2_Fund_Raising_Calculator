# Functions go here
def num_check(type, question, lowest):

  # Set up error message so that it specifies either 'an integer' or 'a number' depending on the 'type'.
  if type == int:
    error_specific = "an integer"
  else:
    error_specific = "a number"

  error = "Please enter {} that is more than {} \n".format(error_specific, lowest)

  valid = False
  while not valid:

    # Ask the question and check that the answer is valid
    try:
      response = type(input(question))

      if response > lowest:
        return response
      else:
        print(error)

    except ValueError:
      print(error)

# **** Main Routine Goes Here

# Ask for number of items
num_items = num_check(int, "How many items will you be making? ", 0)

# Ask for cost
expense = num_check(float, "$", 0)

print("you are making {} items at at cost of ${:.2f}".format(num_items, expense))