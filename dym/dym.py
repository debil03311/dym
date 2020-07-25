#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from time import sleep, localtime
from random import randrange
from os import kill

dynmap = 'http://minecraft.naru.pro:8123/index.html?worldname=narupro&mapname=surface&zoom=1'

opt = Options()
opt.add_argument("--headless")
ff = webdriver.Firefox(options=opt)

try:
	ff.get(dynmap)
except:
	ff.quit()
	kill()

print('* Connected to dynmap, waiting...')
sleep(5)

while True:
	naptime = 2

	online_count = int(
		ff.find_element_by_css_selector(
			'.sidebar .panel .section:nth-child(odd) legend'
		).get_attribute('innerHTML') \
		 .replace('Players [','')	 \
		 .replace('/20]','')
	)

	if online_count > 0:
		naptime = randrange(20,41,5)

		lt = localtime()
		tmin = lt.tm_min
		if tmin < 10:
			tmin = "0" + str(tmin)

		filename = str(lt.tm_year) 	\
			+ '.' +str(lt.tm_mon)	\
			+ '.' +str(lt.tm_mday)
		log_players = open('logs/' filename + '.players', "a+")

		timestamp =	"[ "+str(lt.tm_year)+'/' \
			+str(lt.tm_mon)+'/'  \
			+str(lt.tm_mday)+' ' \
			+str(lt.tm_hour)+':' \
			+str(tmin)+' ]'

		online_string = '  Online: '+str(online_count)+'/20'
		print('\n' + timestamp)
		log_players.write('\n\n'+timestamp)
		print(online_string)
		log_players.write('\n'+online_string)

		for i in range(1, online_count+1):
			player = "  " + ff.find_element_by_css_selector(
				'.player:nth-child('+str(i)+') > a'
			).get_attribute('innerHTML')

			print(player)

			log_players.write('\n'+player)

			i += 1
		
		log_players.close()

	sleep(naptime)

ff.quit()