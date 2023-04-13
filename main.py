import Time_Dilation_Calculations

print("\nHello! Welcome to an idea I had concerning time dilation!\n\n"
      "First, some truth. I am not an expert and have never studied physics or mathematics in depth. Therefore,\n"
      "these calculations could be completely off. However, I thought this would be a fun experiment to try to \n"
      "solve with programming and used it as an excuse to practice. I will attempt to explain my thought process\n"
      "for the viewer and also for myself when I undoubtedly return to this project.\n\n"
      "The original hypothesis was a question of whether or not there was some kind of 'sweet spot' with speed of\n"
      "travel relative to light speed. I believe I got the idea when I was fooling around with a time dilation\n"
      "calculator on the web. Anyway, here are some calculations I made in the order that I made them in. Enjoy.")
while True:
    print("\nWhich function do you want to run?\n"
          "1. Distance Traveled Chart\n"
          "2. Time Dilation Chart\n"
          "3. Sweet Spot Experiment Explanation\n"
          "4. Time Dilation Calculator\n"
          "5. Velocity Calculator\n"
          "6. Reach Calculator\n")
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
    elif answer == "6":
        Time_Dilation_Calculations.reach_calculator()
    else:
        print("ERROR. Please enter a number from 1-6.")
        continue
