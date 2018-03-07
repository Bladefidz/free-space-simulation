# Visualization of particle in 2 Dimensional Space

import math
import time

from tkinter import *

class Visualization2D(object):
	"""docstring for Visualization2D"""
	def __init__(self, numParticles, width, height, delay = 0.2):
		self.delay = delay

		self.max_dim = max(width, height)
		self.width = width
		self.height = height
		self.numParticles = numParticles

		# Initializing a drawing surface
		self.master = Tk()
		self.w = Canvas(self.master, width = 500, height = 500)
		self.w.pack()
		self.master.update()

		# Draw a backing and lines
		x1, y1 = self._map_coords(0, 0)
		x2, y2 = self._map_coords(width, height)
		self.w.create_rectangle(x1, y1, x2, y2, fill = "white")

		# Draw grid lines
		for i in range(width + 1):
			x1, y1 = self._map_coords(i, 0)
			x2, y2 = self._map_coords(i, height)
			self.w.create_line(x1, y1, x2, y2)
		for i in range(height + 1):
			x1, y1 = self._map_coords(0, i)
			x2, y2 = self._map_coords(width, i)
			self.w.create_line(x1, y1, x2, y2)

		# Draw some status text
		self.particles = None
		self.text = self.w.create_text(25, 0, anchor = NW, text = "Ready")
		self.master.update()

	def _map_coords(self, x, y):
		"Maps grid positions to window positions (in pixels)"
		return (250 + 450 * ((x - self.width / 2.0) / self.max_dim),
				250 + 450 * ((self.height / 2.0 - y) / self.max_dim))

	def _draw_particle(self, position, direction):
		"Returns a polygon representing a particle with the specified parameters."
		x, y = position.getX(), position.getY()
		d1 = direction + 165
		d2 = direction - 165
		x1, y1 = self._map_coords(x, y)
		x2, y2 = self._map_coords(x + 0.6 * math.sin(math.radians(d1)),
								  y + 0.6 * math.cos(math.radians(d1)))
		x3, y3 = self._map_coords(x + 0.6 * math.sin(math.radians(d2)),
								  y + 0.6 * math.cos(math.radians(d2)))
		return self.w.create_polygon([x1, y1, x2, y2, x3, y3], fill="red")

	def update(self, space, particles):
		# Delete all existing particles
		if self.particles:
			for particle in self.particles:
				self.w.delete(particle)
				self.master.update_idletasks()
		# Draw new particles
		self.particles = []
		conv = False
		for particle in particles:
			pos = particle.getPosition()
			x, y = pos.getX(), pos.getY()
			x1, y1 = self._map_coords(x - 0.08, y - 0.08)
			x2, y2 = self._map_coords(x + 0.08, y + 0.08)
			self.particles.append(self.w.create_oval(x1, y1, x2, y2,
				fill = "black"))
			self.particles.append(
				self._draw_particle(
					particle.getPosition(),
					particle.getDirection()))
		# Update text
		self.w.delete(self.text)
		# self.text = self.w.create_text(
		# 	25, 0, anchor=NW,
		# 	text = ""
		# )
		self.master.update()
		time.sleep(self.delay)

	def done(self):
		"Indicate that the animation is done so that we allow the user to close the window."
		mainloop()


def test():
	V2d = Visualization2D(1, 500, 500)


if __name__ == '__main__':
	test()