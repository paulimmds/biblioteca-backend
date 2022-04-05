from flask import current_app, request, jsonify
from application import db
from application.models import Obra

"""@current_app.route('/obra', methods=['GET'])
def obra_get():
    data = Obra.query.all()
    print(data)
    return jsonify('status : OK')
"""
@current_app.route('/obra', methods=['GET','POST'])
def obra():
    if request.method == 'GET':
        data = Obra.query.all()
        print(data)
        return jsonify('status : OK')
    
    data = request.json
    obra = Obra(id=data['id'],
                titulo=data['titulo'],
                editora=data['editora'],
                foto=data['foto'],
                autores=data['autores'])

    db.session.add(obra)
    db.session.commit()
    return jsonify("status : OK")