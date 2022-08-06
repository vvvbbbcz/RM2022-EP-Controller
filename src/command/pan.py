from robomaster.robot import Robot

from src.odometer import get_point
from src.utils.pan import move_to, check_point, servo_to, servo_back, move_back


def cmd_pan(ep: Robot):
	check_point(get_point())
	move_to(ep.chassis)
	servo_to(ep.servo)
	ep.chassis.drive_speed()
	input("请按回车键继续...")
	ep.chassis.drive_speed(x=-0.008, y=-0.01)
	input("请按回车键继续...")
	servo_back(ep.servo)
	move_back(ep.chassis)
