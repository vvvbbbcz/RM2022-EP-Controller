import time

from robomaster import robot
from robomaster.chassis import Chassis
from robomaster.robot import Robot

from src.odometer import get_real_pos, set_point
from src.utils.points import find_point, get_next_str
from src.utils.vector import wrap_angle


def rotate_to(chassis: Chassis, degree):
	chassis.move(z=wrap_angle(get_real_pos()[2] - degree), z_speed=120).wait_for_completed()


def move_ep(ep: Robot, chassis: Chassis, from_point: str, to_point: str):
	ep.set_robot_mode(robot.CHASSIS_LEAD)
	from_area = from_point[0]  # TODO
	from_index = int(from_point[1])
	to_area = to_point[0]
	to_index = int(to_point[1])
	goal = find_point(to_point)
	if from_area == "A":
		rotate_to(chassis, -90)
		time.sleep(0.3)
		if from_index <= 5:
			chassis.move(x=get_real_pos()[0] - 2.85, xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_area == "A" and to_index <= 5:
				chassis.move(y=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(y=2.85 - get_real_pos()[1], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		else:
			chassis.move(y=2.85 - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
		time.sleep(0.3)
		chassis.move(x=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
		chassis.drive_speed()
	elif from_area == "B":
		rotate_to(chassis, -180)
		time.sleep(0.3)
		if from_index <= 5:
			chassis.move(x=get_real_pos()[1] - 2.85, xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_area == "B" and to_index <= 5:
				chassis.move(y=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(y=get_real_pos()[0] + 2.85, xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		else:
			chassis.move(y=get_real_pos()[0] + 2.85, xy_speed=1).wait_for_completed()  # 移动到边线
			chassis.drive_speed()
		time.sleep(0.3)
		chassis.move(x=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
		chassis.drive_speed()
	elif from_area == "C":
		rotate_to(chassis, 90)
		time.sleep(0.3)
		print(from_point)
		if from_index <= 5:
			chassis.move(x=-2.85 - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_area == "C" and to_index <= 5:
				chassis.move(y=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(y=get_real_pos()[1] + 2.85, xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		else:
			chassis.move(y=get_real_pos()[1] + 2.85, xy_speed=1).wait_for_completed()
			chassis.drive_speed()
		time.sleep(0.3)
		chassis.move(x=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
		chassis.drive_speed()
	elif from_area == "D":
		rotate_to(chassis, 0)
		time.sleep(0.3)
		if from_index <= 5:
			chassis.move(x=-2.85 - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_area == "D" and to_index <= 5:
				chassis.move(y=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(y=2.85 - get_real_pos()[0], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		else:
			chassis.move(y=2.85 - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
		time.sleep(0.3)
		chassis.move(x=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
		chassis.drive_speed()
	elif from_area == "E":
		if from_index == 1:
			rotate_to(chassis, 0)
			time.sleep(0.3)
			chassis.move(y=2.85 - get_real_pos()[0], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_index <= 5:
				chassis.move(x=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(x=2.85 - get_real_pos()[1], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		elif from_index == 2:
			rotate_to(chassis, -90)
			time.sleep(0.3)
			chassis.move(y=2.85 - get_real_pos()[1], xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_index <= 5:
				chassis.move(x=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(x=get_real_pos()[0] + 2.85, xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		elif from_index == 3:
			rotate_to(chassis, -180)
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[0] + 2.85, xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_index <= 5:
				chassis.move(x=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(x=2.85 + get_real_pos()[1], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
		elif from_index == 4:
			rotate_to(chassis, 90)
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[1] + 2.85, xy_speed=1).wait_for_completed()
			chassis.drive_speed()
			time.sleep(0.3)
			if to_index <= 5:
				chassis.move(x=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			else:
				chassis.move(x=2.85 - get_real_pos()[0], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
	time.sleep(0.3)
	# To
	if to_area == "A":
		rotate_to(chassis, -90)
		time.sleep(0.3)
		if to_index <= 5:
			chassis.move(x=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
			
		else:
			if from_area != "A":
				chassis.move(x=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			chassis.move(y=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			
	elif to_area == "B":
		rotate_to(chassis, -180)
		time.sleep(0.3)
		if to_index <= 5:
			chassis.move(x=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
			
		else:
			if from_area != "B":
				chassis.move(x=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
				chassis.drive_speed()
			chassis.move(y=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
			
	elif to_area == "C":
		rotate_to(chassis, 90)
		time.sleep(0.3)
		if to_index <= 5:
			chassis.move(x=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			
		else:
			if from_area != "C":
				chassis.move(x=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()  # TODO
				chassis.drive_speed()
			chassis.move(y=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
			
	elif to_area == "D":
		rotate_to(chassis, 0)
		time.sleep(0.3)
		if to_index <= 5:
			chassis.move(x=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			
		else:
			if from_area != "D":
				chassis.move(x=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()  # TODO
				chassis.drive_speed()
			chassis.move(y=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			
	elif to_area == "E":
		if to_index == 1:
			rotate_to(chassis, 0)
			time.sleep(0.3)
			chassis.move(y=goal[2] - get_real_pos()[0], xy_speed=1).wait_for_completed()
			
		elif to_index == 2:
			rotate_to(chassis, -90)
			time.sleep(0.3)
			chassis.move(y=goal[3] - get_real_pos()[1], xy_speed=1).wait_for_completed()
			
		elif to_index == 3:
			rotate_to(chassis, -180)
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[0] - goal[2], xy_speed=1).wait_for_completed()
			
		elif to_index == 4:
			rotate_to(chassis, 90)
			time.sleep(0.3)
			chassis.move(y=get_real_pos()[1] - goal[3], xy_speed=1).wait_for_completed()
			
	set_point(to_point)


def move_points(ep: Robot, chassis: Chassis, from_point: str, amount: int):
	index = 0
	point = from_point
	while index < amount:
		point = get_next_str(point)
		index += 1
	move_ep(ep, chassis, from_point, point)
