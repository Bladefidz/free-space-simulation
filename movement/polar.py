class Compass():
	"""
	Movement using geometric series pattern with compass direction
	(North 90, South 270, East 0, West 180).
	"""
	def __init__(self, progression, pattern):
		"""
		pattern	String 	movement pattern. ex: NSEW for north-south-east-west
		"""
		self.progression = progression
		self.pattern = pattern
		self.curPatternId = 0  # Current selected pattern movement

	def toDegree(self, pat):
		if pat == 'N':
			return 90
		if pat == 'S':
			return 270
		if pat == 'E':
			return 0
		if pat == 'W':
			return 180

	def getCurrentDirection(self):
		return self.toDegree(self.pattern[self.curPatternId])

	def getNextDirection(self):
		"""
		Get compass direction in degree
		"""
		self.progression.forward()
		if self.curPatternId+1 > len(self.pattern):
			self.curPatternId = 0
		pat = self.toDegree(self.pattern[self.curPatternId])
		self.curPatternId += 1
		return pat, self.progression.getNextDistance()


def test():
	import sys
	sys.path.insert(0, '../progression')
	from series import Geometric

	print("======================================")
	print("Load geometric progression and compass")
	geo = Geometric(4, 0.5)
	comp = Compass(geo, 'NSEW')

	print("\n======================================")
	print("Testing 10 movement of geometric progression using compass")
	for i in range(10):
		print(comp.getNextDirection())


if __name__ == '__main__':
	test()