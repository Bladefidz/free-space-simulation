import math

# === Provided class Position
class Position2D(object):
	"""docstring for Position"""
	def __init__(self, x, y):
		"""
		Initialize a position with coordinates (x, y).
		"""
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def getNewPosition(self, angle, speed):
		"""
		Computes and returns the new Position after a single clock-tick has
		passed, with this object as the current position, and with the
		specified angle and speed.

		Does NOT test whether the returned position fits inside the space.

		angle: number representing angle in degrees, 0 <= angle < 360
		speed: positive float representing speed

		Returns: a Position object representing the new position.
		"""
		old_x, old_y = self.getX(), self.getY()
		angle = float(angle)
		# Compute the change in position
		rad = math.radians(angle) - 0.001  # Round floating point error
		delta_x = speed * math.cos(rad)
		delta_y = speed * math.sin(rad)
		# Add that to the existing position
		new_x = old_x + delta_x
		new_y = old_y + delta_y
		return Position2D(new_x, new_y)

	def isEqualTo(self, that):
		if round(self.x, 4) == round(that.getX(), 4) and round(self.y, 4) == round(that.getY(), 4):
			return True
		return False

	def __str__(self):
		return "(%0.2f, %0.2f)" % (self.x, self.y)


def test():
	pos = Position(100.8, 900.9)


if __name__ == '__main__':
	test()