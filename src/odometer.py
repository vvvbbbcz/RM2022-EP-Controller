from robomaster.robot import Robot

from src.utils.vector import wrap_angle, rotate

chassis_pos = [0, 0, 0]
pos = [0, 0, 0]
offset = [0, 0, 0]
point = "A5"


def get_offset():
	return offset


def get_point():
	return point


def get_pos():
	return pos


def get_chassis_pos():
	return chassis_pos


def set_chassis_pos(pos_list):
	global chassis_pos
	chassis_pos[0] = pos_list[1]
	chassis_pos[1] = pos_list[0]


def set_offset(the_offset: list):
	global offset
	offset = the_offset


def set_chassis_rotate(rotate_list):
	global chassis_pos
	chassis_pos[2] = rotate_list[0]


def set_point(p: str):
	global point
	point = p


def add_offset(x, y, z):
	offset[0] += x
	offset[1] += y
	offset[2] += z


def get_real_pos():
	rotate_pos = rotate([chassis_pos[0], chassis_pos[1]], offset[2])
	return [rotate_pos[0] + offset[0], rotate_pos[1] + offset[1], wrap_angle(chassis_pos[2] + offset[2])]


def set_real_pos(x, y, z):
	angel_offset = z - chassis_pos[2]
	pos_rotate = rotate([chassis_pos[0], chassis_pos[1]], angel_offset)
	set_offset([x - pos_rotate[0], y - pos_rotate[1], z - chassis_pos[2]])


def init_odometer(ep: Robot):
	if not ep.chassis.sub_position(cs=0, freq=10, callback=set_chassis_pos):
		print("ERROR: 订阅底盘位置失败！")
	if not ep.chassis.sub_attitude(freq=10, callback=set_chassis_rotate):
		print("ERROR: 订阅底盘角度失败！")

