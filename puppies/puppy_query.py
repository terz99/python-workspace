# File import starts here
import os
import sys
import datetime
from sqlalchemy import func
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from puppies import Base, Shelter, Puppy
# File import ends here



# Session creation starts here
engine = create_engine("sqlite:///puppyshelter.db")
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# Session creation ends here

def query_one():

	""" This query gets all the puppies from
	puppyshelter.db and prints their names """

	print("Query one initialized...")
	query_result = session.query(Puppy.name)\
		.order_by(Puppy.name.asc())\
		.all()

	print("Query one successful...")
	for puppy in query_result:
		print(puppy.name)

def query_two():

	""" This function queries all the puppies that
	are less than 6 months old and orders them
	by the youngest first """

	print("Query two initialized...")
	six_months_ago = None
	# Getting today's date 
	today = datetime.date.today()
	# See if the current date minus six months goes through a leap date 
	if passes_leap_year(today): 
		print("{} is a leap year, continuing...".format(today.year))
		six_months_ago = today - datetime.timedelta(days=183)
	else:
		print("{} is not a leap year, continuing...".format(today.year))
		six_months_ago = today - datetime.timedelta(days=182)

	print("Six months ago was the date {}".format(six_months_ago))
	print("Starting query...")
	query_result = session.query(Puppy.name, Puppy.dateOfBirth)\
		.filter(Puppy.dateOfBirth >= six_months_ago)\
		.order_by(Puppy.dateOfBirth.desc()).all()
	
	print("Query successful, printing results:")
	for elem in query_result:
		print(elem.name, elem.dateOfBirth)

def query_three():

	""" This function queries all the puppies 
	and organizes them by their weight in ascending order """

	print("Query three initialized...")
	query_result = session.query(Puppy.name, Puppy.weight)\
		.order_by(Puppy.weight.asc())\
		.all()

	print("Query successful, printing results:")
	for elem in query_result:
		print(elem.name, elem.weight)

def query_four():

	""" This function queries all the puppies and groups them by shelters """

	print("Query four initialized...")
	query_result = session.query(Shelter.name, func.count(Puppy.id))\
		.join(Puppy)\
		.group_by(Shelter.id)\
		.all()

	print("Query successful, printing results:")
	for elem in query_result:
		print(elem.name, elem[1])



# Helper methods
def passes_leap_year(today):

	""" This method checks if the interval of 
	six months ago and today goes through a leap day """

	current_year = today.year
	if is_leap_year(current_year):
		six_months_ago = today - datetime.timedelta(days=183)
		leap_day = datetime.date(current_year, 2, 29)
		return leap_day >= six_months_ago
	else:
		return False

def is_leap_year(current_year):

	""" This method checks if this is a leap year """	
	if current_year%4 != 0:
		return False
	elif current_year%100 != 0:
		return True
	elif current_year%400 != 0:
		return False
	else:
		return True

print("Testing query one...")
query_one()
print("Query one successful...")
print("------------------------------")

print("Testing query two...")
query_two()
print("Query two successful...")
print("------------------------------")

print("Testing query three...")
query_three()
print("Query three successful...")
print("------------------------------")

print("Testing query four...")
query_four()
print("Query four successful...")
