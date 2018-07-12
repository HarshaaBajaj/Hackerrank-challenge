import json
from urllib.request import urlopen

def  get_country_count(substr,p):
	'''
		Description:
			Utility function to count the number of countries whose name contains substr with population >= p
		Input : 
			substr -- substring to be checked for in country names
			p -- population condition
		Output : 
			count of countries with population >=p
	'''
	link = 'https://jsonmock.hackerrank.com/api/countries/search?name='
	total_pgs = 1; count = 0
	url = link + substr + "&page=" + str(total_pgs)
	response = json.loads(urlopen(url).read().decode('utf8'))
	if len(response['data']) < 1:	return print('no matches')
	total_pgs = response['total_pages']
	while total_pgs != 0 :
		if total_pgs != 1:
			url = link + substr + "&page=" + str(total_pgs)
			response = json.loads(urlopen(url).read().decode('utf8'))
		count += sum(map(lambda x : 1 if x['population']>=p else 0,response['data']))
		total_pgs -= 1
	return print(count)
		
if __name__ == '__main__':
	tokens = (input('Please enter the substring and population separated by space\n') or 'un 100').split()
	get_country_count(tokens[0],int(tokens[1]))