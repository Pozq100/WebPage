import random as rng
import time

def main(state):
    print(state)
    if state == 1:
        Temperature = round(rng.uniform(20, 40), 1)
        Humidity = round(rng.uniform(0, 100), 1)
        EC_level = round(rng.uniform(0, 1), 0)
        pH_level = round(rng.uniform(0, 14), 0)
        light_level = round(rng.uniform(0, 1023), 0)
        print(Temperature,Humidity,EC_level,pH_level,light_level)

    return

if __name__ == "__main__":
    main(1)