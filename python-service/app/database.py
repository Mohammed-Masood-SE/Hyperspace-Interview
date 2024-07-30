from app import db
from app.models import Language

def initialize_db():
    db.create_all()
    # Insert initial data
    if Language.query.count() == 0:
        languages = [
            'C++',
            'JavaScript',
            'Python',
            'TypeScript',
            'Go'
        ]
        for lang in languages:
            db.session.add(Language(language=lang))
        db.session.commit()
