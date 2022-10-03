from __future__ import with_statement
import contextlib
try:
	from urllib.parse import urlencode
except ImportError:
	from urllib import urlencode
try:
	from urllib.request import urlopen
except ImportError:
	import urllib.request as urllib2 #change 1

file_object = open('shortenedurlfiles.txt', 'a')

def make_tiny(url):
	request_url = ('http://tinyurl.com/api-create.php?' +
	urlencode({'url':url}))
	with contextlib.closing(urlopen(request_url)) as response:
		return response.read().decode('utf-8')

def filereader():
	f = open("urlfiles.txt", "r")
	urllist = f.read().split()
	return urllist

def fileopener(url):
	global  file_object
	file_object.write(url+"\n")

def main():
	urllist=filereader()
	print("Shortened URLs")
	for url in urllist:
		fileopener(make_tiny(url))
		print(make_tiny(url))
			# print(tinyurl)
	global file_object
	file_object.close()
if __name__ == '__main__':
	main()