from flask import Blueprint, request, jsonify
from ..services.supabase_service import get_user_progress, login_user, logout_user
from ..services.bible_api import get_verse, get_chapter

bp = Blueprint('main', __name__)

bible = Blueprint('bible', __name__)

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    senha = data.get('senha')
    
    # Chamar função de login
    token = login_user(email, senha)
    
    if token:
        return jsonify({'token': token}), 200
    else:
        return jsonify({'error': 'Credenciais inválidas'}), 401
    
@bp.route('/logout', methods=['POST'])
def logout():
    # Chamar função de logout
    message = logout_user()
    return jsonify({'message': message})

@bp.route('/user/create-profile/<user_id>', methods=['POST'])
def create_profile(user_id):
    data = request.get_json()
    response = create_profile(user_id, data)
    return jsonify(response)

@bp.route('/progress/<user_id>', methods=['GET'])
def user_progress(user_id):
    progress = get_user_progress(user_id)
    return jsonify(progress)


# Definindo a rota para buscar um versículo
@bible.route('/<book>/chapter/<chapter>/verse/<verse>', methods=['GET'])
def get_verse_route(book, chapter, verse):
    """
    Rota para obter um versículo específico do livro, capítulo e versículo fornecidos.
    """
    return get_verse(book, int(chapter), int(verse))  # Chama a função get_verse do serviço

# Definindo a rota para buscar um capítulo
@bible.route('/<book>/chapter/<chapter>', methods=['GET'])
def get_chapter_route(book, chapter):
    """
    Rota para obter todos os versículos de um capítulo específico do livro.
    """
    return get_chapter(book, int(chapter))  # Chama a função get_chapter do serviço