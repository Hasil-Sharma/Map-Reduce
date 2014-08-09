class DataCreate:
	dataScraper = __import__('DataScraper')
	dataClean = __import__('DataClean')
	
	def __init__(self,url):
		scrape = self.dataScraper.DataScraper(url)
		self.finalWords = self.dataClean.DataClean(scrape).getFinal()

	def getFinal(self):
		return self.finalWords
