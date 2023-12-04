from flask_sqlalchemy import SQLAlchemy

default_img = "https://via.placeholder.com/300x200/808080/000000?text=NA"

db = SQLAlchemy()

class Pet (db.Model):
    __tablename__ = 'pets'
    
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    name = db.Column(db.Text,nullable=False)
    species = db.Column(db.Text,nullable=False)
    photo_url = db.Column(db.Text,default = default_img)
    age = db.Column(db.Integer,default=None, nullable=True)
    notes =db.Column(db.Text)
    available = db.Column(db.Boolean,default = True, nullable=False)
    
    
def connect_db(app):
    db.app = app
    db.init_app(app)
    

    