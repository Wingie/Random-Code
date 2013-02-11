import twitter
from datetime import datetime
api = twitter.Api(consumer_key='VL40pD0CVJPomvY34GVI8g',
                           consumer_secret='bgdzloc0UNevZMTEQRN7m9ckrstosa3JJxgpuxEVYU4',
                            access_token_key='21511099-o63mMV4HUkKcaFMlkOYJKlHi8Z05ChBjrI0YV9HA',
                            access_token_secret='rQ5wIvEhBniLcNTm3bwo2Tj4tUJAdnHWYLsPr2d8m0')
import serial
ser = serial.Serial('/dev/ttyUSB1', 9600)
i = ser.readline()[:-2]
temp =  "Arduino Logged temp at " + datetime.now().strftime("%Y-%m-%d %H:%M:%S") + " is " + i + "*C" 
print temp
friends=api.PostUpdate(temp)
