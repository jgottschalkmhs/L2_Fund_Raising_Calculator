#  *** Functions go here ****


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


# Checks a response to a question is not blank
def not_blank(question):

  valid = False
  while not valid:
    response = input(question)

    if response != "":
      return response
    else:
      print("Sorry, this can't be blank.\n")

# Checks answer to y / n question is yes / no
def yes_no(question):

  to_check = ["yes", "no"]
  
  valid = False
  while not valid:

    response = input(question).lower()

    for item in to_check:
      if response == item:
        return response
      elif response == item[0]:
        return item

    print("Please enter either yes or no...\n")

# Asks user for item and cost and returns 2D list
def get_costs(title):

  # Set up master list to hold all costs
  all_costs = []  
  print()
  print("Please enter the {}".format(title))

  valid = False
  while not valid:
    # List to contain each item (name, amount)
    costs_items = []
    item_name = not_blank("What is the item name? ") 

    if item_name.lower() != "xxx":
      item_cost = num_check(float, "What is the cost? ", 0)

    else:
      break

    # Add name and cost for each item to 'row' list
    costs_items.append(item_name)
    costs_items.append(item_cost)

    # Add each row to the master list
    all_costs.append(costs_items)

  return all_costs

# Prints 2D cost list and returns subtotal
def print_costs(heading, cost_list, num_items):
  # Iterate through list and add costs
  subtotal = 0
  for item in cost_list:
    subtotal += item[1]

  # Output goes here...
  print()
  print("***** {} *****".format(heading))

  for item in cost_list:
    print("{} - ${}".format(item[0], item[1]))

  print("\nTotal: ${:.2f}\n".format(subtotal * num_items))
  
  # Return sub total so that it can be used to find recommended price
  return subtotal

# ***** Main Routine goes here *****
product_name = not_blank("What will you be making? ")   # check not blank
how_many = num_check(int,"How many items will you be making? ",0)  # check that this is an integer more than 1

# Get variable costs...
variable_costs = get_costs("Variable Costs")

# Output costs
show_variable = print_costs("Variable Costs", variable_costs, how_many)


