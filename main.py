import os
import subprocess


#Ejecuci
comando_script1 = ["python", "keylogger.py"]

comando_script2 = ["python", "accelerometer.py"]

proceso_script1 = subprocess.Popen(comando_script1)

proceso_script2 = subprocess.Popen(comando_script2)


proceso_script1.wait()
proceso_script2.wait()


comando_script3 = ["python" ,"merger.py"]

proceso_script3 = subprocess.Popen(comando_script3)

proceso_script3.wait()

print("Todos los scripts han terminado.")
