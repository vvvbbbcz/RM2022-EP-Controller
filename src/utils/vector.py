import math


def wrap_angle(angle: float):
	if angle > 180:
		angle = angle - 360
	if angle <= -180:
		angle = angle + 360
	return angle


def rotate(vector: list, angle):
	"""
	Rotate a vector by an angle in degrees.
	"""
	x, y = vector[0], vector[1]
	rad = angle * math.pi / 180
	cos = math.cos(rad)
	sin = math.sin(rad)
	return [x * cos + y * sin, -x * sin + y * cos]


def apply_offset(vector: list, offset):
	"""
	Apply an offset to a vector.
	"""
	return [vector[0] + offset[0], vector[1] + offset[1], vector[2] + offset[2]]


def calc_angle_to_y(vector):
	"""
	Calculate the angle to the y-axis.
	"""
	return wrap_angle(90 - math.degrees(math.atan2(vector[1], vector[0])))
