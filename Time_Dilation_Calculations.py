import matplotlib.pyplot as plt
import math
# TODO consider moving calculations away from strings for readability? idk
# PLAN A:
# set mission parameters and find best speed

# PLAN B:
# travel distance difference calculator

# PLAN 1:
# Find best speed(s) given a RELATIVE TIME and DISTANCE
# Calculate distance traveled in steps of 0.1 and find the greatest give a relative time
# 5lys away in 20 years relative time


lightyearmps = 186282  # miles per second at light speed
seconds_in_year = 31536000  # in a normal year
miles_per_year = 5287130236800.001  # at light speed


# DISTANCE TRAVELED CHART
def distance_traveled_chart():
    print("\nHere I made a simple chart showing the relation between a speed as a percentage of a light year compared\n"
          "to the amount of miles per second at that speed. This isn't the curved graph I expected at the time.\n")
    speed = [perc / 10 for perc in range(11)]  # .1 intervals relative to a lightyear
    miles = [(perc / 10) * lightyearmps for perc in range(11)]  # miles per speed interval

    plt.plot(miles, speed, marker="o")
    plt.title("Miles Per Second At Percentage Of A Lightyear")
    plt.xlabel("Miles Per Second")
    plt.ylabel("Percentage of Lightyear")
    plt.yticks(ticks=speed)
    return plt.show()


# TIME DILATION CHART
def time_dilation_chart():
    print("Unsatisfied with the previous chart, I looked up the time dilation equation and figured out how to code\n"
          "it in. The equation solves for RELATIVE time. If you don't know what that is, basically, if a crew is \n"
          "traveling near lightspeed for a year through space, then relative time, or the time that passed on earth,\n"
          "would be 2.3 years. This chart is what I expected from my first program and shows exactly what I described.")
    speed = [perc / 10 for perc in range(10) if perc != 0]  # cant divide by 0
    years_time = [1 / math.sqrt(1 - perc ** 2 / 1 ** 2) for perc in speed]  # calculate for relative time

    plt.plot(speed, years_time, marker="o")
    plt.title("Time Dilation Relative to Velocity")
    plt.xlabel("velocity as percentage of a lightyear".title())
    plt.ylabel("years traveled".title())
    return plt.show()


# SWEET SPOT EXPERIMENT - HYPOTHESIS TRUE.. TODO NEEDS TO READ EASIER FOR CLARITY
def sweet_spot_experiment():
    print("\nHere is where I realized that my hypothesis was true. Simply based on the fact that traveling at 50%\n"
          "lightspeed for 2 years and 90% for 1 year both produce the same relative time of ~2.3 years.\n")
    # The idea is that traveling at 50% for two years and 90% for one year both produce 2.3 years relative time, however
    # 50% for two years produces more distance traveled
    print("Relative time traveling for two years @ 50% light speed: ", str(2 / math.sqrt(1 - 0.5 ** 2 / 1 ** 2)))
    print("Relative time traveling for one year @ 90% light speed:  ", str(1 / math.sqrt(1 - 0.9 ** 2 / 1 ** 2)))
    input("\nPress enter to continue.\n")
    print("\nAs you can see its not exact but its pretty close.\n"
          "Therefore, I can compare the distance covered by these two instances:\n")
    print("Distance traveled in two years @ 50% speed of light:", str((miles_per_year * 0.5) * 2).rjust(21), "miles")
    print("Distance traveled in one year @ 90% speed of light:", str(miles_per_year * 0.900535).rjust(22), "miles")
    print("Difference:", str(miles_per_year - miles_per_year * 0.900535).rjust(63), "miles")
    difference = miles_per_year - miles_per_year * 0.900535  # 50% + 50% = 1 light year, so I could use it as a bar
    base = miles_per_year * 0.900535  # trying to make math easier
    print("Percent further:", int(difference * 100 / base))  # using the difference I could calculate percent farther
    print("\nThere you have it! I have proven that during the same 2.3 years on Earth, the crew that traveled\n"
          "for two years at 50% light speed actually traveled 11% farther than the crew that went faster for 1 year!")
    input("\nPress enter to return to menu.\n")
    return


# TIME DILATION CALCULATOR W/ DISTANCE
def time_dilation_calculator():  # TODO define rules, break loop
    print("\nAfter messing with the formula manually in the previous module, I wanted to find out what exactly is the\n"
          "optimal speed to travel. Also, I realized it would be useful to have travel distance calculated for me.\n"
          "This is what I came up with. It helped me confirm what I would later turn into a graph. It could also\n"
          "be useful in a real life situation if you needed to calculate relative time and distance with a given\n"
          "crew travel time and speed.\n")
    while True:
        time = input("Enter crew travel time in years: ")
        velocity = input("Enter velocity as a decimal of a light year (example: 0.9): ")
        try:
            time = float(time)  # testing users input
            velocity = float(velocity)
        except ValueError:  # wrong input
            input("ERROR. Please enter numbers only. Press enter to try again.")
            continue  # try again
        if velocity < 1:  # formula will only work with value less than 1
            relative_time = time / math.sqrt(1 - velocity ** 2 / 1 ** 2)  # relative (Earth) time calculation
            print(f"\nRelative time: {relative_time} years")
            print(f"Distance traveled: {(time * miles_per_year) * velocity} miles")  # simple distance calculation
            while True:
                answer = input("\nEnter 'y' to try again. Otherwise, enter 'n' to get back to the menu.\n")
                if answer == "y":
                    break  # that was fun! try again
                elif answer == "n":
                    return  # that was boring. go back to menu
                else:
                    print("Invalid input.")
        else:  # simplest solution - formula won't work correctly
            input("ERROR. Please enter a velocity less than 1. Press enter to try again.")
            continue


