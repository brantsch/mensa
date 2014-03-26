import html.parser
import html.entities
from .dish import dish
from .menu import menu
from datetime import date
import re

date_rgx = re.compile("\D*(\d*)\.(\d*)\.")

def parse(data):
	mp = MensaParser()
	mp.feed(data.decode(encoding="latin_1",errors="ignore"))
	return mp.menu

class MensaParser(html.parser.HTMLParser):
	def __init__(self):
		super(MensaParser,self).__init__()

	def reset(self):
		super(MensaParser,self).reset()
		self.current_row = None
		self.in_row = False
		self.cur_item = ""
		self.tbl_cnt = 0
		self.row_cnt = 0
		self.cur_date = ""
		self.menu = menu()

	def handle_starttag(self,tag,attrs):
		if tag == "table":
			self.tbl_cnt += 1
		if self.tbl_cnt == 1: 
			if tag == "tr":
				self.in_row = True
				self.row_cnt += 1
				self.current_row = []
			if self.in_row and tag == "td":
				self.cur_item = ""
		
	def handle_endtag(self,tag):
		if self.in_row and tag == "td":
			self.current_row.append(self.cur_item)
		if tag == "tr":
			self.current_row = list(map(lambda x: x.strip(),self.current_row))
			if self.current_row[0]:
				self.cur_date = self.current_row[0]
			else:
				self.current_row[0] = self.cur_date
			del self.current_row[1]
			if self.current_row[2]:
				try:
					day, month = date_rgx.match(self.current_row[0]).groups()
					the_date = date(date.today().year,int(month),int(day))
					cur_dish = dish(the_date,*self.current_row[1:])
					self.menu.append(the_date,cur_dish)
				except ValueError:
					pass
		if self.tbl_cnt == 1 and tag == "table":
			def nop(*unused):
				pass
			self.handle_starttag = nop
			self.handle_endtag = nop
			self.handle_data = nop

	def handle_data(self,data):
		if self.in_row:
			self.cur_item += data

	def handle_entityref(self, name):
		if self.in_row:
			c = chr(html.entities.name2codepoint[name])
			self.cur_item += c

	def handle_charref(self, name):
		if self.in_row:
			if name.startswith('x'):
				c = chr(int(name[1:], 16))
			else:
				c = chr(int(name))
			self.cur_item += c
