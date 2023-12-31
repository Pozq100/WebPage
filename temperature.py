from hal import hal_temp_humidity_sensor as temp_humid_sensor
from hal import hal_dc_motor as dc_motor
import time

def optimal_temp(Temperature):
    dc_motor.init()
    if Temperature > 20:
        dc_motor.set_motor_speed(50)
        speed = 50
    else:
        dc_motor.set_motor_speed(0)
        speed = 0
    return speed
def main():
    temp_humid_sensor.init()
    dc_motor.init()
    while True:
        Temperature, Humidity = temp_humid_sensor.read_temp_humidity()
        if Temperature != -100:
            optimal_temp(Temperature)

if __name__ == '__main__':
    main()