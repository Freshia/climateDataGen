import random
import math

def humidity_data():
    relative_humidity = random.randrange(55.0,77.0)
    dew_point = (100 - relative_humidity)/5
    temperature = random.randrange(15.0,42.0)
    humidity = 100.00 * ((611 * math.exp(5423 * ((1 / 273)) - (1 / (dew_point + 273)))) / (611 * math.exp(5423 * ((1 / 273)-(1 / temperature))))) 
    return humidity

def wind_speed_data():
    longitude = random.randrange(98.0,102.0)
    wind_speed = 0.0001 * longitude
    return wind_speed

def pressure_data():
    temperature = random.randrange(15.0,42.0)
    #Confirm if me nt to be 10??
    pressure = 101325 * math.exp(((0.00 - 9.81) * 0.0289644 * (200))/(8.31444598 * (temperature + 273)))
    return pressure