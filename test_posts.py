import requests
import pytest

# Ejecutarlo con pytest
#pytest test_posts.pys

BASE_URL = "https://jsonplaceholder.typicode.com"

def test_posts_crud():
    print("\n--- INICIANDO PRUEBAS DE POSTS ---")
    
    # GET
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100
    assert "body" in data[0]
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"

    # POST
    new_post = {
        "userId": 1,
        "title": "Hola este es un titulo",
        "body": "Este es un ejemplo de prueba"
    }
    response = requests.post(f"{BASE_URL}/posts", json=new_post)
    assert response.status_code == 201
    assert response.json()["id"] is not None
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    # PUT
    update_data = {
        "id": 1,
        "title": "Titulo actualizado",
        "body": "Cuerpo actualizado",
        "userId": 1
    }
    response = requests.put(f"{BASE_URL}/posts/1", json=update_data)
    assert response.status_code == 200
    assert response.json()['title'] == "Titulo actualizado"
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"

    # DELETE
    response = requests.delete(f"{BASE_URL}/posts/1")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"


def test_todos_crud():
    print("\n--- INICIANDO PRUEBAS DE TODOS ---")
    
    # GET
    response = requests.get(f"{BASE_URL}/todos")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 200
    
    first_todo = data[0]
    assert "completed" in first_todo
    assert isinstance(first_todo['completed'], bool)
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"

    # POST
    new_todo = {
        "userId": 2,
        "title": "Sacar la basura",
        "completed": False
    }
    response = requests.post(f"{BASE_URL}/todos", json=new_todo)
    assert response.status_code == 201
    assert response.json()['completed'] is False
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    # PUT
    update_todo = {
        "userId": 2,
        "id": 1,
        "title": "Sacar la basura",
        "completed": True
    }
    response = requests.put(f"{BASE_URL}/todos/1", json=update_todo)
    assert response.status_code == 200
    assert response.json()['completed'] is True
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    #DELETE
    response = requests.delete(f"{BASE_URL}/todos/1")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"

def test_albums_crud():
    print("\n--- INICIANDO PRUEBAS DE ALBUMS ---")
    
    # GET
    response = requests.get(f"{BASE_URL}/albums")
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 100
    assert "title" in data[0]
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    # POST
    new_album = {
        "userId": 10,
        "title": "lorem impsu"
    }
    response = requests.post(f"{BASE_URL}/albums", json=new_album)
    assert response.status_code == 201
    assert response.json()['title'] == "lorem impsu"
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    # PUT
    update_album = {
        "userId": 10,
        "id": 92,
        "title": "Titulo actualizado"
    }
    response = requests.put(f"{BASE_URL}/albums/92", json=update_album)
    assert response.status_code == 200
    assert response.json()['title'] == "Titulo actualizado"
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"
    
    # DELETE
    response = requests.delete(f"{BASE_URL}/albums/1")
    assert response.status_code == 200
    assert response.elapsed.total_seconds() < 2.0, "El endpoint es muy lento (>2s)"