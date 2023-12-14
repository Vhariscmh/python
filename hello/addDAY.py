from datetime import datetime, timedelta, date

# Taking input as the current date using today() method
# today() method is supported by the date class in the datetime module
Begindatestring = date.today()

# Print the beginning date
print("Beginning date:")
print(Begindatestring)

# Calculating the end date by adding 10 days
Enddate = Begindatestring + timedelta(days=10)

# Print the ending date
print("Ending date:")
print(Enddate)
