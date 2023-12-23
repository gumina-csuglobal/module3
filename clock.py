
"""
This program calculates the hour an alarm will sound on a 24-hour clock. 

It asks the user for the time now (in hours)
Then asks for the number of hours to wait for the alarm.
Then outputs what the time will be on a 24-hour clock when the alarm goes off.
"""

def main():
    hours = int(input("What is the current time (in hours)?:"))
    wait_time = int(input("How long will you set the alarm for (in hours)?:"))

    alarm_hour = (hours+wait_time)%24

    print(f"\n\nGiven the current hour is {hours} and the alarm is set for {wait_time} hours from now,")
    print(f"The alarm will sound on hour {alarm_hour}.")

if __name__ == "__main__":
    main()