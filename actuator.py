class SimpleActuator(object):
	"""docstring for Motor"""
	def __init__(self, speed, steer):
		self.speed = speed
		self.steer = steer

	def accelerate(self, acc):
		self.speed += acc

	def decelerate(self, dec):
		self.speed -= acc

	def getSpeed(self):
		return self.speed

	def getDirection(self):
		return self.steer.getCurrentDirection()

	def move(self, obstacles):
		degree, self.speed = self.steer.getNextDirection()
		return degree, self.speed


def test():
	print("================================")
	print("Load modules")
	from movement.polar import Compass
	from progression.series import Geometric

	print("\n================================")
	print("Init modules")
	geo = Geometric(4, 0.5)
	compass = Compass(geo, 'NSEW')
	actuator = SimpleActuator(1, compass)

	print("\n================================")
	print("Move with actuator within 10 loop")
	for i in range(10):
		print(actuator.move(None))


if __name__ == '__main__':
	test()