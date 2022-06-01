import Time_Dilation_Calculations

print("Which function do you want to run?\n"
      "1. Distance Traveled Chart\n"
      "2. Time Dilation Chart\n"
      "3. Sweet Spot Experiment\n"
      "4. Time Dilation Calculator\n"
      "5. Velocity Calculator\n")
while True:
    answer = input(">")
    if answer == "1":
        Time_Dilation_Calculations.distance_traveled_chart()
    elif answer == "2":
        Time_Dilation_Calculations.time_dilation_chart()
    elif answer == "3":
        Time_Dilation_Calculations.sweet_spot_experiment()
    elif answer == "4":
        Time_Dilation_Calculations.time_dilation_calculator()
    elif answer == "5":
        Time_Dilation_Calculations.velocity_calculator()
    else:
        print("ERROR. Please enter a number 1-5.")
        continue
