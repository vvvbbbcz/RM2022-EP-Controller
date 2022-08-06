import math
import time

from robomaster import robot
from robomaster.gimbal import Gimbal
from robomaster.robot import Robot
from robomaster.vision import Vision

from src.utils import marker
from src.utils.marker import marker_a, marker_b, marker_c, marker_d
from src.utils.vector import rotate, wrap_angle

scanning_marker = []
gimbal_pitch = 0
gimbal_yaw = 0
gimbal_ground_pitch = 0
gimbal_ground_yaw = 0


def calc_abs_pos(area, relative_x, relative_y, cos_alpha, cos_beta):
	x, y = 0, 0
	if cos_alpha >= 0:
		if cos_beta >= 0:
			area_x = relative_x + -0.5
			area_y = relative_y + 0
		else:
			area_x = relative_x + -0.33
			area_y = relative_y + 0
	else:
		area_x = relative_x + -0.67
		area_y = relative_y + 0
	if area == 'A':
		x = -area_x
		y = marker_a[0][1] + area_y
	elif area == 'B':
		x = marker_b[0][0] - area_y
		y = -area_x
	elif area == 'C':
		x = area_x
		y = marker_c[0][1] - area_y
	elif area == 'D':
		x = marker_d[0][0] + area_y
		y = area_x
	return [x, y, area_x, area_y]


def get_angle_correct(x, y, the_marker_info):
	return the_marker_info[1][3] + math.degrees(math.atan((x - 0.5) / y))


def move_ep_to(from_x, from_y, goal_x, goal_y, chassis):
	chassis.move_ep(x=-(goal_x - from_x), xy_speed=1.0).wait_for_completed()
	time.sleep(0.3)
	chassis.move_ep(y=-(from_y - goal_y), xy_speed=1.0).wait_for_completed()
	time.sleep(0.3)
	chassis.move_ep(x=0, y=0, xy_speed=1.0).wait_for_completed()


def scan_markers(gimbal, area='A', from_yaw=-180, to_yaw=180, retry=False):
	global scanning_marker
	scan_field = False
	markers = ['A', '1']
	marker_info = marker_a
	if area == 'A':
		markers = ['A', '1']
		marker_info = marker_a
	elif area == 'B':
		markers = ['B', '2']
		marker_b[0][2] = 0
		marker_b[1][2] = 0
		marker_info = marker_b
	elif area == 'C':
		markers = ['C', '3']
		marker_c[0][2] = 0
		marker_c[1][2] = 0
		marker_info = marker_c
	elif area == 'D':
		markers = ['D', '4']
		marker_d[0][2] = 0
		marker_d[1][2] = 0
		marker_info = marker_d
	while True:
		gimbal.moveto(pitch=5, yaw=from_yaw, pitch_speed=10, yaw_speed=180).wait_for_completed()
		gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
		if not scan_field:
			while len(marker.find_marker_from_list(scanning_marker, markers[0])) < 5:  # 等待扫描到C
				if gimbal_yaw >= to_yaw:
					scan_field = True
					break
			while marker_info[0][2] <= 0:  # 标签没有被扫描(记录)过，则持续瞄准
				the_marker = marker.find_marker_from_list(scanning_marker, markers[0])
				if len(the_marker) == 5:  # 防止瞬间丢目标导致的数组越界
					if 0.495 < the_marker[0] < 0.505 and 0.495 < the_marker[1] < 0.505:
						record_marker(markers[0], gimbal_yaw, 0.26 / the_marker[3] + 0.08)
						time.sleep(0.3)
						gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
						break
					# 持续瞄准标签C
					aim_move = marker.aim_marker(gimbal_pitch, gimbal_yaw, the_marker)
					gimbal.drive_speed(aim_move[0], aim_move[1])
				else:
					print("WARN: marker " + markers[0] + " missed")
		if not scan_field:
			while len(marker.find_marker_from_list(scanning_marker, markers[1])) < 5:
				gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
				if gimbal_yaw >= 180:
					scan_field = True
					break
			while marker_info[1][2] <= 0:
				the_marker = marker.find_marker_from_list(scanning_marker, markers[1])
				if len(the_marker) == 5:  # 防止瞬间丢目标导致的数组越界
					if 0.495 < the_marker[0] < 0.505 and 0.495 < the_marker[1] < 0.505:
						record_marker(markers[1], gimbal_yaw, 0.26 / the_marker[3] + 0.08)
						time.sleep(0.3)
						gimbal.drive_speed(pitch_speed=0, yaw_speed=30)
						break
					aim_move = marker.aim_marker(gimbal_pitch, gimbal_yaw, the_marker)
					gimbal.drive_speed(aim_move[0], aim_move[1])
				else:
					print("WARN: marker " + markers[1] + " missed")
		if (marker_info[0][2] > 0 and marker_info[1][2] > 0) or not retry:
			break


