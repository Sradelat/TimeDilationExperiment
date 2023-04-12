import matplotlib.pyplot as plt
import math

# PLAN A:
# set mission parameters and find best speed

# PLAN B:
# travel distance difference calculator

# PLAN 1:
# Find best speed(s) given a RELATIVE TIME and DISTANCE
# Calculate distance traveled in steps of 0.1 and find the greatest give a relative time
# 5lys away in 20 years relative time


lightyearmps = 186282  # miles per second
seconds_in_year = 31536000  # in a year
miles_per_year = 5287130236800.001  # at light speed

# DISTANCE TRAVELED CHART
def distance_traveled_chart():
    speed = [perc / 10 for perc in range(11)]  # .1 intervals relative to a lightyear
    # print(speed)
    # miles = [lightyearmps * perc for perc in speed]  # miles per interval -- UNUSED?
    # print(miles)
    miles = [(perc / 10) * lightyearmps for perc in range(11)]  # miles per speed interval
    # print(miles)

    plt.plot(miles, speed, marker="o")
    plt.title("Miles Per Second At Percentage Of A Lightyear")
    plt.xlabel("Miles Per Second")
    plt.ylabel("Percentage of Lightyear")
    plt.yticks(ticks=speed)
    return plt.show()


# TIME DILATION CHART
def time_dilation_chart():
    speed = [perc / 10 for perc in range(10) if perc != 0]  # cant divide by 0
    years_time = [1 / math.sqrt(1 - perc ** 2 / 1 ** 2) for perc in speed]
    plt.plot(speed, years_time, marker="o")
    plt.title("Time Dilation Relative to Velocity")
    plt.xlabel("velocity as percentage of a lightyear".title())
    plt.ylabel("years traveled".title())
    # Half light speed time diff 1.15 years half distance traveled
    return plt.show()


# SWEET SPOT EXPERIMENT - HYPOTHESIS TRUE.. TODO NEEDS TO READ EASIER FOR CLARITY
def sweet_spot_experiment():
    # The idea is that traveling at 50% for two years and 90% for one year both produce 2.3 years relative time, however
    # 50% for two years produces more distance traveled
    print("Distance traveled in two years @ 50% speed of light:", str((miles_per_year * 0.5) * 2).rjust(21), "miles")
    print("Distance traveled in one year @ 90% speed of light:", str(miles_per_year * 0.900535).rjust(22), "miles")
    # above percentage (0.900535) is calculated for 2.3 relative time exactly
    # print("Distance traveled in one year @ half the speed of light:", miles_per_year * 0.5, "miles")
    # if traveler travels for two years @ half light speed then relative time is 2.3 years
    # if traveler travels for one year @ 90% light speed then relative time is also 2.3 years
    print("Difference:", str(miles_per_year - miles_per_year * 0.900535).rjust(63), "miles")
    difference = miles_per_year - miles_per_year * 0.900535
    base = miles_per_year * 0.900535
    print("Percent further:", difference * 100 / base)
    # ~11% further going slower! (the half speed number isn't exact)
    return


# TIME DILATION CALCULATOR W/ DISTANCE
def time_dilation_calculator():  # TODO define rules, break loop
    while True:
        time = input("Enter crew travel time in years: ")  # years
        velocity = input("Enter velocity as a fraction of light years: ")  # light years
        try:
            time = float(time)
            velocity = float(velocity)
        except ValueError:
            input("ERROR. Please enter numbers only. Press enter to try again.")
            continue
        if velocity < 1:
            relative_time = time / math.sqrt(1 - velocity ** 2 / 1 ** 2)
            print("Relative time:", relative_time)
            print(f"Distance traveled: {(time * miles_per_year) * velocity} miles")
            input("Press enter to try again.")
            continue
        else:
            input("ERROR. Please enter a velocity less than 1. Press enter to try again.")
            continue


# VELOCITY CALCULATOR
def velocity_calculator():
    # Keeping desired relative time constant but changing crew time will produce desired effect
    print("This calculator has two rules:\n"
          "1. You must enter a NUMBER greater than 0.\n"
          "2. Crew travel time can not be larger than desired relative time.\n")
    while True:
        time = input("Enter crew travel time in years: ")  # years
        relative_time = input("Enter desired relative time: ")
        try:
            time = float(time)
            relative_time = float(relative_time)
        except ValueError:
            print("ERROR. Please enter numbers only.")
            continue
        if time > relative_time:
            input("ERROR. Crew time can not be larger than desired relative time. Press enter to try again.")
            continue
        if time == 0:
            input("ERROR. Time must be greater than zero. Press enter to try again")
            continue
        t = math.sqrt(1 - ((1 / (relative_time / time)) ** 2))  # innermost parenthesis happen first. square root fn
        print(f"Speed relative to light year: {t}")
        break
    return


# REACH CALCULATOR
def reach_calculator():
    print("\nATTN: This calculator works best when using a number that is greater than or equal to 6. "
          "No decimals yet please :)\n")
    d_storage = []
    relative_time = input("Enter desired relative time: ")
    interval = int(relative_time)
    while interval > 0:
        interval -= 1
        try:
            interval = float(interval)
            relative_time = float(relative_time)
        except ValueError:
            print("ERROR. Please enter numbers only.")
            break
        if interval == 0:
            print("\nCalculation Complete.\n")
            # print(d_storage)
            break
        speed = math.sqrt(1 - ((1 / (relative_time / interval)) ** 2))  # innermost parenthesis happen first. square root fn
        d = (speed * miles_per_year) * interval  # distance calculation
        d_storage.append((d, speed))
        print(f"\nSpeed relative to light year: {speed}\n"
              f"Distance traveled in {int(relative_time)} earth years: {d} miles")
    largest = 0, 0
    for entry in d_storage:
        if float(entry[0]) > float(largest[0]):
            largest = entry
    distances = []
    speeds = []
    for entry in d_storage:
        distances.append(entry[0])
        speeds.append(entry[1])
    print(distances)
    print(speeds)
    plt.plot(speeds, distances)
    plt.title(f"affect of speed on Distance over {int(relative_time)} years relative time".title())
    plt.xlabel("Speed as a Percentage of a Lightyear".title())
    plt.ylabel("Distance in Miles".title())
    # plt.yticks(ticks=distances)
    print(f"\nLargest distance, speed: {largest}")
    return plt.show()
    # according to this calculator ~70.71% lightspeed is optimal speed for distance given a relative time




# EXPERIMENTAL REACH CALCULATIONS BASED ON 10 YEARS EARTH TIME -- CREW TIME/RELATIVE TIME
# 9/10 20741459763194.54
# 8/10 25378225136640.0
# 7/10 26430363524944.41  <- 5 times farther than 1/10
# 6/10 25378225136640.008
# 5/10 22893945490928.18
# 4/10 19382939615380.64
# 3/10 15130802387641.14
# 2/10 10360617027040.318
# 1/10  5260628163962.55
