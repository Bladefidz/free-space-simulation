class Particle(object):
	"""
	Represent a particle in the space.

	At all times, the particle has a particular position and direction in the
	space. The robot also has a fixed speed.
	"""
	def __init__(self, position, space, actuator, sensor = None):
		"""
		Initializes a Particle in specified space.
		The particle has initial position in the space.
		The particle movement controlled by motor
		"""
		self.space = space
		self.actuator = actuator
		self.position = position
		self.speed = self.actuator.getSpeed()
		self.sensor = None
		if sensor:
			self.sensor = sensor(self.space)

	def move(self):
		"""
		Move the particle using Motor
		"""
		obstacles = None
		if self.sensor:
			self.sensor.ping(self.position)
			self.obstacles = self.sensor.locateObstacles()
		self.degree, self.speed = self.actuator.move(obstacles)
		# print(self.degree, self.speed)
		self.position = self.position.getNewPosition(
			self.degree, self.speed)

	def getPosition(self):
		"""
		Return the position of the particle

		returns: a Position object giving the particle's position.
		"""
		return self.position

	def getDirection(self):
		"""
		Return the direction of the particle defined by motor movement.

		returns: an integer d giving the direction of the robot as an angle
		degrees, 0 <= d <= 360.
		"""
		return self.degree

	def setPosition(self, position):
		"""
		Set the position of the particle to PARTICLE.

		position: a Position object.
		"""
		# if self.space.isPositionInSpace():
		# 	self.position = position
		raise NotImplementedError # don't change this!

	def setRobotDirection(self, direction):
		"""
		Set the direction of the particle to DIRECTION.

		direction: integer representing an angle in degrees
		"""
		raise NotImplementedError # don't change this!


def test():
	print("================================")
	print("Load modules")
	from position import Position2D
	from space import Rectangular2D
	from actuator import SimpleActuator
	from progression.series import Geometric
	from movement.polar import Compass

	print("\n================================")
	print("Init modules")
	pos = Position2D(0, 0)
	rectSpace = Rectangular2D(500, 500)
	geo = Geometric(4, 0.5)
	compass = Compass(geo, 'ENW')
	actuator = SimpleActuator(1, compass)
	particle = Particle(pos, rectSpace, actuator)

	print("\n================================")
	print("Move with particle 10x")
	for i in range(10):
		particle.move()
		print("Position and direction",
			particle.getPosition(), particle.getDirection())


if __name__ == '__main__':
	test()