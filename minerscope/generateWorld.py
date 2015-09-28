from mcpi import minecraft as m
mc = m.Minecraft.create()

#generate the floor
for x in range(-100,12):
	for z in range(-12,100):
		mc.setBlock(x,0.0,z,4)
#generate the laboratory walls
for x in range(-35,-25):
	for y in range(1,5):
		mc.setBlock(x,y,55,20)
for z in range(55,65):
	for y in range(1,5):
		mc.setBlock(-35,y,z,20)
for x in range(-35,-25):
	for y in range(1,5):
		mc.setBlock(x,y,65,20)
for z in range(55,65):
	for y in range(1,5):
		mc.setBlock(-25,y,z,20)
for x in range(-35,-25):
	for z in range(55,65):
		mc.setBlock(x,5,z,20)
#Removing the 2 blocks to let the player inside the laboratory.
mc.setBlock(-25,1,60,0)
mc.setBlock(-25,2,60,0)
#Position the player in front of the laboratory
mc.player.setPos(-18,1.5,60.5)
mc.setBlock(-34,1,61,57)
mc.setBlock(-34,1,59,41)
mc.setBlock(-34,1,57,35,0)
mc.setBlock(-34,1,63,35,15)

