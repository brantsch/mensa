from traceback import print_exc as traceback_print_exc
from bs4 import BeautifulSoup
from bs4 import element as bs4_element
from .dish import dish
from .menu import menu
from datetime import date
import re

date_rgx = re.compile("\s*\D*(\d*)\.(\d*)\.\?")

def parse(data):
	soup = BeautifulSoup(data.encode(encoding="latin_1",errors="ignore"))
	tbody = soup.body.table.tbody
	# extract the relevant table from HTML
	table = []
	for tr in tbody.children:
		row = []
		try:
			if isinstance(tr,bs4_element.Tag):
				for td in tr.children:
					if isinstance(td,bs4_element.Tag):
						tdstr = ' '.join(td.strings)
						if tdstr:
							row.append(tdstr.strip())
				if any(row):
					table.append(row)
		except:
			traceback_print_exc()
	# walk the table
	for row in table:
		print(row)
