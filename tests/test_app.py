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
        'id':'1',
        'titulo':'Harry Potter',
        'editora':'Rocco',
        'foto':'https://link.com',
        'autores':'JK Rowlling'
    }
    
    res = test_client.post('/obra', json=dados)
    assert res.status_code == 200