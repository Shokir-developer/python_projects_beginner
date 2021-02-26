import time
from datetime import datetime as dt

hostsPath = r"C:\Windows\System32\drivers\etc\hosts"
redirect = "127.0.0.1"

websites = ["www.voydod.com", "voydod.com"]
i = 1
while i > 0:
	if dt(dt.now().year,dt.now().month,dt.now().day,9) < dt.now() < dt(dt.now().year,dt.now().month,dt.now().day,18):
		print("Sorry not allowed")
		with open(hostsPath, "r+") as file:
			content = file.read()
			for site in websites:
				if site in content:
					pass
				else:
					file.write(redirect + " " + site + "\n")
	else:
		print("Allowed access")

	i -= 1
time.sleep(2)
