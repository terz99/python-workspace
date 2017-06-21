# File configuration starts
import os
import sys

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()
# File configuration ends



# Class declaration starts
# These classes represent tables in the database("restaurantmenu.db")
class Restaurant(Base):

	# Table information, the name of the table
	__tablename__ = "restaurant"

	# Table structure
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)

class MenuItem(Base):

	# The name of the table
	__tablename__ = "menu_item"

	# Table structure
	name = Column(String(80), nullable=False)
	id = Column(Integer, primary_key=True)
	course = Column(String(250))
	description = Column(String(250))
	price = Column(String(8))
	restaurant_id = Column(Integer, ForeignKey("restaurant.id"))
	restaurant = relationship(Restaurant)
# Class declaration ends



# Engine configuration starts
engine = create_engine("sqlite:///restaurantmenu.db")
Base.metadata.create_all(engine)
# Engine configuration ends
