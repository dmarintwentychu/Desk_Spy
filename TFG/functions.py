import time


#Trunca los decimales de un valor float
#Utilizo esta función porque al redondear se pueden ir algunos números
def truncate_float(float_number, decimal_places):
    multiplier = 10 ** decimal_places
    return int(float_number * multiplier) / multiplier

#Función sleep más precisa que la de time.sleep()
def sleep(duration, get_now=time.perf_counter):
    now = get_now()
    end = now + duration
    while now < end:
        now = get_now()