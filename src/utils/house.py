import time

from robomaster.chassis import Chassis

from src.move import rotate_to
from src.odometer import get_real_pos
from src.utils.points import find_point

point_a = [2.8, 2.8]
point_b = [-2.8, 2.8]
point_c = [-2.8, -2.8]
point_d = [2.8, -2.8]


def move_to(chassis: Chassis, point: str):
	area = point[0]
	index = int(point[1])
	if area == "A":
		rotate_to(chassis, -90)
		if index <= 5:
			chassis.move(x=get_real_pos()[0] - point_a[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=point_a[1] - get_real_pos()[1], xy_speed=1).wait_for_completed()
		else:
			chassis.move(y=point_a[1] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=get_real_pos()[0] - point_a[0], xy_speed=1).wait_for_completed()
	elif area == "B":
		rotate_to(chassis, -180)
		if index <= 5:
			chassis.move(x=get_real_pos()[1] - point_b[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[0] - point_b[0], xy_speed=1).wait_for_completed()
		else:
			chassis.move(y=get_real_pos()[0] - point_b[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=get_real_pos()[1] - point_b[1], xy_speed=1).wait_for_completed()
	elif area == "C":
		rotate_to(chassis, 90)
		if index <= 5:
			chassis.move(x=point_c[0] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[1] - point_c[1], xy_speed=1).wait_for_completed()
		else:
			chassis.move(y=get_real_pos()[1] - point_c[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=point_c[0] - get_real_pos()[0], xy_speed=1).wait_for_completed()
	elif area == "D":
		rotate_to(chassis, 0)
		if index <= 5:
			chassis.move(x=point_d[1] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=point_d[0] - get_real_pos()[0], xy_speed=1).wait_for_completed()
		else:
			chassis.move(y=point_d[0] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=point_d[1] - get_real_pos()[1], xy_speed=1).wait_for_completed()


def move_back(chassis: Chassis, the_point: str):
	point = find_point(the_point)
	area = point[0]
	index = point[1]
	if area == "A":
		rotate_to(chassis, -90)
		if index <= 5:
			chassis.move(y=point[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=get_real_pos()[0] - point[2], xy_speed=1).wait_for_completed()
		else:
			chassis.move(x=get_real_pos()[0] - point[2], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=point[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
	elif area == "B":
		rotate_to(chassis, -180)
		if index <= 5:
			chassis.move(y=get_real_pos()[0] - point[2], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=get_real_pos()[1] - point[3], xy_speed=1).wait_for_completed()
		else:
			chassis.move(x=get_real_pos()[1] - point[3], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[0] - point[2], xy_speed=1).wait_for_completed()
	elif area == "C":
		rotate_to(chassis, 90)
		if index <= 5:
			chassis.move(y=get_real_pos()[1] - point[3], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=point[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
		else:
			chassis.move(x=point[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[1] - point[3], xy_speed=1).wait_for_completed()
	elif area == "D":
		rotate_to(chassis, 0)
		if index <= 5:
			chassis.move(y=point[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(x=point[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
		else:
			chassis.move(x=point[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			chassis.move(y=point[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
