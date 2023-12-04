from flask_wtf import FlaskForm
from wtforms import (StringField, TextAreaField, IntegerField,BooleanField,SelectField)
from wtforms.validators import InputRequired, Length, NumberRange,Optional,URL




class AddPetForm(FlaskForm):
    pet_name = StringField('Pet Name', validators = [InputRequired()])
    species = SelectField('Species', choices=[("cat", "Cat"), ("dog", "Dog"), ("porcupine", "Porcupine")])
    photourl = StringField('Photo URL',validators=[Optional(),URL()])
    age = IntegerField('Age',validators=[Optional(),NumberRange(min=0, max=30)])
    notes = TextAreaField('Notes',validators=[Optional(),Length(min=10)])
   
    
    
    
    
    
class EditForm(FlaskForm):
    pet_name = StringField('Pet Name', validators = [InputRequired()])
    photourl = StringField('Photo URL',validators=[Optional(),URL()])
    notes = TextAreaField('Notes',validators=[Optional(),Length(min=10)])
    available = BooleanField('Available')
