from collections import Counter

def most_popular_json(file_path):
	import json
	with open(file_path, encoding='utf-8') as newsafr:
		json_data = json.load(newsafr)
	json_descriptions = list()
	for json_item in json_data['rss']['channel']['items']:
		json_description = list(json_item['description'].split(' '))
		json_descriptions += json_description
	json_six_letters_words = list()
	for json_word in json_descriptions:
		if len(json_word) > 6:
			json_six_letters_words.append(json_word)
		else:
			pass
	json_top10 = Counter(json_six_letters_words).most_common(10)
	print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для json:')
	for i, json_unit in enumerate(json_top10):
		print(i+1, json_unit[0],'\n')



def most_popular_xml(file_path):
	import xml.etree.ElementTree as ET
	parser = ET.XMLParser(encoding = 'utf-8')
	tree = ET.parse(file_path, parser)
	root = tree.getroot()
	xml_descriptions = root.findall('channel/item/description')
	xml_description_list = list()
	for xml_item in xml_descriptions:
		xml_description = list(xml_item.text.split(' '))
		xml_description_list += xml_description
	xml_six_letters_words = list()
	for xml_word in xml_description_list:
		if len(xml_word) > 6:
			xml_six_letters_words.append(xml_word)
		else:
			pass
	xml_top10 = Counter(xml_six_letters_words).most_common(10)
	print('Топ 10 самых часто встречающихся в новостях слов длиннее 6 символов для xml:')
	for i, xml_unit in enumerate(xml_top10):
		print(i+1, xml_unit[0], '\n')

most_popular_json('newsafr.json')
most_popular_xml('newsafr.xml')
