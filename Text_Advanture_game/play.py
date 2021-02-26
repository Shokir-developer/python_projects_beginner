import time

answer = input("Text Advanture Game o'yinini o'ynaymizmi [ha/yoq]: ").lower().strip()

if answer == "ha":
	answer = input("Siz hozir chorraxadasiz. Yo'nalish tanlang [ong/chap]: ").lower().strip()
	time.sleep(2)

	if answer == "chap":
		
		answer = input("Oldingizdan maxluq chiqdi, nima qilasiz [xujum/qochish]: ").lower().strip()

		if answer == "xujum":
			print("Bu yaxshi tanlov emas edi. Siz yutqazdingiz.")
		elif answer == "qochish":
			print("Yaxshi tanlov, siz o'zingizni asradingiz.")
			time.sleep(2)

			answer = input("Qochish uchun qanday vosita tanlaysiz [samalyot/mashina]: ").lower().strip()

			if answer == "samalyot":
				print("Afsuski samalyot boshqara olmaysiz ... Maxluq yetib oldi. Siz yutqazdingiz")
			elif answer == "mashina":
				print("Yaxshi tanlov. Siz yutdingiz.")
			else:
				print("Invali code. You lost")
				quit()

	elif answer == "ong":
		print("Siz jarlikka tushdingiz va yutqazdingiz")

	else:
		print("Invali code. You lost")
		quit()

elif answer == "yoq":
	print("Ko'rishguncha")

else:
	print("Invali code. You lost")
	quit()

