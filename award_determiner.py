# Request user to input their swimming, cycling and running time in minutes and store them in float variables.
swimming = float(input("Please enter your swimming time (in minutes): "))
cycling = float(input("Please enter your cycling time (in minutes): "))
running = float(input("Please enter your running time (in minutes): "))

# Calculate the total time taken by adding swimming, cycling and running.
total_time = swimming + cycling + running

# Check and print Provincial Colours award message if total time is within 100 minutes.
if total_time <= 100:
    print("Congratulations! You've been awarded Provincial Colours!")

# Check and print Provincial Half Colours award message if total time is within 105 minutes.
elif total_time <= 105:
    print("Congratulations! You've been awarded Provincial Half Colours!")

# Check and print Provincial Scroll award message if total time is within 110 minutes.
elif total_time <= 110:
    print("Congratulations! You've been awarded Provincial Scroll!")

# Otherwise print that the user has not received any award this time.
else:
    print("You have not received any award this time. Better luck next time!")
