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

# Loops to make testing faster...
for item in range(0,5):
  love_cs = yes_no("Do you like CS? ")
  print("You said '{}'\n".format(love_cs))