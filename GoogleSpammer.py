import requests						#To POST the spams		
import random 						#To randomise the spams
from bs4 import BeautifulSoup				#For scraping the captch
import ctypes						#For minimising the window


#This is to minimise the window after execution
ctypes.windll.user32.ShowWindow( ctypes.windll.kernel32.GetConsoleWindow(), 6 )



#Target form URL
requestURL = 'https://docs.google.com/forms/d/e/1FAIpQLScfq3qfsz6TbLxPlZwhvtiLQx1e8e6-NGPazAj0WsrZRs_eTA/formResponse' 

#Target url to get captcha, comment out if there's no captcha in form
bsURL = 'https://docs.google.com/forms/d/e/1FAIpQLScfq3qfsz6TbLxPlZwhvtiLQx1e8e6-NGPazAj0WsrZRs_eTA/viewform' 



# Open the file that contains the words to use for random generated spam and randomise them, uncomment if you wanna use it

#def randomise():
#	file = open(r'C:\Users\kaush\Desktop\confession.txt', 'r') #file location
#	splitted = file.read().split(' ')
#	random.shuffle(splitted)
#	confess = ''
#	for i in range(100):
#		confess += ' '+ splitted[i]
#	return confess


#Function to get Captcha
def getCaptch():
	source = requests.get(bsURL).text
	soup = BeautifulSoup(source,'lxml')
	codeBlock = soup.find_all('div',class_='freebirdFormviewerViewItemsItemItemTitle exportItemTitle freebirdCustomFont')[6].text       #Change the index number according the form
	code = codeBlock.split(' ')[2]
	return code



formFilled = 0																#To count number of spam


while True:
	payload = {'entry.1696974207' : 'This is a test confession',							#Change the entry.x to match the form you are spamming
			   'entry.1624638507' : 'Morning',
			   'entry.1428141631' : 'Male',
			   'entry.508523218' : '2075/2076',
			   'entry.1367250609' : 'Leibnitz',
			   'entry.823420472' : getCaptch()}

	with requests.Session() as session:										#Spamming the form
		post = session.post(requestURL, data = payload)


	

	formFilled += 1
	prompt = 'Number of times Form has been filled: ' + str(formFilled+1)                                                                                                           
	print(prompt,'\n')

	for i in payload.items():                                                                                       #Shows the spam response
		print(i[1],'\n')

	print('\n\n\n\n\n')
