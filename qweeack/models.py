from werkzeug.security import generate_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, LoginManager
from datetime import datetime
import uuid
from flask_marshmallow import Marshmallow

from .helpers import get_stock_data

db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    """Given *user_id*, return the associated User object.
    :param unicode user_id: user_id (email) user to retrieve
    """
    return User.query.get(user_id)

class User(db.Model, UserMixin):
    """
    Create a User table
    """
    __tablename__ = 'users'
    user_id = db.Column(db.String, primary_key=True)
    first_name = db.Column(db.String(60))
    last_name = db.Column(db.String(60))
    email = db.Column(db.String(60), nullable=False, unique=True)
    password = db.Column(db.String(128), nullable=False)
    member_since = db.Column(db.DateTime(), default=datetime.utcnow)
    last_seen = db.Column(db.DateTime(), default=datetime.utcnow)
    data_added = db.Column(db.DateTime(), default=datetime.utcnow)

    def __init__(self, email, password, first_name, last_name):
        self.user_id = self.set_id()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def set_id(self):
        """
        set_id()
        generates a unique user id using the uuid module
        """
        return str(uuid.uuid4())
    
    def get_id(self):
        return str(self.user_id)
    
    def set_password(self, password):
        """
        set_password()
        hashes the password using the werkzeug.security.generate_password_hash() method
        """
        return generate_password_hash(password)
    
    def __repr__(self):
        return f"<User: {self.email}>"
    

class stock(db.Model):
    """
    Create a stock table
    """
    __tablename__ ='stocks'
    stock_id = db.Column(db.Integer, primary_key=True)
    stock_name = db.Column(db.String(60), nullable=False)
    stock_symbol = db.Column(db.String(60), nullable=False)
    stock_price = db.Column(db.Float, nullable=False)
    stock_open = db.Column(db.Float, nullable=False)
    stock_high = db.Column(db.Float, nullable=False)
    stock_low = db.Column(db.Float, nullable=False)
    stock_volume = db.Column(db.Float, nullable=False)
    stock_market_cap = db.Column(db.Float, nullable=False)
    stock_change = db.Column(db.Float, nullable=False)
    stock_change_percent = db.Column(db.Float, nullable=False)
    stock_date = db.Column(db.DateTime(), default=datetime.utcnow)
    user_id = db.Column(db.String, db.ForeignKey('users.user_id'))

    def __init__(self, stock_name, stock_symbol, stock_price, stock_open, stock_high, stock_low, stock_volume, stock_market_cap, stock_change, stock_change_percent, user_id):
        self.stock_name = self.set_stock_name(stock_name)
        self.stock_symbol = self.set_stock_symbol(stock_symbol)
        self.stock_price = self.set_stock_price(stock_price)
        self.stock_open = self.set_stock_open(stock_open)
        self.stock_high = self.set_stock_high(stock_high)
        self.stock_low = self.set_stock_low(stock_low)
        self.stock_volume = self.set_stock_volume(stock_volume)
        self.stock_market_cap = self.set_stock_market_cap(stock_market_cap)
        self.stock_change = self.set_stock_change(stock_change)
        self.stock_change_percent = self.set_stock_change_percent(stock_change_percent)
        self.user_id = user_id
    
    def set_id(self):
        """
        set_id()
        generates a unique user id using the uuid module
        """
        return str(uuid.uuid4())

    def set_stock_name(self, stock_name):
        print(stock_name)
        return stock_name
    
    def set_stock_symbol(self, stock_symbol):
        print(stock_symbol)
        return stock_symbol
    
    def set_stock_price(self, stock_price):
        print(stock_price)
        return stock_price

    def set_stock_open(self, stock_open):
        print(stock_open)
        return stock_open

    def set_stock_high(self, stock_high):
        print(stock_high)
        return stock_high

    def set_stock_low(self, stock_low):
        print(stock_low)
        return stock_low

    def set_stock_volume(self, stock_volume):
        print(stock_volume)
        return stock_volume

    def set_stock_market_cap(self, stock_market_cap):
        print(stock_market_cap)
        return stock_market_cap

    def set_stock_change(self, stock_change):
        print(stock_change)
        return stock_change

    def set_stock_change_percent(self, stock_change_percent):
        print(stock_change_percent)
        return stock_change_percent

    def __repr__(self):
        return f"<Stock: {self.stock_name}>"
    

class StockSchema(ma.Schema):
    """
     StockSchema
     """
    class Meta:
        fields = ['stock_id','stock_name','stock_symbol','stock_price','stock_open','stock_high','stock_low','stock_volume','stock_market_cap','stock_change','stock_change_percent','stock_date', 'user_id']


stock_schema = StockSchema()
stocks_schema = StockSchema(many=True)




        
        