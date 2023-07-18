import random as rng

def main():
    while True:
        Temperature = round(rng.uniform(20, 40), 1)
        Humidity = round(rng.uniform(0, 100), 1)
        EC_level = round(rng.uniform(0, 1), 0)
        pH_level = round(rng.uniform(0, 14), 0)
        light_level = round(rng.uniform(0, 1023), 0)
        print("Generating Data")

if __name__ == "__main__":
    main()