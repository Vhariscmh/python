import datetime

# Get the current date and time
a = datetime.datetime.today()

# Get the current date and time with more precision (includes microseconds)
b = datetime.datetime.now()

# Print the current date and time obtained using today()
print("Today's date and time:", a)

# Print the current date and time obtained using now()
print("Current date and time with microseconds:", b)
