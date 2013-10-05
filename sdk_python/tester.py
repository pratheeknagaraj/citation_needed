from __future__ import print_function
from alchemyapi import AlchemyAPI
import json

demo_text = 'The protocol\'s principle \"common but differentiated responsibilities\" is targeted to indicate that industrial activity in developed nations is largely responsible for the common issue of climate change and thus the responsibility burden is targeted at such nations'

alchemyapi = AlchemyAPI()

print('')
print('')
print('############################################')
print('#   Entity Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.entities('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Entities ##')
	for entity in response['entities']:
		print('text: ', entity['text'])
		print('type: ', entity['type'])
		print('relevance: ', entity['relevance'])
		print('sentiment: ', entity['sentiment']['type'] + ' (' + entity['sentiment']['score'] + ')')
		print('')
else:
	print('Error in entity extraction call: ', response['statusInfo'])


'''
print('')
print('')
print('')
print('############################################')
print('#   Sentiment Analysis Example             #')
print('############################################')
print('')
print('')

print('Processing html: ', demo_html)
print('')

response = alchemyapi.sentiment('html',demo_html)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Document Sentiment ##')
	print('type: ', response['docSentiment']['type'])
	print('score: ', response['docSentiment']['score'])
else:
	print('Error in sentiment analysis call: ', response['statusInfo'])

'''

print('')
print('')
print('')
print('############################################')
print('#   Keyword Extraction Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.keywords('text',demo_text, { 'sentiment':1 })

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Keywords ##')
	for keyword in response['keywords']:
		print('text: ', keyword['text'])
		print('relevance: ', keyword['relevance'])
		print('sentiment: ', keyword['sentiment']['type'] + ' (' + keyword['sentiment']['score'] + ')')
		print('')
else:
	print('Error in keyword extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Concept Tagging Example                #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.concepts('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Concepts ##')
	for concept in response['concepts']:
		print('text: ', concept['text'])
		print('relevance: ', concept['relevance'])
		print('')
else:
	print('Error in concept tagging call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Relation Extraction Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.relations('text',demo_text)

if response['status'] == 'OK':
	print('## Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Relations ##')
	for relation in response['relations']:
		if 'subject' in relation:
			print('Subject: ', relation['subject']['text'] )
		
		if 'action' in relation:
			print('Action: ', relation['action']['text'])
		
		if 'object' in relation:
			print('Object: ', relation['object']['text'])
		
		print('')
else:
	print('Error in relation extaction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Text Categorization Example            #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.category('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Category ##')
	print('text: ', response['category'])
	print('score: ', response['score'])
	print('')
else:
	print('Error in text categorization call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Language Detection Example             #')
print('############################################')
print('')
print('')

print('Processing text: ', demo_text)
print('')

response = alchemyapi.language('text',demo_text)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))


	print('')
	print('## Language ##')
	print('language: ', response['language'])
	print('iso-639-1: ', response['iso-639-1'])
	print('native speakers: ', response['native-speakers'])
	print('')
else:
	print('Error in language detection call: ', response['statusInfo'])


'''
print('')
print('')
print('')
print('############################################')
print('#   Author Extraction Example              #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.author('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Author ##')
	print('author: ', response['author'])
	print('')
else:
	print('Error in author extraction call: ', response['statusInfo'])



print('')
print('')
print('')
print('############################################')
print('#   Feed Detection Example                 #')
print('############################################')
print('')
print('')

print('Processing url: ', demo_url)
print('')

response = alchemyapi.feeds('url',demo_url)

if response['status'] == 'OK':
	print('## Response Object ##')
	print(json.dumps(response, indent=4))

	print('')
	print('## Feeds ##')
	for feed in response['feeds']:
		print('feed: ', feed['feed'])
else:
	print('Error in feed detection call: ', response['statusInfo'])

print('')
print('')
'''

