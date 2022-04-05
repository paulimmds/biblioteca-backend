Rotas da aplicação:

[POST] /obras : A rota deverá receber titulo, editora, foto, e autores dentro do corpo da requisição. Ao cadastrar um novo projeto, ele deverá ser armazenado dentro de um objeto no seguinte formato: { id: 1, titulo: 'Harry Potter', editora: 'Rocco',foto: 'https://i.imgur.com/UH3IPXw.jpg', autores: ["JK Rowling", "..."]};

[GET] /obras/ : A rota deverá listar todas as obras cadastradas

[PUT] /obras/id : A rota deverá atualizar as informações de titulo, editora, foto e autores da obra com o id presente nos parâmetros da rota

[DELETE] /obras/id : A rota deverá deletar a obra com o id presente nos parâmetros da rota