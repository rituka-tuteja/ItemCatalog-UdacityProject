from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()


# Create dummy user
User1 = User(name="Jane Doe", email="janedoe@udacity.com",
             picture='/static/JaneDoe.jpg')
session.add(User1)
session.commit()


# Menu for Main China Town
restaurant1 = Restaurant(user_id=1, name="Main China Town")

session.add(restaurant1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Dumplings", description="pockets full of yummy",
                     price="$5.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Wonton with Chilli sauce", description="not for the faint hearted",
                     price="$5.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Hakka Noodles", description="angel hair with veggies and sauces",
                     price="$9.50", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Chocolate Cake", description="fresh baked and served with ice cream",
                     price="$3.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Fried Rice", description="Made with A grade rice",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Root Beer", description="16oz of refreshing goodness",
                     price="$1.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Iced Tea", description="with Lemon",
                     price="$.99", course="Beverage", restaurant=restaurant1)

session.add(menuItem6)
session.commit()

menuItem7 = MenuItem(user_id=1, name="Manchurian with rice/noodles", description="A must have, chef special",
                     price="$6.49", course="Entree", restaurant=restaurant1)

session.add(menuItem7)
session.commit()

menuItem8 = MenuItem(user_id=1, name="Schezwan platter", description="assortments of the best kind",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem8)
session.commit()


# Menu for Incredible India
restaurant2 = Restaurant(user_id=1, name="Incredible India")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Samosas", description="Crisp turnovers with spices potatoes and peas",
                     price="$3.99", course="Appetizer", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Dal Makhni with Naan", description="lentils delicately spiced", price="$12", course="Entree", restaurant=restaurant2)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Palak Paneer with rice", description="Spinach and Indian feta cheese cubes.",
                     price="$12", course="Entree", restaurant=restaurant2)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Vegetarian Thali", description="assorted colorful delicacies",
                     price="$15", course="Entree", restaurant=restaurant2)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Mango Lassi", description="summer in a glass",
                     price="$3.99", course="Beverage", restaurant=restaurant2)

session.add(menuItem5)
session.commit()

menuItem6 = MenuItem(user_id=1, name="Gulab Jamun", description="little laddoos made from yum and sugar",
                     price="$12", course="Entree", restaurant=restaurant2)

session.add(menuItem6)
session.commit()


# Menu for Thai Basil Leaf
restaurant1 = Restaurant(user_id=1, name="Thai Basil Leaf")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Pad Thai", description="peanut, lemon and basil goodness",
                     price="$8.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Chef special Soup", description="as healthy as they come",
                     price="$6.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Drunken Noodles", description="noodles drunk in savory taste",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Stinky Tofu", description="Thai dish, deep fried fermented tofu served with pickled cabbage.",
                     price="$7.99", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Thai Iced Tea", description="coconut milk in our special Thai tea",
                     price="$2.50", course="Beverage", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Julio Burrito Grill
restaurant1 = Restaurant(user_id=1, name="Julio Burrito Grill")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Fish Taco", description="choice of soft or hard tacos",
                     price="$5.99", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Especial Burrito", description="with extra guac and cheese",
                     price="$6.99", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Quesedilla", description="sandwich of burrito and cheese and corn",
                     price="$2.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Burrito bowl", description="burrito but in a bowl",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Soda Pop", description="choice of soda",
                     price="$2.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Queso Burrito", description="with special sauce",
                     price="$6.80", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Tony's Bistro
restaurant1 = Restaurant(user_id=1, name="Tony\'s Bistro")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Pesto Pasta", description="choice of pasta served with pesto sauce",
                     price="$13.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Farm House Pizza", description="all the veggies you can imagine are on this Pizza",
                     price="$14.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Mom's Spaghetti", description="Spaghetti with some incredible tomato sauce made by mom",
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Garlic Bread", description="Bread with melted cheese and garlic", 
                     price="$3.95", course="Appetizer", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem5 = MenuItem(user_id=1, name="Italian Platter", description="assorted platter of bread, pasta and pizza",
                     price="$18.95", course="Entree", restaurant=restaurant1)

session.add(menuItem5)
session.commit()


# Menu for Curry Leaf Plate
restaurant1 = Restaurant(user_id=1, name="Curry Leafy PLate")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Dosa", description="crepe served with your choice of topping",
                     price="$9.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="South Indian Thali", description="plated assortment of the variety",
                     price="$17.95", course="Entree", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Idli", description="circular shaped food for a healthy start",
                     price="$6.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Curd Rice", description="Yummiest rice delicacy",
                     price="$6.75", course="Entree", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Paysum", description="sweet dish",
                     price="$7.00", course="Dessert", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


# Menu for Cuppycake Bakery
restaurant1 = Restaurant(user_id=1, name="Cuppycake Bakery")

session.add(restaurant1)
session.commit()

menuItem9 = MenuItem(user_id=1, name="Fruit Cake", description="fruity goodness in a cake slice",
                     price="$8.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem9)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Chocolate Cake", description="chocolaty and cadbury slice",
                     price="$2.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Donut", description="ooooo",
                     price="$1.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem3 = MenuItem(user_id=1, name="Veg Patty", description="crispy potato filled crumchy food",
                     price="$7.50", course="Appetizer", restaurant=restaurant1)

session.add(menuItem3)
session.commit()

menuItem4 = MenuItem(user_id=1, name="Cheesecake", description="number of layers 2",
                     price="$8.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem4)
session.commit()

menuItem2 = MenuItem(user_id=1, name="Raspberry Butter Cake", description="seasonal only",
                     price="$9.50", course="Dessert", restaurant=restaurant1)

session.add(menuItem2)
session.commit()

menuItem10 = MenuItem(user_id=1, name="Pineapple Special", description="droplets of pineapple",
                      price="$1.99", course="Dessert", restaurant=restaurant1)

session.add(menuItem10)
session.commit()


# Menu for Mama's Deli
restaurant1 = Restaurant(user_id=1, name="Mama\'s Deli")

session.add(restaurant1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Veggie Burger", description="Burger with veggies, tomato, onion, patty is optional",
                     price="$6.95", course="Entree", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(user_id=1, name="French Fries", description="potatoes deep fried",
                     price="$3.99", course="Appetizer", restaurant=restaurant1)

session.add(menuItem2)
session.commit()


restaurant1 = Restaurant(user_id=1, name="Ice Cream Corner")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Vanilla", description="made from vanilla beans",
                     price="$5.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()

menuItem1 = MenuItem(user_id=1, name="Chocolate", description="top favorite",
                     price="$6.95", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


menuItem1 = MenuItem(user_id=1, name="Strawberry", description="natural flavors and chunks of strawberry",
                     price="$4.25", course="Dessert", restaurant=restaurant1)

session.add(menuItem1)
session.commit()


print "added menu items!"