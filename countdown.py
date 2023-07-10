from datetime import datetime

def countdown_fix(stop: datetime) -> None:
    difference = stop - datetime.now()
    count_hours, rem = divmod(difference.seconds, 3600)
    #count_minutes, count_seconds = divmod(rem, 60)
    if difference.days < 0:
        print("Vacation")
    else:
        print(  str(difference.days) + "d"
            + str(count_hours) + "h"
            #+ str(count_minutes) + "m"
            #+ str(count_seconds) + "s"
            )

def main() -> None:
    end_time = datetime(2023, 7, 20, 15, 00, 0)
    countdown_fix(end_time)

if __name__ == '__main__':
    main()