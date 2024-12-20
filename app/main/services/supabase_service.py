from supabase import create_client
import os
from dotenv import load_dotenv

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url, supabase_key)

def login_user(email, senha):
    response = supabase.auth.sign_in_with_password({
        'email':email, 
        'password':senha
    })
    return response

def logout_user():
    try:
        response = supabase.auth.sign_out()
        if response:
            return "Usuário deslogado com sucesso"
        else:
            return "Falha ao deslogar usuário"
    except Exception as e:
        return f"Erro ao deslogar usuário: {str(e)}"
    
def reset_password(email):
    response = supabase.auth.api.reset_password_for_email(email)
    return response

def get_user_data():
    response = supabase.auth.get_user_identities()
    return response

def create_user(email, senha):
    response = supabase.auth.sign_up({
        'email':email, 
        'password':senha
    })
    print(response)
    return None

def create_profile(user_id: str, body: dict) -> dict:
    response = supabase.table('profiles').insert({
        'user_id': user_id,
        'email': body['email'],
        'name': body['name'],
        'bio': body['bio'],
        'favorite_books': body['favorite_books']
    }).execute()
    return response

def update_profile(user_id: str, body: dict) -> dict:
    response = supabase.table('profiles').update({
        'name': body['name'],
        'bio': body['bio'],
        'favorite_books': body['favorite_books']
    }).eq('user_id', user_id).execute()
    return response


def get_user_progress(user_id):
    response = supabase.from_('reading_progress').select('*').eq('user_id', user_id).execute()
    return response.data

# Outras funções conforme necessário