def set_scanning_marker(marker_list):
	global scanning_marker
	scanning_marker = marker_list


def record_marker(marker_id, angle, distance):
	if marker_id == 'A':
		marker_a[0][2] = 1
		marker_a[0][3] = angle
		marker_a[0][4] = distance
	if marker_id == '1':
		marker_a[1][2] = 1
		marker_a[1][3] = angle
		marker_a[1][4] = distance
	if marker_id == 'B':
		marker_b[0][2] = 1
		marker_b[0][3] = angle
		marker_b[0][4] = distance
	if marker_id == '2':
		marker_b[1][2] = 1
		marker_b[1][3] = angle
		marker_b[1][4] = distance
	if marker_id == 'C':
		marker_c[0][2] = 1
		marker_c[0][3] = angle
		marker_c[0][4] = distance
	if marker_id == '3':
		marker_c[1][2] = 1
		marker_c[1][3] = angle
		marker_c[1][4] = distance
	if marker_id == 'D':
		marker_d[0][2] = 1
		marker_d[0][3] = angle
		marker_d[0][4] = distance
	if marker_id == '4':
		marker_d[1][2] = 1
		marker_d[1][3] = angle
		marker_d[1][4] = distance


def relative_pos(marker_info):
	cos_alpha = ((1 + marker_info[0][4] * marker_info[0][4]) - marker_info[1][4] * marker_info[1][4]) / (
				2 * marker_info[0][4])
	cos_beta = ((1 + marker_info[1][4] * marker_info[1][4]) - marker_info[0][4] * marker_info[0][4]) / (
				2 * marker_info[1][4])
	relative_y = math.cos(math.radians((math.degrees(math.acos(cos_alpha)) - 90))) * marker_info[0][4]
	relative_x = math.tan(math.asin(cos_alpha)) * relative_y - 0
	return [relative_x, relative_y, cos_alpha, cos_beta]


def set_gimbal_angle_value(angle_list):
	global gimbal_pitch
	global gimbal_yaw
	global gimbal_ground_pitch
	global gimbal_ground_yaw
	gimbal_pitch = angle_list[0]
	gimbal_yaw = angle_list[1]
	gimbal_ground_pitch = angle_list[2]
	gimbal_ground_yaw = angle_list[3]


def vision_position(ep: Robot, retry: bool, area: chr, from_yaw=-180, to_yaw=180):
	gimbal: Gimbal = ep.gimbal
	vision: Vision = ep.vision
	ep.set_robot_mode(mode=robot.FREE)
	gimbal.sub_angle(freq=20, callback=set_gimbal_angle_value)
	vision.sub_detect_info(name="marker", color="red", callback=set_scanning_marker)
	marker_info = marker_a
	if area == 'A':
		marker_a[0][2] = 0
		marker_a[1][2] = 0
		marker_info = marker_a
	elif area == 'B':
		marker_b[0][2] = 0
		marker_b[1][2] = 0
		marker_info = marker_b
	elif area == 'C':
		marker_c[0][2] = 0
		marker_c[1][2] = 0
		marker_info = marker_c
	elif area == 'D':
		marker_d[0][2] = 0
		marker_d[1][2] = 0
		marker_info = marker_d
	scan_markers(gimbal, area, from_yaw, to_yaw, retry)  # TODO area
	relative = relative_pos(marker_info)
	pos = calc_abs_pos(area, relative[0], relative[1], relative[2], relative[3])
	print("获取到位置" + str(pos))
	yaw = get_angle_correct(pos[2], pos[3], marker_info)
	print(yaw)
	if area == 'A':
		yaw = wrap_angle(-yaw - 135)
	elif area == 'B':
		yaw = wrap_angle(-yaw + 135)
	elif area == 'C':
		yaw = wrap_angle(-yaw + 45)
	elif area == 'D':
		yaw = wrap_angle(-yaw - 45)
	print("获取到角度" + str(yaw))
	pos = rotate(pos, 45)
	gimbal.recenter(pitch_speed=30, yaw_speed=180).wait_for_completed()
	gimbal.unsub_angle()
	vision.unsub_detect_info("marker")
	return [pos[0], pos[1], yaw]
