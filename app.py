from distutils.log import debug
from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import Bike, db, connect_db

debug = DebugToolbarExtension()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///bike_shop_db'
app.config['SQLALCHEMY_ECHO'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = '12m45'

connect_db(app)
db.create_all()

@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/about-us')
def about_page():
    return render_template('about.html')

@app.route('/collection')
def bike_list():
    bikes = Bike.query.all()
    return render_template('items.html', bikes=bikes)

@app.route('/collection/<int:bike_id>')
def detail(bike_id):
    bike = Bike.query.get(bike_id)
    return render_template('details.html',bike = bike)

