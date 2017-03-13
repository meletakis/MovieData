import unittest
from moviedataAPI import MoviesNowPlaying, MovieDirectors

class MoviesNowPlayingRightInput(unittest.TestCase):

	#Working but it takes a lot time getting all movies
	# def testMoviesNowPlayingNoCode(self): 
	# 	self.assertTrue(MoviesNowPlaying(), msg = "testMoviesNowPlayingNoCode")

	def testMoviesNowPlayingGreeceCode(self):
		self.assertTrue(MoviesNowPlaying("GR"), msg = "testMoviesNowPlayingGreeceCode")

class MoviesNowPlayingBadInput(unittest.TestCase):

	def testMoviesNowPlayingWrongRegionCode(self):
		self.assertFalse(MoviesNowPlaying("GREECE"), msg = "testMoviesNowPlayingWrongRegionCode")

	def testMoviesNowPlayingWrongNumber(self):
		self.assertFalse(MoviesNowPlaying("12345"), msg = "testMoviesNowPlayingWrongNumber")

class MovieDirectorsRightInput(unittest.TestCase):
	
	def testMovieDirectors5digitCode(self):
		self.assertTrue(MovieDirectors(14564), msg = "MovieDirectors5digitCode")

	def testMovieDirectors6digitCode(self):
		self.assertTrue(MovieDirectors(14564), msg = "MovieDirectors7digitCode")
		
class MovieDirectorBadInput(unittest.TestCase):

	def testMovieDirectorsNoCode(self):
		self.assertFalse(MovieDirectors(), msg = "MovieDirectorsNoCode")

	def testMovieDirectorsWrongCode(self):
		self.assertFalse(MovieDirectors(00), msg = "MovieDirectorsWrongCode")

def main():
    unittest.main()

if __name__ == '__main__':
    main()