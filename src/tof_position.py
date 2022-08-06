import math

from robomaster.robot import Robot
from robomaster.sensor import DistanceSensor

from src.odometer import get_point, get_real_pos, set_real_pos


def set_distance(dis):
	area = get_point()[0]
	origin = get_real_pos()
	tof = dis[0] / 1000.0  # 单位转换
	if area == "A":
		if -120 < origin[2] < -60:  # 仅保留特定角度的数据
			set_real_pos(origin[0], -math.cos(math.degrees(origin[2] + 90)) * tof + 3.1, origin[2])  # 校正数据
	elif area == "B":
		if -150 < origin[2] <= -180 or 150 < origin[2] <= 180:
			set_real_pos(-math.cos(math.degrees(origin[2])) * tof - 3.1, origin[1], origin[2])
	elif area == "C":
		if 60 < origin[2] < 120:
			set_real_pos(origin[0], -math.cos(math.degrees(origin[2] + 90)) * tof - 3.1, origin[2])
	elif area == "D":
		if -30 < origin[2] < 30:
			set_real_pos(-math.cos(math.degrees(origin[2])) * tof + 3.1, origin[1], origin[2])


def tof_position(ep: Robot, sensor: DistanceSensor):
	sensor.sub_distance(freq=20, callback=set_distance)
