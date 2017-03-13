from moviedataAPI import MoviesNowPlaying, MovieDirectors
from moviedataDB import MovieDatabase

db = MovieDatabase()
if db.Connect():
	movies = MoviesNowPlaying("GR")
	if movies:	# if API returned movies list
		for movie in movies:
			if db.InsertMovie(movie['id'], movie['overview'], movie['title'], movie['original_title']):
				directors = MovieDirectors(movie['id'])

				if directors: # if API returned directors list
					for director in directors:
						if db.InsertDirector(director['person_id'], director['full_name'], director['imdb_id']):
							db.InsertMovieDirector(director['person_id'], movie['id'])
		db.CleanTables()
	else:
		print"ERROR! It was impossible to obtain movies"

	db.DisConnect()