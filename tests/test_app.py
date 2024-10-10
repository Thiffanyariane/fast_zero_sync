from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Ação
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Assert


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'Thiffany',
            'password': '1234',
            'email': 'thi@email.com',
        },
    )
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'Thiffany',
        'email': 'thi@email.com',
    }


def teste_read_user(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'Thiffany',
                'email': 'thi@email.com',
            }
        ]
    }


def teste_get_user_id(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'id': 1,
        'username': 'Thiffany',
        'email': 'thi@email.com',
    }


def teste_get_user_id_not_found(client):
    response = client.get('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def teste_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'id': 1,
            'password': '12345',
            'username': 'testeusername2',
            'email': 'teste@teste.com',
        },
    )
    assert response.json() == {
        'id': 1,
        'username': 'testeusername2',
        'email': 'teste@teste.com',
    }


def teste_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'id': 2,
            'password': '12345',
            'username': 'testeusername2',
            'email': 'teste@teste.com',
        },
    )
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}


def teste_delete_user(client):
    response = client.delete('/users/1')
    assert response.json() == {'message': 'User deleted'}


def teste_delete_user_not_found(client):
    response = client.delete('/users/2')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'User not found'}
