import unittest
from moviedataDB import MovieDatabase

class InsertMovieBadInput(unittest.TestCase):

	def testInsertMovieAllNull(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie(None, None, None, None)
			, msg = "testInsertMovieAllNull")
		db.DisConnect()

	def testInsertMovieWrongMovieId(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie("WrongMovieId", "Description", "Title", "Original Ttitle")
			, msg = "testInsertMovieWrongMovieId")
		db.DisConnect()

	def testInsertMovieNoneMovieId(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie(None, "Description", "Title", "Original Ttitle")
			, msg = "testInsertMovieNoneMovieId")
		db.DisConnect()

	def testInsertMovieWrongDescription(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie(1245, None, "Title", "Original Ttitle")
			, msg = "testInsertMovieWrongDescription")
		db.DisConnect()

	def testInsertMovieWrongTitle(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie(1245,"Description", None, "Original Ttitle")
			, msg = "testInsertMovieWrongTitle")
		db.DisConnect()

	def testInsertMovieWrongOriginalTitle(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertMovie(1245, "Description" , "Title", None)
			, msg = "testInsertMovieWrongOriginalTitle")
		db.DisConnect()

class InsertMovieRightInput(unittest.TestCase):

	def testInsertMovieRightInput(self):
		db = MovieDatabase()
		db.Connect()
		self.assertTrue(db.InsertMovie(1245, "Description" , "My Special Title", "Original Titke")
			, msg = "testInsertMovieRightInput")
		db.DisConnect()

class InsertDirectorBadInput(unittest.TestCase):

	def testInsertDirectorAllNull(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertDirector(None, None, None)
			, msg = "testInsertDirectorAllNull")
		db.DisConnect()

	def testInsertDirectorWrongDirectorId(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertDirector("WrongDirectorId", "Name", "IMDB")
			, msg = "testInsertDirectorWrongDirectorId")
		db.DisConnect()

	def testInsertDirectorNoneDirectorId(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertDirector(None, "Name", "IMDB")
			, msg = "testInsertDirectorNoneDirectorId")
		db.DisConnect()

	def testInsertDirectorWrongImdbId(self):
		db = MovieDatabase()
		db.Connect()
		self.assertFalse(db.InsertDirector("1245", "Name", None)
			, msg = "testInsertDirectorWrongDescription")
		db.DisConnect()

class InsertDirectorRightInput(unittest.TestCase):

	def testInsertDirectorRightInput(self):
		db = MovieDatabase()
		db.Connect()
		self.assertTrue(db.InsertDirector(1564, "Nikos Tsentis" , "nm12344")
			, msg = "testInsertDirectorRightInput")
		db.DisConnect()

	def testInsertDirectorWithoutName(self):
		db = MovieDatabase()
		db.Connect()
		self.assertTrue(db.InsertDirector(15632, None, "nm12344321")
			, msg = "testInsertDirectorRightInput")
		db.DisConnect()




def main():
    unittest.main()

if __name__ == '__main__':
    main()