from models import db, Pet
from app import app

with app.app_context():
    db.drop_all()
    db.create_all()


    pets = [Pet(name = 'dunkin', species = 'dog', 
                 photo_url = 'https://preview.redd.it/are-these-little-guys-really-shih-tzus-v0-p2rv4bvt1mec1.jpg?width=626&format=pjpg&auto=webp&s=5c74e0a7ede8053a8920d442d6319532d7b783f5',
                 age = '5',
                 notes = 'Black dog very cute'), 
                 Pet(
    name='Max', 
    species='dog', 
    photo_url='data:image/jpeg;base64,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', 
    age=2, 
    notes='Energetic golden retriever'
), Pet(
    name='Luna', 
    species='rabbit', 
    photo_url='data:image/jpeg;base64,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', 
    age=1, 
    notes='Fluffy white rabbit with a gentle personality',
    available = False
)]
    
    db.session.add_all(pets)
    db.session.commit()

    print('Adding to database successful')