from sunpy.io import fits
import os
import datetime
import pickle

cme_list = pickle.load(open("cme_pickle.dat","rb"))

def read_data(year,month, day):
	for file in os.listdir("/media/sarah/SAMSUNG/ml_sun_images/"):
		if file.startswith("aia_lev1_171a_{year}_{month}_{day}t".format(year=year,month=month,day=day)):
			filename = "/media/sarah/SAMSUNG/ml_sun_images/"+file
			data = fits.read(filename)


			image = data[1][0][::32,::32]

			date_string = data[1][1]["DATE-OBS"]

			date = datetime.datetime.strptime(date_string[:-3],"%Y-%m-%dT%H:%M:%S")

			for cme in cme_list:
				if cme["datetime"]>date:
					next_cme = cme
					break

			time_to_next_cme = next_cme["datetime"] - date

			return {"image":image, "date":date, "time_to_next_cme":time_to_next_cme}

def read_all_data():
	data = []
	for year in ["2013","2014"]:
		for month in range(1,13):
			month_string = str(month).zfill(2)
			for day in range(1,32):
				day_string = str(day).zfill(2)
				print year, month, day
				daily_data = read_data(year,month_string,day_string)
				if daily_data:
					data.append(daily_data)

	return data


data = read_all_data()


pickle.dump(data,open("all_data_pickle.dat","w"))