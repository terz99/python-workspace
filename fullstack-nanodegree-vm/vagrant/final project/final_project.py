# File import starts here
from flask import Flask, render_template, url_for, request, redirect, flash
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem
# File import ends here


# Flask config
app = Flask(__name__)


# DB config starts here
engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
# DB config ends here


@app.route('/')
@app.route('/restaurants')
def restaurants():
	""" This function shows all the restaurants in the database """

	# Query all the restaurants and render them with html template 
	restaurants = session.query(Restaurant).all()
	return render_template('restaurants.html', restaurants=restaurants)


@app.route('/restaurants/<int:restaurant_id>/menu')
def show_restaurant_with_id(restaurant_id):
	""" This method shows the menu of a specific restaurant """

	# Query the restaurant and its menu and render them with html
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
	for i in range(len(items)):
		if not '$' in items[i].price:
			items[i].price = '$' + items[i].price
	return render_template('menu.html', items=items, restaurant=restaurant)


@app.route('/restaurants/new', methods=['GET', 'POST'])
def create_restaurant():
	""" This method directs you to a page to create a new restaurant """

	# See if the request method is POST, i.e. a new restaurant is created
	# otherwise render the html 
	if request.method == 'POST':
		new_restaurant = Restaurant(name=request.form['name'])
		session.add(new_restaurant)
		session.commit()
		return redirect(url_for('restaurants'))
	else:
		return render_template('new_restaurant.html')


@app.route('/restaurants/<int:restaurant_id>/edit', methods=['GET', 'POST'])
def edit_restaurant(restaurant_id):
	""" This function directs us to another page where you edit a specific restaurant """

	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	# If the request method is POST then the restaurant has been edited
	# otherwise render the template to show the page
	if(request.method == 'POST'):
		new_name = request.form['name']
		restaurant.name = new_name
		session.add(restaurant)
		session.commit()
		return redirect(url_for('restaurants'))
	else:
		return render_template('edit_restaurant.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/delete', methods=['GET', 'POST'])
def delete_restaurant(restaurant_id):
	""" This function deletes a restaurant from the database """

	# See if the user tries to delete the restaurant or just opening the page
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if request.method == 'POST':
		session.delete(restaurant)
		session.commit()
		return redirect(url_for('restaurants'))
	else:
		return render_template('delete_restaurant.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/menu/new', methods=['GET', 'POST'])
def create_menu_item(restaurant_id):
	""" This method creates a new menu item in the specific restaurant's menu """

	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	if(request.method == 'POST'):
		name = request.form['name']
		description = request.form['description']
		price = '$' + request.form['price']
		course = request.form['course']
		if len(name) == 0 or len(description) == 0 or len(price) == 1 or len(course) == 0:
			pass
		else:
			new_item = MenuItem(name=name, course=course, description=description, price=price,\
				restaurant_id=restaurant_id, restaurant=restaurant)
			session.add(new_item)
			session.commit()
		return redirect(url_for('show_restaurant_with_id', restaurant_id=restaurant_id))
	else:
		return render_template('new_menu_item.html', restaurant=restaurant)


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/edit', methods=['GET', 'POST'])
def edit_menu_item(restaurant_id, menu_id):
	""" This method edits a menu item in a specific restaurant """

	# See if it's a post method
	# otherwise render the html to show the page
	restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
	item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
	if request.method == 'POST':
		name = request.form['name']
		description = request.form['description']
		price = '$' + request.form['price']
		course = request.form['course']
		if len(name) != 0:
			item.name = name
		if len(description) != 0:
			item.description = description
		if len(price) != 1:
			item.price = price
		if len(course) != 0:
			item.course = course
		session.add(item)
		session.commit()
		return redirect(url_for('show_restaurant_with_id', restaurant_id=restaurant_id))
	else:
		return render_template('edit_menu_item.html', restaurant=restaurant, item=item)
	


@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/delete', methods=['GET', 'POST'])
def delete_menu_item(restaurant_id, menu_id):
	""" This method deletes an menu item from the restaurant's menu """

	# See if the request method is POST, if so then delete the menu items
	# otherwise render the html and show the page
	item = session.query(MenuItem).filter_by(id=menu_id, restaurant_id=restaurant_id).one()
	if request.method == 'POST':
		session.delete(item)
		session.commit()
		return redirect(url_for('show_restaurant_with_id', restaurant_id=restaurant_id))
	else:
		restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
		return render_template('delete_menu_item.html', item=item, restaurant=restaurant)


if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0', port=5000)