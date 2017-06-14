# "Database code" for the DB Forum.

import datetime
import psycopg2
import bleach

def get_posts():
	"""Return all posts from the 'database', most recent first."""
	db_connection = psycopg2.connect("dbname=forum")
	cursor = db_connection.cursor()
	query = "select content, time from posts order by time desc;"
	cursor.execute(query)
	# posts = [{"content": str(row[1]), "time": str(row[0])} for row in cursor.fetchall()]
	posts = cursor.fetchall()
	db_connection.close()
	return posts

def add_post(content):
	""" Inserts a new post into the forum database """
	db_connection = psycopg2.connect("dbname=forum")
	cursor = db_connection.cursor()

	query = "insert into posts (content) values (%s);"
	cursor.execute(query, (content,))
	db_connection.commit()
	db_connection.close()


