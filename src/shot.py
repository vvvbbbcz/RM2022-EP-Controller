import time

from robomaster import robot, blaster
from robomaster.ai_module import AiModule
from robomaster.blaster import Blaster
from robomaster.chassis import Chassis
from robomaster.gimbal import Gimbal
from robomaster.robot import Robot
from src.move import rotate_to
from src.odometer import get_point
from src.utils.shotter import aim_goal

goal_list = []
goal_amount: int = 0
start_time = 0


def shot_goal(gimbal: Gimbal, ep_blaster: Blaster, goal: int):
	while goal_amount > 0 and len(goal_list) > goal and time.time() < start_time + 15:
		if len(goal_list[goal]) > 2:
			g_1 = goal_list[goal][1] / 320
			g_2 = goal_list[goal][2] / 240

			if 0.495 < g_1 < 0.505 and 0.645 < g_2 < 0.655:  # 判断是否瞄准标靶
				break
			aim_move = aim_goal([g_1, g_2])
			print(goal)
			gimbal.drive_speed(aim_move[0], aim_move[1])
			time.sleep(0.1)  # 设置延时以防止通信问题
	gimbal.move(pitch=1, pitch_speed=30).wait_for_completed()
	ep_blaster.set_led()
	ep_blaster.fire()  # 发射水弹
	ep_blaster.set_led(effect=blaster.LED_OFF)
	time.sleep(0.9)  # 设置延时使水弹发射速度符合要求


	# pid_Yaw.set_error(variable_X - 0.5)
	# pid_Pitch.set_error(0.65 - variable_Y)
	# gimbal_ctrl.rotate_with_speed(pid_Yaw.get_output(),pid_Pitch.get_output())
	# time.sleep(0.05)
	# variable_Post = 0.05
	# if abs(variable_X - 0.5) <= variable_Post and abs(0.65 - variable_Y) <= variable_Post:
	# 	gun_ctrl.set_fire_count(1)
	# 	led_ctrl.gun_led_on()
	# 	ir_blaster_ctrl.fire_once()
	# 	gun_ctrl.fire_once()
	# 	led_ctrl.gun_led_off()


def choose():
	index = 0
	min_index = 0
	while index < goal_amount:
		g_in_1 = goal_list[index][1] / 320
		g_in_2 = goal_list[index][2] / 240
		g_min_1 = goal_list[min_index][1] / 320
		g_min_2 = goal_list[min_index][2] / 240
		dis_1 = (g_in_1 - 0.5) * (g_in_1 - 0.5) + (g_in_2 - 0.5) * (g_in_2 - 0.5)
		dis_2 = (g_min_1 - 0.5) * (g_min_1 - 0.5) + (g_min_2 - 0.5) * (g_min_2 - 0.5)
		if dis_1 < dis_2:
			min_index = index
		index += 1
	return min_index


def set_goals(ai_info):
	global goal_list
	global goal_amount
	goal_amount = ai_info[0]
	goal_list = ai_info[1]
	# while index < goal_amount:
	# 	goal_list[index][0] = ai_info[1][index][0]
	# 	goal_list[index][1] = ai_info[1][index][1] / 320
	# 	goal_list[index][2] = ai_info[1][index][2] / 240
	# 	goal_list[index][3] = ai_info[1][index][3] / 320
	# 	goal_list[index][4] = ai_info[1][index][4] / 240
	# 	goal_list[index][5] = ai_info[1][index][5] / 100


def shot(ep: Robot):
	global goal_list
	global start_time
	gimbal: Gimbal = ep.gimbal
	chassis: Chassis = ep.chassis
	ai: AiModule = ep.ai_module
	point = get_point()
	area = point[0]
	index = int(point[1])
	ai.sub_ai_event(callback=set_goals)
	start_time = time.time()
	ep.set_robot_mode(robot.FREE)
	if area == "A":
		rotate_to(chassis, -90)
	elif area == "B":
		rotate_to(chassis, -180)
	elif area == "C":
		rotate_to(chassis, 90)
	elif area == "D":
		rotate_to(chassis, 0)
	gimbal.moveto(pitch=10, yaw=-90.0 * (index - 1.0) / 8.0, pitch_speed=30, yaw_speed=180)

	while time.time() < start_time + 15:
		# pass
		if goal_amount > 0:
			shot_goal(gimbal, ep.blaster, choose())
	time.sleep(0.3)
	gimbal.recenter(yaw_speed=180).wait_for_completed()
