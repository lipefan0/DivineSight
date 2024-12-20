import pytest
import json
from app.main.services.supabase_service import login_user, create_user, create_profile, update_profile

@pytest.mark.skip("Ainda não implementado")
def test_login_user():
    login_data = {
        'email': 'lipefan0@gmail.com',
        'senha': '19708512Aa@'
    }
    response = login_user(login_data['email'], login_data['senha'])
    assert response.user is not None
    assert response.user.email == login_data['email']
    print("teste completado com sucesso")

@pytest.mark.skip("Ainda não implementado")
def test_create_profile():
    user_id = '60695a9a-d1d2-44c2-bf07-45d78657c15a'
    profile_data = {
        'user_id': user_id,
        'email': 'contato@peitastyle.com',
        'name': 'Felipe',
        'bio': 'Software Developer',
        'favorite_books': [
            'genesis',
            'pedro',
            'lucas'
        ]
    }
    response = create_profile(user_id, profile_data)
    print("Profile created successfully")

def test_update_profile():
    user_id = '60695a9a-d1d2-44c2-bf07-45d78657c15a'
    profile_data = {
        'name': 'Felipe Fernandes',
        'bio': 'CEO at Peita Style',
        'favorite_books': [
            'genesis',
            'pedro',
            'lucas'
        ]
    }
    response = update_profile(user_id, profile_data)
    print("Profile updated successfully")

def test_create_user():
    pytest.skip("Ainda não implementado")
    create_data = {
        'email': 'contato@peitastyle.com',
        'senha': '19708512Aa@'
    }
    response = create_user(create_data['email'], create_data['senha'])
    print(response)
