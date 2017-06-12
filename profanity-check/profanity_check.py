from urllib.request import FancyURLopener

class MyOpener(FancyURLopener):
	version = 'Dushan'

def read_text():
	file = open('movie_quotes.txt', 'r')
	content_of_file = file.read()
	file.close()
	profanity_check(content_of_file)

def profanity_check(text):
	opener = MyOpener()
	connection = opener.open('http://www.wdylike.appspot.com/?q='+text)
	response = str(connection.read())
	if 'true' in response:
		print('There is a curse word!!')
	elif 'false' in response:
		print('There is NO curse word.')
	else:
		print('Could not connect with www.wdylike.appsot.com')

read_text()