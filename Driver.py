from DataCreate import DataCreate
from collections import Counter
from pymongo import MongoClient
import json

f = open('input.txt')
urls = f.read().split()

def getWords(url):
	words = DataCreate(url).getFinal()
	return words

def getSource(urls):
	source = dict()
	for url in urls:
		for word in getWords(url):
			if word in source:
				source[word].append(url.replace('.','_'))
			else:
				source[word] = [url.replace('.','_')]
			#replacement because keys in mongodb cannot store '.'
	return source

source = getSource(urls)
client = MongoClient()
db = client.mapreduce
posts = db.invertedindex

def final(key,value):
	val = dict()
	val['word'] = value[0]
	val['urls'] = value[1]
	post_id = posts.insert(val)
	print post_id

def mapfn(key,value):
#key is the word and value is the url from which it was fetched
#Mapping and combining in single step
	yield key,dict(Counter(value))

def reducefn(key,value):
#key is the word and value is the list of the items returned by
#mapfn after they have been combined
	return key,value[0]






