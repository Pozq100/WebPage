from hal import hal_servo as servo
<<<<<<< Updated upstream
import time
=======
import main_test1 as test
>>>>>>> Stashed changes
def optimal_ec(Moisture_sensor):
    if not Moisture_sensor:
        servo.set_servo_position(45)
        position = 45
    else:
        servo.set_servo_position(0)
        position = 0
    return position
def main():
    servo.init()
    while True:
        optimal_ec(test.moisture_reading)

if __name__ == '__main__':
    main()