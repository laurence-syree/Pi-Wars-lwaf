import motorlibrary as mc

while True:
	input = mc.GetCharicter()

	if input == "w":
		MoveBy("f", 0.5)
	elif input == "s":
		MoveBy("b", 0.5)
	elif input == "a":
		Turn("l")
	elif input == "d":
		Turn("r")
	elif input == " ":
		Turn("s")
	elif input == "e":
		break