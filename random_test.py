import random as rng
from time import sleep
from random import random

for i in range(10):
    Temperature = round(rng.uniform(20, 40), 1)
    Humidity = round(rng.uniform(0, 100), 1)
    EC_level = round(rng.uniform(0, 1), 0)
    pH_level = round(rng.uniform(0, 14), 0)
    light_level = round(rng.uniform(0, 1023), 0)

    temp = random() * 100
    Humi = random() * 55

    print(Temperature)
    print(Humidity)
    print(EC_level)
    print(pH_level)
    print(light_level)
    #print(temp)
    #print(Humi)
    print("-----break-----")
    sleep(2)