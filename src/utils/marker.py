from simple_pid import PID

# TODO 坐标系变换
marker_a = [[0.5, 0.675, 0, 0, -1], [-0.5, 0.675, 0, 0, -1]]
marker_b = [[-0.675, 0.5, 0, 0, -1], [-0.675, -0.5, 0, 0, -1]]
marker_c = [[-0.5, -0.675, 0, 0, -1], [0.5, -0.675, 0, 0, -1]]
marker_d = [[0.675, -0.5, 0, 0, -1], [0.675, 0.5, 0, 0, -1]]


def has_marker(marker_list, the_marker):
	"""
	判断是否有对应的marker
	:param marker_list: 要查找的列表
	:param the_marker: 要查找的marker内容
	:return: True/False
	"""
	index = 0
	while index < len(marker_list):
		if marker_list[index][4] == the_marker:
			return True
		index += 1
	return False


def find_marker_from_list(marker_list, the_marker):
	"""
	从列表中查找对应的marker，返回marker的信息。
	如果没有找到，返回[]。
	:param marker_list: 要查找的列表
	:param the_marker: 要查找的marker内容
	:return: x, y, 长度, 高度，marker内容
	"""
	goal = []
	index = 0
	while index < len(marker_list):
		if marker_list[index][4] == the_marker:
			goal = list(marker_list[index])
			return goal
		index += 1
	return goal


def aim_marker(pitch, yaw, marker_info):
	"""
	根据marker的信息，计算目标pitch和yaw。
	:param pitch: 当前云台pitch
	:param yaw: 当前云台yaw
	:param marker_info: marker的信息，与find_marker_from_list()返回的信息相同
	:return
	"""
	marker_pos_x = 0.5 - marker_info[1]
	marker_pos_y = marker_info[0] - 0.5
	pitch_pid = PID(Kp=100, setpoint=pitch + marker_pos_x)
	yaw_pid = PID(Kp=100, setpoint=yaw + marker_pos_y)
	return [pitch_pid(pitch), yaw_pid(yaw)]
