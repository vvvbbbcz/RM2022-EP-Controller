from robomaster.robot import Robot

from src.odometer import set_real_pos
from src.tof_position import tof_position
from src.utils.command import home
from src.utils.vector import wrap_angle
from src.utils.vision_position import vision_position


def cmd_location(ep: Robot):
	# 区域
	area = 'A'
	cmd_1_1 = input("请输入区域：").upper()
	if len(cmd_1_1) == 0:
		return
	if home(cmd_1_1[0]):
		return
	elif cmd_1_1[0] == 'E':
		cmd_1_1_1 = input("请输入坐标(x,y,z)：")
		cmd_1_1_1_list = cmd_1_1_1.split(" ")
		if len(cmd_1_1_1_list) == 3:
			set_real_pos(float(cmd_1_1_1_list[0]), float(cmd_1_1_1_list[1]), float(cmd_1_1_1_list[2]))
			return
	elif cmd_1_1[0] == "F":
		tof_position(ep, ep.sensor)
		return
	area = cmd_1_1[0]
	# 询问重试
	retry = False
	print("是否重试，默认不重试")
	print("1.是")
	cmd_1_2 = input("请输入指令：")
	if len(cmd_1_2) == 0:
		return
	if home(cmd_1_2[0]):
		return
	if cmd_1_2[0] == "1":
		retry = True
	# 询问角度
	start = -180
	end = 180
	print("起始角 结束角，默认-180 180")
	cmd_1_3 = input("请输入指令：")
	cmd_1_3_list = cmd_1_3.split(" ")
	if home(cmd_1_3_list):
		return
	elif len(cmd_1_3_list) == 2:
		start = wrap_angle(float(cmd_1_3_list[0]))
		end = wrap_angle(float(cmd_1_3_list[1]))
	# 定位
	pos = vision_position(ep, retry, area, start, end)
	print("当前位置：" + str(pos))
	# 误差
	cmd_1_4 = input("请输入误差(x，y, z)，回车则跳过：")
	cmd_1_4_list = cmd_1_4.split(" ")
	if home(cmd_1_4_list):
		return
	elif len(cmd_1_4_list) == 3:
		pos = [pos[0] + float(cmd_1_4_list[0]), pos[1] + float(cmd_1_4_list[1]), pos[2] + float(cmd_1_4_list[2])]
	set_real_pos(pos[0], pos[1], pos[2])
