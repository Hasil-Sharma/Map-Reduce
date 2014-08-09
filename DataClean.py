class DataClean:
	def __init__(self,scraperClass):
		self.final_cleaned_data = self.getFinalData(scraperClass.getFinalData())

	def getFinalData(self,elements):
		data = []
		for string in elements:
			words = string.split()
			for word in words:
				word = ''.join(e.lower() for e in word if e.isalpha())
				if len(word) > 2:
					data.append(word)
		return data

	def printFinalData(self):
		for string in self.final_cleaned_data:
			print string

	def getFinal(self):
		return self.final_cleaned_data
