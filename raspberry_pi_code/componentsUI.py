from grovepi import *
import time

from grovepi import *
from grove_rgb_lcd import *

import os
import subprocess
import time

dir_path = './data_history_pooling/treHistory255/'
prev_hits_count = str(len(os.listdir(dir_path)))
while True:
    result = subprocess.run(['/usr/bin/vcgencmd',  'measure_temp'], stdout=subprocess.PIPE)
    actual_hits_count = str(len(os.listdir(dir_path)))
    if prev_hits_count < actual_hits_count:
        digitalWrite(2,1)
        time.sleep(0.1)
        digitalWrite(2,0)
        prev_hits_count = actual_hits_count
    hits_count = 'Hits count: ' + str(actual_hits_count) + '\n' + result.stdout.decode('utf-8')
    setText(hits_count + '\n' + 'temperature')
    #setRGB(0,0,0)
    time.sleep(5) #sleep 5 seconds
    
    button_status = digitalRead(3)
    if button_status:
        setRGB(0,255,0)
    else:
        setRGB(0,0,0)