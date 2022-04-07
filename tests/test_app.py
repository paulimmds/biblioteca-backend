""" 
Testing the API routes
    - /obra/ [GET]
    - /obra/ [POST]
    - /obra/<id>/delete [DELETE]
    - /obra/<id>/update [UPDATE]
"""
def test_get(test_client):
    res = test_client.get('/obra')
    
    assert res.status_code == 200

def test_post(test_client):
    dados = {
        'titulo':'Harry Potter',
        'editora':'Rocco',
        'foto':'https://link.com',
        'autores':'JK Rowlling'
    }
    
    res = test_client.post('/obra', json=dados)
    assert res.status_code == 200

def test_put(test_client):
    dados = {
        'id':'10',
        'titulo':'Teste 1',
        'editora':'Teste 2',
        'foto':'Teste 3',
        'autores':'Teste 4'
    }

    res = test_client.put(f"/obra/{dados['id']}", json=dados)
    assert res.status_code == 200

def test_put_nonexisting_id(test_client):
    dados = {
        'id':'100',
        'titulo':'Teste 1',
        'editora':'Teste 2',
        'foto':'Teste 3',
        'autores':'Teste 4'
    }

    res = test_client.put(f"obra/{dados['id']}", json=dados)
    assert res.status_code == 404

def test_del(test_client):
    dados = {'id': '21'}

    res = test_client.delete(f"obra/{dados['id']}", json=dados)
    assert res.status_code == 200

def test_del_nonexisting_id(test_client):
    dados = {'id': '100'}

    res = test_client.delete(f"obra/{dados['id']}", json=dados)
    assert res.status_code == 404

