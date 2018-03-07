from position import Position2D

class Rectangular2D(object):
	"""
	A RectangularSpace represents a rectangular region.

	A space has a width and a height and contains (width * height) tiles.
	"""
	def __init__(self, width, height):
		"""
		Initializes a rectangular space with the specified width and height.

		width: an integer > 0
		height: an integer > 0
		"""
		if width > 0 and height > 0:
			self.width = width
			self.height = height
			self.size = self.width * self.height

	def getNumTiles(self):
		"""
		Return the total number of tiles in the space

		returns: an integer
		"""
		return self.size

	def getRandomPosition(self):
		"""
		Return a random position inside the space.

		returns: a position object.
		"""
		return Position2D(
			random.uniform(0, self.width),
			random.uniform(0, self.height))

	def isPositionInSpace(self, pos):
		"""
		Return True if pos is inside the space.

		pos: a position object.
		returns: True if pos is in the space, False otherwise
		"""
		if pos.getX() < 0.0 or pos.getY() < 0.0:
			return False
		if int(pos.getX()) >= self.width or int(pos.getY()) >= self.height:
			return False
		return True


def test():
	rs = Rectangular2D(500, 500)


if __name__ == '__main__':
	test()