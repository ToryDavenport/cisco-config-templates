from jinja2 import Environment, FileSystemLoader
import pandas as pd
import xlrd
import os

file_loader = FileSystemLoader('.')
file_path = "./Infastructure_Information.xlsx"

data = pd.read_excel(file_path)
interfaces = data['Interface:']
ips = data['IP:']
hostname = data['Hostname:']


for device in range(0,25):
	os.system(f"touch ./configs/output/config_{hostname[device]}.cfg")
	file = open(f"./configs/output/config_{hostname[device]}.cfg", "w")
	env = Environment(loader=file_loader)
	template = env.get_template('./configs/Gold_Standard.txt')
	file.write(template.render(hostname=hostname[device], interface=interfaces[device], ip=ips[device]))
	file.close()

