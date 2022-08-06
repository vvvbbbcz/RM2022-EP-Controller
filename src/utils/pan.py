import time

from robomaster.chassis import Chassis
from robomaster.servo import Servo


def check_point(point: str):
	point = point.upper()
	return point[0] == "E" and (point[1] == "1" or point[1] == "3")


def move_to(chassis: Chassis):
	chassis.move(z=-45, z_speed=45).wait_for_completed()
	time.sleep(0.3)
	chassis.move(y=-0.3, xy_speed=1).wait_for_completed()
	chassis.drive_speed()


def move_back(chassis: Chassis):  # TODO
	chassis.move(y=0.3, xy_speed=1).wait_for_completed()
	time.sleep(0.3)
	chassis.move(z=45, z_speed=45).wait_for_completed()


def servo_to(servo: Servo):
	servo.moveto(index=2, angle=-78).wait_for_completed()
	time.sleep(1)


def servo_back(servo: Servo):
	servo.moveto(index=2, angle=-35).wait_for_completed()
	time.sleep(1)
