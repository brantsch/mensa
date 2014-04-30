#!/usr/bin/env python3

import re
from sys import path
import os
path.append(os.getcwd()+"/..")
from util import fetch
from mensa.parser import parse

#def parse(string):
#	string = re.sub(r"\r|\n","",string)
#	string = re.sub(r"&nbsp;"," ",string)
#	tbl_rgx = re.compile(r"<table.*?><tbody>(.*?)</tbody>.*?</table>")
#	tbl_match = tbl_rgx.search(string)
#	tbl = tbl_match.group(1)
#	rows = []
#	for line in re.split(r"<tr>|</tr>",tbl):
#		if line:
#			row = []
#			for cell in re.split(r"<td>|</td>",line):
#				if cell:
#					row.append(cell)
#			rows.append(row)
#	return rows

def main():
	#res = parse(fetch())
	with open("speiseplan_beispiel.html","rb") as data:
		html = str(data.read(),encoding="latin_1",errors="ignore")
		res = parse(html)
		#return(res)
		#for row in res:
		#	print(row)

if __name__ == "__main__":	
	main()
