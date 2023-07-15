import random as rng
import csv
def DataGeneration():
    Temperature = round(rng.uniform(20, 40), 1)
    Humidity = round(rng.uniform(0, 100), 1)
    EC_level = round(rng.uniform(0, 1), 0)
    pH_level = round(rng.uniform(0, 14), 0)
    light_level = round(rng.uniform(0, 1023), 0)
    WriteData([Temperature,Humidity,EC_level,pH_level,light_level])
    return [Temperature,Humidity,EC_level,pH_level,light_level]

def WriteData(Datas):
    with open(csvfile, 'a', newline="") as Data:
        writer = csv.writer(Data)
        writer.writerow(Datas)
    return
def ReadData(index):
    # Temperature: 1, Humidity: 2, EC_level: 3, pH_level: 4, light_level:5
    datatype = {
        1: "Temperature",
        2: "Humidity",
        3: "EC_level",
        4: "pH_level",
        5: "light_level"
    }
    temp = pd.read_csv(csvfile, usecols=[datatype[index]])
    return temp
def ReadLine(csvfile,line):
    data = []
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(line - 1):
            next(reader)
        for i in next(reader):
            data.append(float(i))
    return data
