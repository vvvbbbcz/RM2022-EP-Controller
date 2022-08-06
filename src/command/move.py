from robomaster.robot import Robot

from src.move import move_ep, move_points
from src.odometer import get_point
from src.utils.command import home


def cmd_move(ep: Robot):
	cmd_2 = input("请输入单元格，默认A1：").upper()
	if len(cmd_2) == 0:
		return
	elif home(cmd_2[0]):
		return
	elif len(cmd_2) == 2:
		move_ep(ep, ep.chassis, get_point(), cmd_2)


def cmd_move_amount(ep: Robot):
	cmd_3 = input("请输入格子数，默认1：")
	if len(cmd_3) == 0:
		return
	elif home(cmd_3[0]):
		return
	elif len(cmd_3) == 1:
		move_points(ep, ep.chassis, get_point(), int(cmd_3))
