from flask import Flask, render_template, url_for, request, redirect, flash, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

app = Flask(__name__)

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/restaurants/<int:restaurant_id>/menu/JSON')
def restaurantMenuJSON(restaurant_id):
	items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id).all()
	return jsonify(MenuItems=[i.serialize for i in items])

@app.route('/restaurants/<int:restaurant_id>/menu/<int:menu_id>/JSON')
def menuItemJSON(restaurant_id, menu_id):
	item = session.query(MenuItem).filter_by(restaurant_id=restaurant_id, id=menu_id).one()
	return jsonify(MenuItem=item.serialize)

@app.route('/restaurants/<int:restaurant_id>/')
def restaurantMenu(restaurant_id):
    restaurant = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant.id)
    return render_template('menu.html', restaurant=restaurant, items=items)


@app.route('/restaurants/<int:restaurant_id>/add', methods=["GET", "POST"])
def newMenuItem(restaurant_id):
    if(request.method == "POST"):
    	new_menu_item = MenuItem(name=request.form["name"], restaurant_id=restaurant_id)
    	session.add(new_menu_item)
    	session.commit()
    	flash('new item has been created - ' + new_menu_item.name + '!')
    	return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
    	return render_template("newmenuitem.html", restaurant_id=restaurant_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/edit', methods=["GET", "POST"])
def editMenuItem(restaurant_id, menu_id):
    if request.method == "POST":
    	item = session.query(MenuItem).filter_by(id=menu_id).one()
    	new_name = request.form["name"]
    	if(new_name):
    		old_name = item.name
    		item.name = new_name
    		session.add(item)
    		session.commit()
    		flash(old_name + ' has been edited to ' + new_name)
    	return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
    else:
    	return render_template("editmenuitem.html", item=session.query(MenuItem).filter_by(id=menu_id).one(),\
    		restaurant_id=restaurant_id, menu_id=menu_id)


@app.route('/restaurants/<int:restaurant_id>/<int:menu_id>/delete', methods=["GET", "POST"])
def deleteMenuItem(restaurant_id, menu_id):
	if(request.method == "POST"):
		item = session.query(MenuItem).filter_by(id=menu_id).one()
		name = item.name
		session.delete(item)
		session.commit()
		flash(name + ' has been deleted!')
		return redirect(url_for("restaurantMenu", restaurant_id=restaurant_id))
	else:
		return render_template("deletemenuitem.html", item=session.query(MenuItem).filter_by(id=menu_id).one(),\
			restaurant_id=restaurant_id, menu_id=menu_id)
    

if __name__ == '__main__':
	app.secret_key = 'super_secret_key'
	app.debug = True
	app.run(host='0.0.0.0', port=5000)