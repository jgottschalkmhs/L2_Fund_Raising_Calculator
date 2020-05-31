# functions go here


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
      if amount < 0:
        print(error)
        continue
    
    except ValueError:
      print(error)
      continue

    if profit_type == "unknown":
      find_type = input("Do you mean ${:.2f}.  ie {:.2f} dollars? , y / n ".format(amount, amount))

      # Set profit type based on user answer above
      if find_type == "yes":
        profit_type = "$"
      else: profit_type = "%"

    if profit_type == "$":
      return amount
    else:
      goal = (amount / 100) * total_costs
      return goal

# Main  Routine goes here

total_costs = 200

profit_target = profit_goal(total_costs)
print()
print("Profit Targert: ${:.2f}".format(profit_target))