from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, TextAreaField, SelectField
from wtforms.fields.html5 import URLField
from wtforms.validators import InputRequired, Optional, URL, AnyOf, NumberRange

class AddPetForm(FlaskForm):
    """Form for adding a pet."""

    specie_types = ['cat', 'dog', 'porcupine']

    name        = StringField('Pet Name', validators=[InputRequired()])

    # species     = SelectField('Species', choices=[(sp, sp) for sp in specie_types], 
    #                                     validators=[InputRequired()])
    species     = StringField('Species', validators=[InputRequired(),
                                                    AnyOf(['cat', 'dog', 'porcupine'])])
    photo_url   = URLField('Photo Url', validators=[Optional(),
                                                    URL()])
    age         = IntegerField('Age', validators=[Optional(),
                                                    NumberRange(min=0, max=30)])
    notes       = TextAreaField('Notes', validators=[Optional()])