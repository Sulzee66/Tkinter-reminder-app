from datetime import datetime
import json
import os
import time
from plyer import notification


def send_notification(mssg):
    notification.notify(
        title = 'Reminder',
        message = mssg,
        app_icon = None,
        timeout = 10,
    )


def count():
    with open("file.json", "r") as f:
        data = json.load(f)
    
    h = data["hour"]
    m = data["minute"]
    mssg = data["message"]
    alarm_time = h + ":" + m

    while True:
        os.system('cls')
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        parsed_time = current_time[:5]

        if parsed_time == alarm_time:
            send_notification(mssg)
            break
        else:
            print(current_time)
                
        time.sleep(1)

    

if __name__ == "__main__":
    count()