import json
import os
from flask import jsonify

from app.main.services.openai_service import get_explanation

# Constantes
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# Alterar para usar um caminho absoluto correto
BIBLE_STRUCTURE_PATH = os.path.join(BASE_DIR, "../../../acf.json")

# Carregando o JSON com a estrutura da Bíblia
def load_bible_structure():
    with open(BIBLE_STRUCTURE_PATH, "r", encoding="utf-8-sig") as file:
        return json.load(file)

bible_structure = load_bible_structure()

# Buscar livro baseado no nome ou abreviação
def get_book_data(book):
    # Verificar pelo nome ou abreviação
    return next((b for b in bible_structure if b["name"].lower() == book.lower() or b["abbrev"].lower() == book.lower()), None)

# Buscar capítulo dentro do livro
def get_chapter_data(book_data, chapter):
    # O capítulo é indexado em 1, então o índice do array é `chapter - 1`
    if chapter > len(book_data["chapters"]):
        return None
    return book_data["chapters"][chapter - 1]

# Buscar versículo dentro do capítulo
def get_verse_data(chapter_data, verse):
    # O versículo é simplesmente um índice do capítulo
    if verse > len(chapter_data):
        return None
    return chapter_data[verse - 1]

# Função para obter o versículo
def get_verse(book, chapter, verse):
    book_data = get_book_data(book)
    if not book_data:
        return jsonify({"error": f"O livro '{book}' não foi encontrado."}), 404

    chapter_data = get_chapter_data(book_data, chapter)
    if not chapter_data:
        return jsonify({"error": f"O capítulo {chapter} não existe no livro '{book}'."}), 404

    verse_data = get_verse_data(chapter_data, verse)
    if not verse_data:
        return jsonify({"error": f"O versículo {verse} não existe no capítulo {chapter} do livro '{book}'."}), 404

    # Obter a explicação teológica do versículo
    explanation = get_explanation(verse_data)
    
    return jsonify({"book": book_data["name"], "chapter": chapter, "verse": verse, "text": verse_data, "explanation": explanation}), 200

# Função para obter o capítulo
def get_chapter(book, chapter):
    book_data = get_book_data(book)
    if not book_data:
        return jsonify({"error": f"O livro '{book}' não foi encontrado."}), 404

    chapter_data = get_chapter_data(book_data, chapter)
    if not chapter_data:
        return jsonify({"error": f"O capítulo {chapter} não existe no livro '{book}'."}), 404

    return jsonify({"book": book_data["name"], "chapter": chapter, "verses": chapter_data}), 200
