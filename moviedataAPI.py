import ConfigParser
import json
import urllib, urllib2

configParser = ConfigParser.RawConfigParser()   
configParser.read('.config')

api_key = "?api_key=" + configParser.get('API', 'key')
url_prefix = "https://api.themoviedb.org/3/"

def Request(url_body, parameters=''):
	try:
		url = url_prefix + url_body + api_key + "&" + urllib.urlencode(parameters) 
		return json.load(urllib2.urlopen(url))
	except (urllib2.HTTPError, ValueError):
		print "ERROR in processing HTTP Request"
		return False

def MoviesNowPlaying(region=''):
	
	movies_now_playing = Request("movie/now_playing", {"region": region})
	if movies_now_playing and movies_now_playing['total_results']:		# if API call returned results (both HTTPError and ValueError)
		print "Getting Movies Now Playing from themoviedb API. \n"
		total_pages = movies_now_playing['total_pages'] 
		if total_pages > 1: 						# if resultset has more than one page
			for page in range(2, total_pages+1):	# get all pages
				movies_now_playing_temp = Request("movie/now_playing", {"region": region, "page": page})
				movies_now_playing['results']+=movies_now_playing_temp['results'] 	# concatanate list with results 
		return movies_now_playing['results']
	else:
		return None

def PersonDetails(person_id=None):

	if not person_id:
		return None
	
	person_details = Request("person/" + str(person_id))
	if person_details:
		return { "person_id" : person_id, "full_name": person_details['name'], "imdb_id": person_details['imdb_id'] }  
	else:
		return None

def MovieDirectors(movie_id=None):

	if not movie_id:
		return None

	movie_credits = Request("movie/" + str(movie_id) + "/credits")
	if not movie_credits:
		return None

	directors = []
	for crew in movie_credits['crew']:
		if crew['job'] == "Director":
			director_details = PersonDetails(crew['id'])
			if director_details:
				directors.append(director_details)
	return directors

