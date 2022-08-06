from simple_pid import PID


def aim_goal(goal_xy):
	"""
	:param yaw: ...
	:param pitch: ...
	:param goal_xy: marker的信息，与find_marker_from_list()返回的信息相同
	:return
	"""
	marker_pitch = 0.65 - goal_xy[1]
	marker_yaw = goal_xy[0] - 0.5
	pitch_pid = PID(Kp=85, Kd=3, setpoint=marker_pitch)
	yaw_pid = PID(Kp=115, Ki=1, Kd=5, setpoint=marker_yaw)
	return [pitch_pid(0), yaw_pid(0)]
