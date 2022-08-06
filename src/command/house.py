import time

from robomaster.chassis import Chassis
from robomaster.gripper import Gripper

from src.move import rotate_to
from src.odometer import get_point, set_point
from src.utils.house import move_to, move_back
from src.utils.points import find_point


def cmd_house(chassis: Chassis, gripper: Gripper):
	gripper.open()
	move_to(chassis, get_point())
	input("按下回车夹紧机械夹：")
	gripper.close()
	point = input("输入目的地：").upper()
	move_back(chassis, point)
	set_point(point)
	rotate_to(chassis, find_point(point)[4])
	chassis.move(x=0.15, xy_speed=1).wait_for_completed()
	chassis.drive_speed()
	gripper.open()
	time.sleep(1)
	chassis.move(x=-0.15, xy_speed=1).wait_for_completed()
	chassis.drive_speed()
	time.sleep(0.3)
	if point[0] == "A":
		rotate_to(chassis, -90)
	elif point[0] == "B":
		rotate_to(chassis, -180)
	elif point[0] == "C":
		rotate_to(chassis, 90)
	elif point[0] == "D":
		rotate_to(chassis, 0)