# VELOCITY CALCULATOR
def velocity_calculator():
    # Keeping desired relative time constant but changing crew time will produce desired effect
    print("\nThis turned out to be the prototype for the calculation that I would finally use to graph my theory.\n"
          "Honestly for that, it is kind of redundant. All it does is calculate for speed instead of relative time.\n"
          "Which, does actually end up being important. It could also be used in a real life situation if you wanted\n"
          "to figure out how fast you needed to go if you needed to define crew travel time and relative time based\n"
          "on supplies, or maybe lifespans.\n"
          "\nThis calculator has two rules:\n"
          "1. You must enter a NUMBER greater than 0.\n"
          "2. Crew travel time can not be larger than desired relative time.\n")
    while True:
        time = input("Enter desired crew travel time in years: ")
        relative_time = input("Enter desired relative time in years: ")
        try:
            time = float(time)  # test if user entered correctly
            relative_time = float(relative_time)
        except ValueError:  # if not throw error
            print("ERROR. Please enter numbers only.")
            continue  # try again
        if time > relative_time:  # cause math doesn't work this way
            input("ERROR. Crew time can not be larger than desired relative time. Press enter to try again.")
            continue  # try again
        if time == 0:  # cannot divide by 0
            input("ERROR. Time must be greater than zero. Press enter to try again")
            continue  # try again
        t = math.sqrt(1 - ((1 / (relative_time / time)) ** 2))  # square rt fn - calculates for SPEED
        print(f"Speed relative to light year: {t}")
        while True:
            answer = input("\nEnter 'y' to try again. Otherwise, enter 'n' to get back to the menu.\n")
            if answer == "y":
                break  # that was fun! try again
            elif answer == "n":
                return  # that was boring. go back to menu
            else:
                print("Invalid input.")
        break
    return


# REACH CALCULATOR
def reach_calculator():
    print("\nWe have arrived! The Magnum Opus of this coding adventure. This graph not only confirms my original\n"
          "hypothesis, but it also shows us what the optimal travel speed is with relative time in mind. The simplest\n"
          "way I can explain it is this: Let's say we're going to have a 10 year long space race to see who travels\n"
          "the farthest.\n"
          "\nOne would think, the faster you go, the farther you'll get.. Not true. This pretend race is based on\n"
          "a 10 year Earth time limit, and if you go too fast, time dilation actually works against you! Go on!\n"
          "Enter 10 years into the the program and see for yourself!"
          "\n\nATTN: This calculator works best when using a number that is greater than or equal to 6.\n\n"
          "The calculator will calculate crew speed for every year up to the amount of years you enter.\n"
          "Therefore, optimal space travel speed will be more accurate with a higher number of years entered.\n"
          "For example: 10 years relative time entered. The calculator solves for 9 years crew time, then 8 years\n"
          "crew time, then 7, and so on. This records a speed and a distance every iteration. The largest distance\n"
          "covered is then pulled from all of the calculations. Finally, all of the calculations are graphed.\n")
    while True:
        d_storage = []  # master list of distances and speeds for each crew interval
        relative_time = input("Enter desired relative time (Earth time) in years: ")
        crew_interval = int(relative_time)  # copies input to start a countdown interval  TODO can go after value check?

        while crew_interval > 0:  # calculate for each year up to however many years were entered
            crew_interval -= 1  # TODO this block for value check - separate check from countdown?
            try:
                crew_interval = float(crew_interval)
                relative_time = float(relative_time)
            except ValueError:
                print("ERROR. Please enter numbers only.")
                break
            if crew_interval == 0:
                break
            speed = math.sqrt(1 - ((1 / (relative_time / crew_interval)) ** 2))  # square root fn
            d = (speed * miles_per_year) * crew_interval  # distance calculation
            d_storage.append((d, speed))

        sorted_d = sorted(d_storage)
        largest = sorted_d[-1][0], sorted_d[-1][1]  # sorted list instead of iterating - saves memory and time I think
        for entry in d_storage:  # pulls the largest distance in the list
            if float(entry[0]) > float(largest[0]):
                largest = entry
        distances = []
        speeds = []
        for entry in d_storage:
            distances.append(entry[0])
            speeds.append(entry[1])
        plt.plot(speeds, distances)
        plt.title(f"affect of speed on Distance over {int(relative_time)} years relative time".title())
        plt.xlabel("Speed as a Percentage of a Lightyear".title())
        plt.ylabel("Distance in Miles".title())
        # plt.yticks(ticks=distances)
        print(f"\nLargest distance in miles: {largest[0]}\n"
              f"Percentage of lightyear at which distance was achieved: {largest[1]}")
        plt.show()
        while True:
            answer = input("\nEnter 'y' to try again. Otherwise, enter 'n' to see the conclusion.\n")
            if answer == "y":
                break  # that was fun! try again
            elif answer == "n":
                print("\nCONCLUSION:\n"
                      "\nAccording to this calculator, ~70.71% lightspeed is the optimal speed for distance\n"
                      "given a relative time!")
                quit()
            else:
                print("Invalid input.")





# EXPERIMENTAL REACH CALCULATIONS BASED ON 10 YEARS EARTH TIME -- CREW TIME/RELATIVE TIME
# 9/10 20741459763194.54
# 8/10 25378225136640.0
# 7/10 26430363524944.41  <- ~5 times farther than 1/10
# 6/10 25378225136640.008
# 5/10 22893945490928.18
# 4/10 19382939615380.64
# 3/10 15130802387641.14
# 2/10 10360617027040.318
# 1/10  5260628163962.55
