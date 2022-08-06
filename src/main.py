from robomaster import robot

from src.command.house import cmd_house
from src.command.location import cmd_location
from src.command.move import cmd_move, cmd_move_amount
from src.command.odometer import cmd_correct
from src.command.pan import cmd_pan
from src.command.point import cmd_set_point
from src.connect import start_connect
from src.odometer import init_odometer, chassis_pos, get_real_pos, get_offset
from src.shot import shot

ep = robot.Robot()


if __name__ == '__main__':
	print("=======================================")
	print("RM2022 基础营3组 EP机器人控制程序")
	print("=======================================")
	start_connect(ep)
	init_odometer(ep)
	ep.set_robot_mode(robot.CHASSIS_LEAD)
	ep.led.set_led(r=0, g=255, b=0)
	while True:
		print("=======================================")
		print("1.视觉+TOF定位")
		print("2.移动 {单元格}")
		print("3.移动 {格子数}")
		print("4.盖房【单元格】")
		print("5.转转盘")
		print("6.敲铃铛")
		print("7.打靶")
		print("8.起始单元格设置")
		print("=======================================")

		command = input("请输入指令：")
		cmd_list = command.split(" ")
		if cmd_list[0] == "1":
			cmd_location(ep)
		elif cmd_list[0] == "2":
			cmd_move(ep)
		elif cmd_list[0] == "3":
			cmd_move_amount(ep)
		elif cmd_list[0] == "4":
			cmd_house(ep.chassis, ep.gripper)
		elif cmd_list[0] == "5":
			cmd_pan(ep)
		elif cmd_list[0] == "7":
			shot(ep)
		elif cmd_list[0] == "8":
			cmd_set_point()
		elif cmd_list[0] == "9":
			cmd_correct(ep.chassis)
		elif cmd_list[0] == "0":
			print(chassis_pos)
			print(get_offset())
			print(get_real_pos())
	ep.chassis.unsub_position()
	ep.close()
