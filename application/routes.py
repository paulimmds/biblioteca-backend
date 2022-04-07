from flask import request, jsonify
from application import db
from application.models import Obra
from flask import Blueprint

app_bp = Blueprint('app_bp', __name__)

@app_bp.route('/obra', methods=['GET'])
def obra_get():
    if request.method == 'GET':
        obras = Obra.query.all()
        data = []

        for obra in obras:
            dic = {'id':obra.id,
                 'titulo':obra.titulo,
                 'editora':obra.editora,
                 'foto':obra.foto,
                 'autores':obra.autores}
            data.append(dic)
        
        result = {'obras':data}

        return jsonify(result)

@app_bp.route('/obra', methods=['POST'])
def obra_post():
    data = request.json
    obra = Obra(titulo=data['titulo'],
                editora=data['editora'],
                foto=data['foto'],
                autores=data['autores'])

    db.session.add(obra)
    db.session.commit()
    return jsonify("status : OK")

@app_bp.route('/obra/<id>', methods=['PUT'])
def obra_put(id):
    data = request.json
    obra = Obra.query.filter_by(id=id).first()
    if obra:
        obra.update(data)
        db.session.commit()
        return jsonify("status : OK")
    
    return jsonify("There is no Obra with this ID"), 404

@app_bp.route('/obra/<id>', methods=['DELETE'])
def obra_del(id):
    data = request.json
    obra = Obra.query.filter_by(id=id).first()
    if obra:
        db.session.delete(obra)
        db.session.commit()
        return jsonify("Obra deletada com sucesso!")
    return jsonify("Obra não existe!"), 404