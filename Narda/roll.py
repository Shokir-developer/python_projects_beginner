import random
import time
max = 6
min = 1

yana = True

while yana:
	print("Tosh tashlanayapdi ...")
	print("Natijalar ... ")
	time.sleep(1)
	print(random.randint(min, max))
	print(random.randint(min, max))

	yana = int(input("Yana o'ynashni xohlaysizmi [ha(1) yoki yoq(0)]: "))
