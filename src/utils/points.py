points = [['A', 1, 2.09, 0.34, -45],
		  ['A', 2, 2.35, 0.73, -65],
		  ['A', 3, 2.43, 1.19, -90],
		  ['A', 4, 2.35, 1.64, -115],
		  ['A', 5, 2.09, 2.09, -135],
		  ['A', 6, 1.67, 2.35, -155],
		  ['A', 7, 1.19, 2.43, -180],
		  ['A', 8, 0.73, 2.35, -155],
		  ['A', 9, 0.34, 2.09, -135],
		  ['E', 2, 0, 1.74],
		  ['B', 1, -0.34, 2.09, -135],
		  ['B', 2, -0.73, 2.35, -155],
		  ['B', 3, -1.19, 2.43, 180],
		  ['B', 4, -1.64, 2.35, 155],
		  ['B', 5, -2.09, 2.09, 135],
		  ['B', 6, -2.35, 1.64, 115],
		  ['B', 7, -2.43, 1.19, 90],
		  ['B', 8, -2.35, 0.73, 65],
		  ['B', 9, -2.09, 0.34, 45],
		  ['E', 3, -1.74, 0],
		  ['C', 1, -2.09, -0.34, 135],
		  ['C', 2, -2.35, -0.73, 115],
		  ['C', 3, -2.43, -1.19, 90],
		  ['C', 4, -2.35, -1.64, 65],
		  ['C', 5, -2.09, -2.09, 45],
		  ['C', 6, -1.67, -2.35, 25],
		  ['C', 7, -1.19, -2.43, 0],
		  ['C', 8, -0.73, -2.35, -25],
		  ['C', 9, -0.34, -2.09, -45],
		  ['E', 4, 0, -1.74],
		  ['D', 1, 0.34, -2.09, 45],
		  ['D', 2, 0.73, -2.35, 25],
		  ['D', 3, 1.19, -2.43, 0],
		  ['D', 4, 1.64, -2.35, -25],
		  ['D', 5, 2.09, -2.09, -4],
		  ['D', 6, 2.35, -1.64, -65],
		  ['D', 7, 2.43, -1.19, -90],
		  ['D', 8, 2.35, -0.73, -115],
		  ['D', 9, 2.09, -0.34, -135],
		  ['E', 1, 1.74, 0],
		  ]


def get_point_index(point: str):
	index = 0
	while index < len(points):
		if len(point) == 2:
			if points[index][0] == point[0] and points[index][1] == int(point[1]):
				return index
		index += 1
	return 0


def find_point(point: str):
	return points[get_point_index(point)]


def get_next_index(point: str):
	index = get_point_index(point)
	if index < len(points) - 1:
		return index + 1
	else:
		return 0


def get_next(point: str):
	return points[get_next_index(point)]


def get_next_str(point: str):
	return points[get_next_index(point)][0] + str(points[get_next_index(point)][1])
