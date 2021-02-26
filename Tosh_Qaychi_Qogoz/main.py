import random

tanlovlar = ["Tosh", "Qaychi", "Qog'oz"]

computer_tanlovi = c = 0
person_tanlovi = p = 0

print("Natija: Computer: " + str(c) + "\tPlayer: " + str(p))

run = True
while run:

	computer_tanlovi = random.choice(tanlovlar)
	person_tanlovi = input("Tosh, Qaychi, Qog'oz yoki Chiqish: ")

	if person_tanlovi == computer_tanlovi:
		print("Durrang")
	elif person_tanlovi == "Tosh":
		if computer_tanlovi == "Qaychi":
			print("O'yinchi g'olib")
			p += 1
		else:
			print("Computer yutdi")
			c += 1


	elif person_tanlovi == "Qog'oz":
		if computer_tanlovi == "Tosh":
			print("O'yinchi g'olib")
			p += 1
		else:
			print("Computer yutdi")
			c += 1

	elif person_tanlovi == "Qaychi":
		if computer_tanlovi == "Qog'oz":
			print("O'yinchi g'olib")
			p += 1
		else:
			print("Computer yutdi")
			c += 1
	elif person_tanlovi == "Chiqish":
		break
	else:
		print("Error command")


	print("Player: " + person_tanlovi)
	print("Computer: " + computer_tanlovi)
	print("")
	print("Natija: Computer: " + str(c) + "\tPlayer: " + str(p))
	print("")