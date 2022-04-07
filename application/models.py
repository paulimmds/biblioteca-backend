from lzma import FORMAT_AUTO
from application import db

class Obra(db.Model):
    __tablename__= 'Obra'
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String(255), nullable=False)
    editora = db.Column(db.String(255), nullable=False)
    foto = db.Column(db.String(255), nullable=False)
    autores = db.Column(db.String(255), nullable=False)

    def update(self, data):
        for key, value in data.items():
            setattr(self, key, value)
        
        return self