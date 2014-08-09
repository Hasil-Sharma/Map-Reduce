class DataScraper:
	urllib = __import__('urllib')
	re = __import__('re')
	BeautifulSoup = __import__('bs4')
	
	def __init__(self,url):
		self.final_data = self.getTextOnly(url)

	def visible(self,elm):
		if elm.parent.name in ['style','script','[document]','head','title']:
			return False
		elif self.re.match('<!--.*-->', elm.encode('utf-8','ignore')):
			return False
		return True

	def getTextOnly(self,url):
		html = self.urllib.urlopen(url)
		#html = open(url)
		soup = self.BeautifulSoup.BeautifulSoup(html)
		texts = soup.findAll(text = True)
		return filter(self.visible,texts)

	def getFinalData(self):
		new = []
		for text in self.final_data:
			if text.strip():
				new.append(text.strip())
		return new

	def cleanedText(self):
		for text in self.final_data:
			if text.strip():
				print text
