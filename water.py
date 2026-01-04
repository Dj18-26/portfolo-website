import time
import pyttsx3
from plyer import notification
time_hour = float(input("Set the hour you should want to drink water at this time :"))
while(True):
    engine = pyttsx3.init()
    time.sleep(3600 * time_hour)
    for i in range(3):
        engine.say("Hey Dhiraj Please Drink Your Water Immediately" )
        
    
    
    notification.notify(title = "Water Drink Reminder", message = "Hello Dhiraj, this is your drinking time" , timeout = 2)
    engine.runAndWait()

                        


