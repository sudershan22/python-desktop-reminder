import winsound
import getpass
import time as new_time
from datetime import datetime
from datetime import timedelta
from win10toast import ToastNotifier


def timer(remindername, reminder_time):

    notifier = ToastNotifier()
    notifier.show_toast("Reminder : " + remindername, f"""Set for {datetime.now() + timedelta(minutes=reminder_time)} Seconds.""", duration=5)

    new_time.sleep(reminder_time*60)

    winsound.Beep(2500, 1000)
    notifier.show_toast(f"Reminder", remindername,duration=20)


def wish():

    hours_now = datetime.now().hour
    name = getpass.getuser()
    if hours_now < 12 :
        print("Good Morining", name)

    elif hours_now in range(12,16):
        print("Good Afternoon", name)

    else:
        print("Good Evening", name)


if __name__=="__main__":
    wish()
    reminder_name = input("Reminder name : ")
    reminder_time=int(input("Enter time (in minutes) : "))
    timer(reminder_name, reminder_time)