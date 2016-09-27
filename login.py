import fut
import time
import os
import config
import datetime
import pytz

#Connection to EA Servers
fut = None
delay = 5

while not fut:
 try:
  fut = config.connect()
 except:
  print "Failed connecting, retrying in %d.." % delay
  delay += 15
  time.sleep(delay)

print "Connected.."