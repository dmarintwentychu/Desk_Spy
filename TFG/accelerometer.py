import pandas as pd
import time
import keyboard
from random import randint
from functions import truncate_float, sleep


df2 = pd.DataFrame(columns= ["Time", "Measures"])

while (not(keyboard.is_pressed("esc"))):
    df2.loc[len(df2)] = [truncate_float(time.time(),1), randint(0,4095)]
    sleep(0.1)

df2.to_csv("./Dataset/test.csv")