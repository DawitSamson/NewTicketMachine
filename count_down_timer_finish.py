# to make timer we need to import and install time library
import time


# define the countdown function
def countdown_finish():
    time_sec = 3
    while time_sec > 0:
        minutes, secs = divmod(time_sec, 60)
        hour, minutes = divmod(minutes, 60)
        timeleft = str(hour).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(secs).zfill(2)
        print(timeleft + "\r", end='')
        time.sleep(1)
        time_sec -= 1
        print(timeleft)

