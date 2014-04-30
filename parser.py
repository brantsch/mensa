from bs4 import BeautifulSoup
from .dish import dish
from .menu import menu
from datetime import date
import re

date_rgx = re.compile("\D*(\d*)\.(\d*)\.")

def parse(data):
	soup = BeautifulSoup(data.encode(encoding="latin_1",errors="ignore"))
	tbody = soup.body.table.tbody
	cur_date = None
	for tr in tbody.children:
		try:
			#tds = list(tr.children)
			for td in tr.children:
				print(td.string,end="")
				dishes.append(dish(
			print('----------------',end="")
		except: pass
		#menu.append(dish(*(tr.children)))
	#menu = list(soup.body.table.tbody.children)
	return menu
