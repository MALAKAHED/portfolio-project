from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Meal, Order, User  # Assuming your models are in a separate file called models.py

app = Flask(__name__)

# Database setup
engine = create_engine('sqlite:///the_6_meals.db')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

@app.route('/')
def index():
    # Fetch meals from the database
    meals = session.query(Meal).all()
    return render_template('index.html', meals=meals)

# Route for meal details
@app.route('/meal/<int:meal_id>')
def meal_details(meal_id):
    meal = session.query(Meal).get(meal_id)
    return render_template('meal_details.html', meal=meal)

# If you want to add more functionality such as placing orders, add routes accordingly.

if __name__ == '__main__':
    app.run(debug=True)
