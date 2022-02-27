import requests
import plyer
from plyer import notification
import time

def main():
    while True:
        notification.notify(
            title = "Hello Amazing people!",
            message = "Take a break! It has been an hour!",
            app_icon = "heart-icon_34407.ico",
            timeout = 10
        )
        time.sleep(10)
    

if __name__=='__main__':
    main()
