#Whatsapp automation app

#To Use Realtime automation for WhatsApp follow below steps.
"""1.Go to twilio.com & login.
    2.Then, for set-up in console.twilio.com tab under "Phone numbers",in 'Account Info'  save "Account SID & Account Token".
     3.Then, under "Messaging", in "Try it out" go for 'Send a WhatsApp message' and scan from your SmartPhone WhatsApp & send message "join blew-arrow".
      4.Last, Open this file and Run the program.
    """

#step-1 install required library
from twilio.rest import Client
from datetime import datetime, timedelta
import time

#step-2 twilio credentials
account_sid = "" #Follow above steps and paste which you save previous
auth_token = "" #Follow above steps and paste which you save previous

client = Client(account_sid, auth_token)

#step-3 define send message function
def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from = 'whatsapp:', #Number paste from above step-3.
            body = message_body
            to = f'whatsapp:{recipient_number}'
        )
        print(f'Message sent successfully! Message SID{message.sid}')
    except Exception as e:
        print('An error occured')

#step-4 user input
name = input('Enter the recipient name = ')
recipient_number = input('Enter the recipient WhatsApp number with country code (e.g, +1 234 567 8900) = ')
message_body = input(F'Enter the message you want to send to {name}: ')

#step-5 parse date/time and calculate delay
date_str = input('Enter the date to send the message (YYYY-MM-DD): ')
time_str = input('Enter the time to send the message (HH:MM in 24hour format): ')

#datetime
schedule_datetime = datetime.strptime(f'{date_str} {time_str}') #String pass time
current_datetime = datetime.now()

#calcluate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <= 0:
    print('The specified time is in the past. Please enter a future date and time: ')
else:
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

    #wait until the scheduled time
    time.sleep(delay_seconds) #1000

    #send the message
    send_whatsapp_message(recipient_number, message_body)

#Theorotical summary
'''
1- twilio client setup
2- user inputs
3- scheduling logic
4- send message
'''

