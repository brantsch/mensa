from traceback import print_exc as traceback_print_exc
from bs4 import BeautifulSoup
from bs4 import element as bs4_element
from .dish import dish
from .menu import menu
from datetime import date
import re

date_rgx = re.compile("\D*(\d*)\.(\d*)\.?")

def parse(data):
	soup = BeautifulSoup(data.decode(encoding="latin_1",errors="ignore"))
	# extract the relevant table from HTML
	table = []
	for tr in soup.body.table.select("tr"):
		try:
			row = []
			for td in tr.select("td"):
				for sup in td.find_all("sup"):
					sup.extract()
				for br in td.find_all("br"):
					br.extract()
				text = td.text.strip()
				text = text.replace('\r\n','')
				
				# convert the 'V+' icon to ascii
				img = td.img
				if img and img['alt'] == "vegan":
					text = "V+"
				
				row.append(text)
				#if text:
				#	print(repr(text))
			if any(row): #prevent empty rows
				table.append(row)
		except:
			traceback_print_exc()

	# walk the table, create dish objects and add them to the menu
	themenu = menu()
	del table[0] #discard the first row which contains no actual information
	# Not only are those goons too daft to present their data in any other form
	# than HTML, they aren't even using a table header! m(
	cur_date = None
	for row in table:
		del row[1]
		if row[0]:
			day, month = date_rgx.match(row[0]).groups()
			cur_date = date(date.today().year,int(month),int(day))
		a_dish = dish(cur_date,*row[1:])
		themenu.append(cur_date,a_dish)
	return themenu
