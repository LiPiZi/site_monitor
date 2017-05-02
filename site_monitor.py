from bs4 import BeautifulSoup
import requests
import time
import difflib

url = raw_input("Enter website to monitor: ")

t = int(raw_input("Wait time: "))
def bodyonly(code):
	soup = BeautifulSoup(code, "html.parser")
	body = soup.find('body')
	contents = body.findChildren()
	webContent = contents
	return webContent
def main():
	while True:
		r1  = requests.get(url)
		data1 = r1.text
		soup1 = bodyonly(data1)
		#soup1 = BeautifulSoup(data1, "html.parser")
		#r1.cookies['example_cookie_name']

		time.sleep(t)

		r2  = requests.get(url)
		data2 = r2.text
		soup2 = bodyonly(data2)
		#soup2 = BeautifulSoup(data2, "html.parser")
		#r2.cookies['example_cookie_name']

		if soup1 == soup2:
			print("No change")
		else:
			l1 = str(soup1).lower().split()
			l2 = str(soup2).lower().split()
			s1 = ""
			s2 = ""
			for i in l1:
			  if i not in l2:
				s1 = s1 + " " + i 
			for j in l2:
			  if j not in l1:
				s2 = s2 + " " + j 

			new = s1 + " " + s2
			print new
if __name__ == "__main__":
	main()
