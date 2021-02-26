import random

book = {}

yana = True
print("ContactBook ga kerakli odam ismi va nomerini kiriting: \n")
while yana:
	name = input("Ismi: ").upper()
	phone = input("Nomeri: +998")
	if len(phone) != 9:
		print("9 xonali raqam kiriting.")

	book[name] = phone

	yana = int(input("Contactga yana odam qoshsayiz '1' ni bosing. Kiritishni tugatish uchun '0' ni bosing: "))

while True:
	search = input("ContactBook dan ism boyicha qidirmoqchimisiz[ha/yoq]: ")

	if search == "ha":
		name = input("Kerakli ismni kiriting: ").upper()
		if name in book:
			print(f"{name} ning nomeri: +998", book[name])
		else:
			print("ContactBook da unday shaxs yo'q.")
	else:
		print("Salomat bo'ling.")
		break