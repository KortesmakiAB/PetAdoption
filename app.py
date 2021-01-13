from flask import Flask, request, redirect, render_template
from models import *
from forms import AddPetForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///petadoption'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True

connect_db(app)

from flask_debugtoolbar import DebugToolbarExtension
app.config['SECRET_KEY'] = "AdoptMittens!"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)


@app.route('/')
def show_home_page():
    """Display Homepage"""

    pets = Pet.query.all()
    
    return render_template('index.html', pets=pets)


@app.route('/add', methods=['GET', 'POST'])
def get_new_pet():
    """Display form to add a pet (GET)
    or handles new form submission (POST)"""

    form = AddPetForm()
    
    if form.validate_on_submit():
        name        = form.name.data
        species     = form.species.data
        photo_url   = form.url.data
        age         = form.age.data
        notes       = form.notes.data

        pet = Pet(name=name, species=species, photo_url=url, age=age, notes=notes)
        db.session.add(pet)
        db.session.commit()

        return redirect('/')

    else:
        return render_template('pet_add.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def show_pet_details(pet_id):
    """Show details about a pet.
    Show a form to edit the pet."""

    pet     = Pet.query.get_or_404(pet_id)
    form    = AddPetForm(obj=pet)

    if form.validate_on_submit():
        pet.name        = form.name.data
        pet.species     = form.species.data
        pet.photo_url   = form.photo_url.data
        pet.age         = form.age.data
        pet.notes       = form.notes.data

        db.session.commit()

        return redirect('/')

    else:
        return render_template('pet_display_edit.html', pet=pet, form=form)

