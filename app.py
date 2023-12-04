from flask import Flask,render_template,redirect,request,flash, url_for
from models import db,Pet,connect_db
from forms import AddPetForm,EditForm


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adopt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = 'abdfasdfasdf'

connect_db(app)

app.app_context().push()
db.create_all()



@app.route("/")
def home():
    pets = Pet.query.all()
    """Show a list of pets"""
    
    return render_template('home.html',pets=pets)


@app.route("/add", methods=("GET","POST"))
def addPet():
    """Retrieve values from the add form and save them in database"""
    if request.method == 'POST':
        new_pet = Pet(
        name = request.form['pet_name'],
        species = request.form['species'],
        photo_url = request.form['photourl'] or None,
        age = request.form['age'] or None,
        notes = request.form['notes'] or None)
     
        name = request.form['pet_name']  
        db.session.add(new_pet)
        db.session.commit()
        
        flash(f"{name} is added!")
        
        return redirect(url_for("home"))
    
    else:
        form = AddPetForm()
        return render_template('add-pet.html', form=form)
    
    
@app.route("/pets/<int:pet_id>")
def details(pet_id):
    """Show details of the pet with the id"""
    pet = Pet.query.get(pet_id)
    
    return render_template("details.html",pet=pet)


@app.route("/pets/<int:pet_id>/edit",methods=("GET","POST"))
def edit(pet_id):
    """Show an editting form,retrieve new values for the pet and save them in database"""
    if request.method=='GET':
        
        pet = Pet.query.get(pet_id)
        form = EditForm()
        form.available.data = pet.available
        form.pet_name.label = pet.name
        form.photourl.data = pet.photo_url
        form.notes.data = pet.notes
        return render_template('editform.html',form=form,pet_id=pet_id)
    
    
    else:
        pet = Pet.query.get(pet_id)
            
    
        pet.photo_url = request.form['photourl'] or None
        pet.notes = request.form['notes'] or None
        if 'available' in request.form:
            pet.available = True
        else:
            pet.available = False
        
        db.session.add(pet)
        db.session.commit()
        
        return redirect(url_for("details",pet_id = pet_id))