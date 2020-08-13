import os

for devices in range(0,22):
	os.system(f"ping 172.16.99.{devices+1} -c 4 >> report.txt")
	print("please wait while we test connectivity to devices..")
	os.system("sleep 5")

