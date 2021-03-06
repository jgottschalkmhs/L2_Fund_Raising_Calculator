#  *** Functions go here ****

def get_costs(title):

  # Set up master list to hold all costs
  all_costs = []  
  print()
  print("Please enter the {}".format(title))

  valid = False
  while not valid:
    # List to contain each item (name, amount)
    costs_items = []
    item_name = input("What is the item name? ")  # replace with call to not blank function

    if item_name.lower() != "xxx":
      item_cost = float(input("What is the cost? "))  # replace with call to number checking function

    else:
      break

    # Add name and cost for each item to 'row' list
    costs_items.append(item_name)
    costs_items.append(item_cost)

    # Add each row to the master list
    all_costs.append(costs_items)

  return all_costs

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
product_name = input("What will you be making? ")   # check not blank
how_many = int(input("How many items will you be making? "))  # check that this is an integer more than 1

# Get variable costs...
variable_costs = get_costs("Variable Costs")

# Output costs
show_variable = print_costs("Variable Costs", variable_costs, how_many)

