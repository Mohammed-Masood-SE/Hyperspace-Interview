from flask import Flask, jsonify, request, abort
from app import app, db
from app.models import Language

@app.route('/languages/', methods=['GET'])
def get_languages():
    languages = Language.query.all()
    return jsonify([language.language for language in languages])

@app.route('/languages/', methods=['POST'])
def add_language():
    if not request.json or 'language' not in request.json:
        abort(400, description="Invalid request: No 'language' field found in JSON body.")
    
    language_name = request.json['language']
    
    if not isinstance(language_name, str) or len(language_name) > 80:
        abort(400, description="Invalid language name. Must be a string up to 80 characters long.")
        
    new_language = Language(language=language_name)
    db.session.add(new_language)
    db.session.commit()
    
    return jsonify({'lang_id': new_language.lang_id, 'language': new_language.language}), 201
