from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem


engine = create_engine('sqlite:///restaurantmenu.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind = engine)

# staging zone, nothing persisted until comiit
session = DBSession()

myFirstRestaurant = Restaurant(name = "Pizza Palace") 
session.add(myFirstRestaurant)
session.commit()

# return a list with all entries
session.query(Restaurant).all()

cheesepizza = MenuItem(name = "Cheese Pizza", description = "Made with all natural ingredients and fresh mozzarella", course = "Entree", price = "$8.99", restaurant = myFirstRestaurant)

session.add(cheesepizza)
session.commit()

items = session.query(MenuItem).all()

for item in items:
	print item.name


firstResult = session.query(Restaurant).first()


# find the item we want to update
veggieBurgers = session.query(MenuItem).filter_by(name='Veggie Burger')
for veggieBurger in veggieBurgers:
	print veggieBurger.id 
	print veggieBurger.restaurant.name
	print "\n"

UrbanVeggieBurger = session.query(MenuItem).filter_by(id=9).one()
print UrbanVeggieBurger.price
UrbanVeggieBurger.price = '$4.99'
session.add(UrbanVeggieBurger)
session.commit()
print UrbanVeggieBurger.price


spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
print spinach.restaurant.name
session.delete(spinach)
session.commit()

spinach = session.query(MenuItem).filter_by(name = 'Spinach Ice Cream').one()
