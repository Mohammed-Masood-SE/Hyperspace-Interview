from app import app, database
with app.app_context():
    database.initialize_db()

if __name__ == '__main__':
    app.run(debug=True)
