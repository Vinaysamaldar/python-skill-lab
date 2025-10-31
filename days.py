#step 1= assin the days of week. 
#step 2= Enter the input number.
#step 3= If day is 1 to 7  print day of week.
#step 4= else day is greater than 7 print input is invalid.

days_of_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

day = int(input("Enter a number (1-7) for the day of the week: "))
if 1 <= day<= 7:
    print(f"Day {day} is {days_of_week[day- 1]}")
elif (day >7):
    print("Invalid input. There are 7 days in a week, Please enter a number between 1-7.")
else:
    print("Invalid input.enter an integer.")
