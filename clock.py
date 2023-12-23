
def main():
    hours = int(input("What is the current time (in hours)?:"))
    wait_time = int(input("How long will you set the alarm for (in hours)?:"))

    alarm_hour = (hours+wait_time)%24

    print(f"\n\nGiven the current hour is {hours} and the alarm is set for {wait_time} hours from now,")
    print(f"The alarm will sound on hour {alarm_hour}.")

if __name__ == "__main__":
    main()