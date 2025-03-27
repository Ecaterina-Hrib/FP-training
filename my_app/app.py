from flask import Flask, Blueprint, jsonify
from config import Config
from models import db
#
app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route("/")
def index():
    try:
        db.session.commit()
        return jsonify({"message": "Conexiunea la baza de date este activă."}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Eroare la conexiune: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)

