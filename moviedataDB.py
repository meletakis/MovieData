import ConfigParser
import psycopg2
from datetime import datetime

configParser = ConfigParser.RawConfigParser()   
configParser.read('.config')
now_dt = datetime.now()

class MovieDatabase:
	def __init__(self):
		self.database = configParser.get('DB', 'database')
		self.user = configParser.get('DB', 'user')
		self.password = configParser.get('DB', 'password')
		self.host = configParser.get('DB', 'host')
		self.port = configParser.get('DB', 'port')
		self.connection = None

	def Connect(self):
		try:
			self.connection = psycopg2.connect(database=self.database,
								user=self.user, 
								password=self.password, 
								host=self.host, 
								port=self.port)
			print "Successfully connected to Movies DB"
			return True
		except psycopg2.Error:
			print "ERROR. Could not connect to databse!"
			return False

	def DisConnect(self):
		self.connection.close()
		print "Successfully dis-connected from Movies DB"

	def InsertMovie(self, movie_id, description, title, original_title):
		try:
			cursor = self.connection.cursor()
			cursor.execute("INSERT INTO movie (title, original_title, description, last_update, movie_id) \
						 VALUES (%s, %s, %s, %s, %s) \
						 ON CONFLICT (movie_id) DO UPDATE \
						 SET title = %s , original_title = %s, description = %s, last_update = %s ",  
						 (title, original_title, description, now_dt, movie_id,   # INSERT values 
						  title, original_title, description, now_dt,)			  # UPDATE values
					   ); 		 
		except psycopg2.Error as Error:
			self.connection.rollback()
			print "ERROR. Could not insert Movie to database!", Error
			return False
		else:
			self.connection.commit()
			print "Movie: " + title + " inserted to Movies DB"
			return True
 					 
	def InsertDirector(self, director_id, full_name, imdb_id):
		try:
			cursor = self.connection.cursor()
			cursor.execute("INSERT INTO director (full_name, imdb_id, last_update, director_id ) \
						 VALUES (%s, %s, %s, %s) \
						 ON CONFLICT (director_id) DO UPDATE \
						 SET full_name = %s , imdb_id = %s, last_update = %s", 
						 (full_name, imdb_id, now_dt, director_id,				# INSERT values
						  full_name, imdb_id, now_dt)							# UPDATE values
					   );
		except psycopg2.Error:
			self.connection.rollback()
			print "ERROR. Could not insert Director to database!"
			return False
		else:
			self.connection.commit()
			print "Director with imdb id: " + imdb_id + " inserted to Movies DB \n"
			return True

	def InsertMovieDirector(self, director_id, movie_id):
		try:
			cursor = self.connection.cursor()
			cursor.execute("INSERT INTO movie_director (director_id, movie_id, last_update) \
						 VALUES (%s, %s, %s) \
						 ON CONFLICT (director_id, movie_id) DO UPDATE \
						 SET last_update = %s", 
						 (director_id, movie_id, now_dt,						# INSERT values
						  now_dt) 												# UPDATE values
					   );
		except psycopg2.Error:
			self.connection.rollback()
			print "ERROR. Could not insert match Director with Movie to database!"
		else:
			self.connection.commit()

	def CleanTables(self):
		try:
			cursor = self.connection.cursor()
			cursor.execute("DELETE FROM movie_director WHERE last_update < timestamp %s",[now_dt])
			cursor.execute("DELETE FROM movie WHERE last_update < timestamp %s",[now_dt])
			cursor.execute("DELETE FROM director WHERE last_update < timestamp %s",[now_dt])
		except psycopg2.Error:
			self.connection.rollback()
			print "ERROR. Could not clean Databasse from older entries"
		else:
			self.connection.commit()
			print "Database cleaned from older entries"