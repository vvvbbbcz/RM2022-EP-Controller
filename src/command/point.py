from src.odometer import set_point, set_real_pos, get_real_pos
from src.utils.command import home
from src.utils.points import find_point


def cmd_set_point():
	cmd_8 = input("输入单元格：").upper()
	point = find_point(cmd_8)
	if len(cmd_8) == 0:
		return
	elif home(cmd_8[0]):
		return
	else:
		set_point(cmd_8)
		cmd_8_1 = input("是否矫正位置？1为是，回车否：")
		if len(cmd_8_1) == 0:
			return
		elif cmd_8_1[0] == "1":
			cmd_8_2 = input("请输入角度：")
			if len(cmd_8_2) == 0:
				set_real_pos(point[2], point[3], get_real_pos()[2])
				return
			elif home(cmd_8_2[0]):
				return
			set_real_pos(point[2], point[3], float(cmd_8_2))
