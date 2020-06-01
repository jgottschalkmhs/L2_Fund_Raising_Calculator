import math
#  *** Functions go here ****

# Checks response is a valid number
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


# Displays instructions if program has not been used before
def instructions():
  
  first_time = yes_no("\nIt this your first time using the program? ")

  # instructions only display if user says it is their first time using the program
  if first_time == "no":
    return ""
  
  print()
  print("***** Instructions ******")
  print()
  print("This program will ask you for...")
  print("- The name of the product you are selling")
  print("- How many items you plan on selling")
  print("- The costs for each component of the product")
  print("- How much money you want to make")
  print()
  print("It will then output an itemised list of the costs with subtotals for the variable and fixed costs.")
  print("Finally it will tell you how much you should sell each item for to reach your profit goal.")
  print()


# rounding function
def round_up(amount, round_to):
    # rounds amount UP to the specified amount (round_to)
    return int(round_to * round(math.ceil(amount) / round_to))


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

    if len(all_costs) == 0:
      comp_question = "Component Name: "
    else:
      comp_question = "Component name (or 'xxx' to move on): "

    item_name = not_blank(comp_question) 

    if item_name.lower() == "xxx" and len(all_costs) == 0:
      print("You must have at least one item")
      continue

    if item_name.lower() != "xxx":
      item_cost = num_check(float, "What is the cost? $", 0)

    else:
      break

    # Add name and cost for each item to 'row' list
    costs_items.append(item_name)
    costs_items.append(item_cost)

    # Add each row to the master list
    all_costs.append(costs_items)

  return all_costs


def get_total(cost_list, num_items):
    # Iterate through list and add costs
  subtotal = 0
  for item in cost_list:
    subtotal += item[1]

  final_subtotal = subtotal * num_items

  return final_subtotal

# Prints 2D cost list and returns subtotal
def print_costs(heading, cost_list, subtotal):

  # Output goes here...
  print()
  print("***** {} *****".format(heading))

  for item in cost_list:
    print("{} - ${:.2f}".format(item[0], item[1]))

  print("\n{} Subtotal: ${:.2f}\n".format(heading, subtotal))
  
  return ""

# Calculates profit...
def profit_goal(total_costs):

  error = "Please enter a valid profit goal\n"
    
  valid = False
  while not valid:
    
    # ask for profit goal...
    response = input("What is your profit goal (eg $50 or 50%) ")

    # check if first character is $...
    if response[0] == "$":
      profit_type = "$"
      # Get amount (everything after the $)
      amount = response[1:]
    
    # check if last character is %
    elif response [-1] == "%":
      profit_type = "%"
      # Get amount (everything before the %)
      amount = response[:-1]

    else:
      # set response to amount for now
      profit_type = "unknown"
      amount = response

    try:
      # Check amount is a number more than zero...
      amount = float(amount)
      if amount <= 0:
        print(error)
        continue
    
    except ValueError:
      print(error)
      continue

    if profit_type == "unknown":
      find_type = yes_no("Do you mean ${:.2f}.  ie {:.2f} dollars? , y / n ".format(amount, amount))

      # Set profit type based on user answer above
      if find_type == "yes":
        profit_type = "$"
      else: profit_type = "%"

    if profit_type == "$":
      return amount
    else:
      goal = (amount / 100) * total_costs
      return goal


# ***** Main Routine goes here *****

# Title / Welcome
print("****** Welcome to the Fund Raising Calculator ******")

# Ask user if its their first time and if it is, display instructions
instructions()

print()

product_name = not_blank("What will you be making? ")   # check not blank
how_many = num_check(int,"How many items will you be making? ",0)  # check that this is an integer more than 1

# Get variable costs...
variable_costs = get_costs("Variable Costs")
variable_sub = get_total(variable_costs, how_many)

print()
have_fixed = yes_no("Do you have fixed costs? ")

# Get fixed costs...
if have_fixed != "no":
  fixed_costs = get_costs("Fixed Costs")
  fixed_sub = get_total(fixed_costs, 1)
else:
  fixed_costs = []
  fixed_sub = 0

# Work out total Cost
total_cost = variable_sub + fixed_sub

# Ask how much profit should be made
print()
profit_target = profit_goal(total_cost)

# work out sales needed and recommended price
sales_needed = total_cost + profit_target
price_unrounded = sales_needed / how_many
recommended_price = round_up(price_unrounded, 1)
print()

# Output...
print("**** Costs Schedule to make {} ******".format(product_name))

print_costs("Variable Costs", variable_costs, variable_sub)

if have_fixed != "no":
  print_costs("Fixed Costs", fixed_costs, fixed_sub)
else:
  print("\nYou have no fixed costs")

# Show Totals and price recommendation
print("Total Costs: ${:.2f}".format(total_cost))
print("Profit Target: ${:.2f}".format(profit_target))
print("Total Amount in Sales Needed: ${:.2f}".format(sales_needed))
print()
recommended_price = round_up(price_unrounded, 1)
print("Recommended Price: ${:.2f}".format(recommended_price))

