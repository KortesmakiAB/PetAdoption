from models import *
from app import app

# Create all tables
db.drop_all()
db.create_all()

# If table isn't empty, empty it
Pet.query.delete()

# Add pets
p1 = Pet(name='Sprinkles', species='cat', photo_url='https://vetstreet.brightspotcdn.com/dims4/default/b59d4b7/2147483647/thumbnail/645x380/quality/90/?url=https%3A%2F%2Fvetstreet-brightspot.s3.amazonaws.com%2Fca%2Ffe%2Fd59759594da1b16835f6743a274d%2FHimalayan-AP-07LB1U-645sm3614.jpg', age=8, notes='Previous Owner: PA paper company accountant. Treated like a spoiled human baby.')
p2 = Pet(name='Sprinkles2', species='dog', photo_url='https://www.goodnewsnetwork.org/wp-content/uploads/2015/08/cute-dog-couch-AllPaws-facebook.jpg', age=2, available=False)
p3 = Pet(name='Pokey', species='porcupine', photo_url='https://www.eekwi.org/sites/default/files/2019-12/porcupine.jpg', age=4, notes='Pokey, LOOOOOOOVES to eat dirt. He literally can\'t stop eating dirt, ever.')

db.session.add_all([p1, p2, p3])
db.session.commit()