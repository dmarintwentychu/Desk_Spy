from pynput import keyboard
import time
import pandas as pd
from functions import truncate_float

# Inicialización del Dataframe:
df = pd.DataFrame(columns= ["Time", "KeyPressed"])

# Función para detectar cuando se ha pulsado (No detecta cuando se mantiene pulsado)
def on_press(key):
    global df

    newRow = {"Time" : truncate_float(time.time(),1) , "KeyPressed" : key}
    df = pd.concat([df, pd.DataFrame([newRow])], ignore_index=True)

#Funcion para detectar cuando se ha soltado la tecla
def on_release(key):
    global df, lastPulse

    if key == keyboard.Key.esc:
        # Parar al Listener
        return False
  

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:  
        listener.join()


df.to_csv('./Dataset/keylog.csv')
