import requests, os, random
from bs4 import BeautifulSoup



import ctypes
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )

requestURL = 'https://docs.google.com/forms/d/e/1FAIpQLSc7hihrQSWh99sp9rUEgpZC4fNToXKOSf4NToH140bmTWn8fg/formResponse' #Target form URL
bsURL = 'https://docs.google.com/forms/d/e/1FAIpQLSc7hihrQSWh99sp9rUEgpZC4fNToXKOSf4NToH140bmTWn8fg/viewform'



f = open(r'C:\Users\kaush\Desktop\confession.txt', 'r')
r = f.read().split(' ')






















times = 0
while True:
	source = requests.get(bsURL).text
	soup = BeautifulSoup(source,'lxml')
	codeBlock = soup.find_all('div',class_='freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont')[5]
	codeBlock=codeBlock.text
	codeBlock = codeBlock.split(' ')
	code = codeBlock[2]
	print(code)


	random.shuffle(r)
	confess = ''
	for i in range(50):
		confess += ' '+ r[i]


	payload = {'entry.1362576193' : 'Dear❤️' + confess,
			   'entry.624385418' : 'Morning',
			   'entry.333920323' : 'Male',
			   'entry.485068538' : '2075/2076',
			   'entry.59965412' : 'Leibnitz',
			   'entry.474259843' : code}





	times += 1

	prompt = 'Number of times Form has been filled: ' + str(times+1)	
	with requests.Session() as session:
		post = session.post(requestURL, data = payload)

	print(prompt)
	for i in payload.items():
                print(i[1])
