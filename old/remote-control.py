import motorlibrary as mc

while True:
	input = mc.GetCharicter()

	if input == "w":
		mc.MoveBy("f", 0.5)
	elif input == "s":
		mc.MoveBy("b", 0.5)
	elif input == "a":
		mc.Turn("l")
	elif input == "d":
		mc.Turn("r")
	elif input == " ":
		mc.Turn("s")
	elif input == "e":
		break