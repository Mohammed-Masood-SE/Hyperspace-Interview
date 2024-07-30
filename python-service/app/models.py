from app import db

class Language(db.Model):
    __tablename__ = 'languages'
    lang_id = db.Column(db.Integer, primary_key=True)
    language = db.Column(db.String(80), nullable=False)