from src.odometer import get_real_pos, set_real_pos
from src.utils.command import home


def cmd_correct(chassis):
	origin = get_real_pos()
	new_offset = [0, 0, 0]
	while True:
		dis = input("x_distance：")
		if len(dis) == 0:
			break
		elif home(dis):
			return
		new_offset[0] = float(dis)
		# chassis.move(x=float(dis), xy_speed=1).wait_for_completed()
	while True:
		dis = input("y_distance：")
		if len(dis) == 0:
			break
		elif home(dis):
			return
		new_offset[1] = -float(dis)
		# chassis.move(y=float(dis), xy_speed=1).wait_for_completed()
	while True:
		degree = input("z_distance：")
		if len(degree) == 0:
			break
		elif home(degree):
			return
		new_offset[2] = float(degree)
		# chassis.move(z=-float(degree), z_speed=60).wait_for_completed()
	set_real_pos(origin[0] - new_offset[0], origin[1] - new_offset[1], origin[2] - new_offset[2])
