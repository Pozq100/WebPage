import random as rng
import csv
import time
import datetime
csvfile = "Alldatas.csv"
folder_id = "1ztWIVXy_3z2zNlTQaRnAoLNic0QcYZHR"

def DataGeneration(Temperature, Humidity, EC_level, pH_level, light_level):
    Time = (time.time() + 28800000) * 1000
    WriteData([Time,Temperature,Humidity,EC_level,pH_level,light_level])
    return [Time,Temperature,Humidity,EC_level,pH_level,light_level]

def WriteData(Datas):
    if Datas[3]:
        Datas[3] = 1.0
    else:
        Datas[3] = 0.0
    with open(csvfile, 'a', newline="") as Data:
        print(Datas)
        writer = csv.writer(Data)
        writer.writerow(Datas)
    return
def ReadLine(csvfile,line):
    data = []
    with open(csvfile, "r") as csvfile:
        reader = csv.reader(csvfile)
        for _ in range(line - 1):
            next(reader)
        for i in next(reader):
            data.append(float(i))
    return data

def LatestLine(csvfile):
    totallines = 0
    with open(csvfile,"r") as file:
        reader = csv.reader(file)
        totallines = sum(1 for row in reader)
    print(totallines)
    if totallines > 20:
        line = totallines - 20
    else:
        line = 3
    return line