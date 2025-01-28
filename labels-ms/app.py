from flask import Flask, request, jsonify
from dotenv import load_dotenv
from models import db, RecordLabel
from flask_migrate import Migrate
from utils import generate_fake_record_labels
import os

# Cargar variables de entorno
load_dotenv()

app = Flask(__name__)

# Configuración de la base de datos
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/record_labels_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Inicializar la base de datos y las migraciones
db.init_app(app)
migrate = Migrate(app, db)

# Cargar la API Key desde el archivo .env
VALID_API_KEY = os.getenv("API_KEY")

# Middleware para verificar la API Key desde el encabezado LABELS-API-KEY
@app.before_request
def verify_api_key():
    api_key = request.headers.get("LABELS-API-KEY")  # Cambiado a LABELS-API-KEY
    if not api_key or api_key != VALID_API_KEY:
        return jsonify({"error": "Unauthorized"}), 401

# Ruta para generar sellos discográficos
@app.route('/api/generate_labels/', methods=['POST'])
def generate_labels():
    try:
        n = int(request.json.get('n', 10))  # Número de registros a generar
        labels = generate_fake_record_labels(n)
        
        # Guardar en la base de datos
        for label in labels:
            new_label = RecordLabel(name=label['name'], country=label['country'])
            db.session.add(new_label)
        db.session.commit()

        return jsonify({"message": f"{n} record labels generated successfully!"}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Ruta para obtener todos los sellos discográficos
@app.route('/api/record_labels/', methods=['GET'])
def get_record_labels():
    try:
        labels = RecordLabel.query.all()
        labels_list = [{"id": label.id, "name": label.name, "country": label.country} for label in labels]
        return jsonify(labels_list), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
