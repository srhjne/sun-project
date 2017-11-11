from bs4 import BeautifulSoup
import requests
import datetime
import pickle

cme_list = []

for year in range(2013,2016):
	for month in ["01","02","03","04","05","06","07","08","09","10","11","12"]:

		main_page = requests.get("https://cdaw.gsfc.nasa.gov/CME_list/UNIVERSAL/%s_%s/univ%s_%s.html"%(year,month,year,month))

		soup = BeautifulSoup(main_page.content, 'html.parser')


		table = soup.select("table tr")
		
		for row in table[1:]:
			cme = {}
			cme_info = row.select("td")
			cme["date"] = cme_info[0].select("a")[0].text.strip()
			cme["time"] = cme_info[1].select("a")[0].text.strip()
			cme["datetime"] = datetime.datetime.strptime(cme["date"]+cme["time"],"%Y/%m/%d%H:%M:%S")
			cme["central_pa"] = cme_info[2].text.strip()
			cme["angular_width"] = int(cme_info[3].text.strip().strip(">"))
			speed = cme_info[4].text.strip()
			if speed not in ["----","---"]:
				cme["linear_speed"] = int(speed)
			se_final_height = cme_info[5].text.strip()
			if se_final_height not in ["----", "---"]:
				cme["second_order_speed_final_height"] = int(se_final_height)
			se_20Rs = cme_info[6].text.strip()
			if se_20Rs not in ["----", "---"]:
				cme["second_order_speed_20_Rs"] = int(se_20Rs)
			mass = cme_info[7].text.strip().split("*")[0]
			if mass not in ["----","---"]:
				cme["mass"] = float(mass)
			ke = cme_info[8].text.strip().split("*")[0]
			mpa = cme_info[9].text.strip().split("*")[0]
			if ke not in ["----", "---"]:
				cme["kinetic_energy"] = float(ke)
			if mpa not in ["----", "---"]:
				cme["MPA"] = float(mpa)
			cme["movies"] = cme_info[10].text.strip()
			cme["remarks"] = cme_info[11].text.strip()
			cme_list.append(cme)


pickle.dump(cme_list, open("cme_pickle.dat","w"))


	