
'''
			Based on Hackerrank challenge 
Script to retrieve movie titles containing certain sub string

'''

import json,urllib

def  getMovieTitles(substr):
	
	'''
		Utility function to get names of movies
			input : substr -- name to be found
			output : names of movies containing substr in ascending order
			
			description:
				Fetch the url for the movie name and identify the number of
				pages returned
				For each page get all the names of the movies
				Sort all the names captured
	'''
	print 'Fetching titles containing', substr
	link = 'https://jsonmock.hackerrank.com/api/movies/search/?Title='
	pageNum=1; 
	try:
		url = link + substr + "&page=" + str(pageNum)
		response = json.loads(urllib.urlopen(url).read())
		total_pgs = response['total_pages']
		if total_pgs > 1: # if more than one page returned loop over all to get names
			titles=set(movie[ 'Title' ].encode('utf-8') for movie in response[ 'data' ]  )
			for i in range(2,total_pgs+1): # from pg2 to end get all titles
				url_new = link + substr + "&page=" + str(i)
				response_new = json.loads(urllib.urlopen(url_new).read())
				titles.update(set(movie[ 'Title' ].encode('utf-8') for movie in response_new[ 'data' ])) # update with titles from this page
			print total_pgs,'pages with',len(titles), 'records found'
			print sorted(titles,key=str.lower)
		elif total_pgs == 1:
			titles = set(movie[ 'Title' ].encode('utf-8') for movie in response[ 'data' ])
			print total_pgs,'page with',len(titles), 'record(s) found'
			print sorted(titles,key=str.lower)
		elif 'data' not in response:
			print "no 'data' packet found for the movie" 
	except:
		print "no matches found"
		
if __name__ == '__main__':
	substring = str(raw_input('Please enter the substring\n') or 'a')
	getMovieTitles(substring)
