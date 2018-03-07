import math

class Geometric(object):
	def __init__(self, a, r):
		"""
		Given the formula of geometry series:
		a: initial value
		r: ratio
		"""
		self.a = a
		self.pastVal = a
		self.curVal = a
		self.r = r

	def forward(self):
		"""
		Forward progression and update current value
		"""
		self.pastVal = self.curVal
		self.curVal = self.curVal * self.r

	def getCurVal(self):
		return self.curVal

	def getNextDistance(self):
		return abs(self.curVal - self.pastVal)

	def nextDirection(self):
		raise NotImplementedError # don't change this!


class Harmonic(Geometric):
	"""docstring for Harmonic"""
	def __init__(self, a, r):
		super().__init__(1/a, 1/r)


def test():
	print("======================")
	print("Load geometric series")
	geo = Geometric(4, 0.5)

	print("======================")
	print("Run 10 forward progression")
	for i in range(10):
		geo.forward()
		print("Current value and distance:",
			geo.getCurVal(), geo.getNextDistance())


if __name__ == '__main__':
	test()