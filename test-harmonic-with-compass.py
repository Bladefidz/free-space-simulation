print("================================")
print("Load modules")
from position import Position2D
from space import Rectangular2D
from actuator import SimpleActuator
from progression.series import Harmonic
from movement.polar import Compass
from particle import Particle
from visualization import Visualization2D

print("\n================================")
print("Init modules")
anim = Visualization2D(1, 10, 10)
pos = Position2D(1, 0)
rectSpace = Rectangular2D(10, 10)
geo = Harmonic(1, 2)
compass = Compass(geo, 'NWE')
actuator = SimpleActuator(1, compass)
particle = Particle(pos, rectSpace, actuator)

print("\n================================")
print("Visualize particle movements until convergence")
lastPost = Position2D(0, 0)
while True:
	particle.move()
	pos = particle.getPosition()
	print("Position and direction", pos, particle.getDirection())
	anim.update(rectSpace, [particle])
	if pos.isEqualTo(lastPost):
		break
	lastPost = pos

anim.done()  # End of animation