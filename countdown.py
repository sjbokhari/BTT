from datetime import datetime

def countdown_fix(stop):
    difference = stop - datetime.now()
    count_hours, rem = divmod(difference.seconds, 3600)
    count_minutes, count_seconds = divmod(rem, 60)
    if difference.days < 0:
        print("日本へようこそ")
    else:
        print(  str(difference.days) + "日" #"d"
            #+ str(count_hours) + "h"
            #+ str(count_minutes) + "m"
            #+ str(count_seconds) + "s"
            )

def main():
    end_time = datetime(2023, 7, 19, 17, 00, 0)
    countdown_fix(end_time)

if __name__ == '__main__':
    main()