import matplotlib.pyplot as plt
import math

# PLAN A:
# set mission parameters and find best speed

# PLAN B:
# travel distance difference calculator

# is there a sweet spot in travel speed?
# x = miles  y = speed in percentage of ly

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
    print("Distance traveled in one year @ 100% speed of light:", str(miles_per_year).rjust(21), "miles")
    print("Distance traveled in one year @ 90% speed of light:", str(miles_per_year * 0.900535).rjust(22), "miles")
    # above percentage is calculated for 2.3 relative time exactly
    print("Distance traveled in one year @ half the speed of light:", miles_per_year * 0.5, "miles")
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
            print(f"Distance traveled: {miles_per_year * velocity} miles")
            input("Press enter to try again.")
            continue
        else:
            input("ERROR. Please enter a velocity less than 1. Press enter to try again.")
            continue


# VELOCITY CALCULATOR
def velocity_calculator():
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
        t = math.sqrt(1 - ((1 / (relative_time / time)) ** 2))  # innermost parenthesis happen first
        print(t)
        break
    return
