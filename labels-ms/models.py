from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class RecordLabel(db.Model):
    __tablename__ = 'record_labels'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(50), nullable=False)
