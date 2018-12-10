
import RPi.GPIO as GPIO # Used to interact with GPIO pins
import time # Used for sleep and to timestamp the email
from email.mime.text import MIMEText # Used to compose email
import smtplib # Used to send email
# Create a function to run when pin state changes 
# When this function is called, all it does is send an email
# based on the state of the pin
def send_alert(channel):
# Set variables
  gmail_user = 'pythoncmru@gmail.com'
  gmail_pass = 'pythoncmru@123'
  sent_from = gmail_user
  send_to = 'firestation809@gmail.com, firestation970@gmail.com'
  # Create Timestamp
  timestamp = time.strftime("%m-%d-%y %H:%M:%S")
# if statement to determine which email msg to send
# If the pin is low then the alarm is sounding
# Boolean vale of pin when high is true, low is false
if GPIO.input(12):
  subject = 'Smoke Detector Stopped ' + timestamp
  body = 'Sorry to interrupt you again, but your smoke detector has stopped sounding. It is possible that there is no fire, but it is also possible that the fire has shorted out part or all of your elecrical system. Thank you for your time. \n\n   Sincerly,\n Pi-Server'
else:
  subject = 'Your House May be on Fire ' + timestamp
  body = 'Sorry to interrupt you, but it seems that your smoke detector is sounding. It is possible that your house is on fire. Thank you for your time. \n\n   Sincerly,\n Pi-Server'
  # Compose the email
  msg = MIMEText(body)
  msg['From'] = sent_from
  msg['To'] = send_to
  msg['Subject'] = subject
  # Send the email
  try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(gmail_user, gmail_pass)
    server.sendmail(sent_from, send_to, msg.as_string())
    server.close()

    if GPIO.input(12):
      print 'All-clear email sent!'
    else:
      print 'Alert email sent!'
    except:
      print 'Something went wrong sending email...'
      # Beginning of Program
      GPIO.setmode(GPIO.BCM) # Set's GPIO pins to BCM GPIO numbering
      INPUT_PIN = 12 # Set's the variable representing the input pin to 12
      GPIO.setup(INPUT_PIN, GPIO.IN) # Sets the input pin to be an input
      # Wait for the input to change states, run the function send_alert when it does
      GPIO.add_event_detect(INPUT_PIN, GPIO.BOTH, callback=send_alert, bouncetime=2000)
      # Endless loop to keep the program running
      var = 1
      while var == 1:
        print 'smoke detector is being monitored'
        time.sleep(60) 
  
 '''  #alaram added
   import datetime
import os
import time

now = datetime.datetime.now()

# Choose 6PM today as the time the alarm fires.
# This won't work well if it's after 6PM, though.
alarm_time = datetime.datetime.combine(now.date(), datetime.time(18, 0, 0))

# Think of time.sleep() as having the operating system set an alarm for you,
# and waking you up when the alarm fires.
time.sleep((alarm_time - now).total_seconds())

os.system("start BTS_House_Of_Cards.mp3")

'''