import openai
from config import Config

print(Config.OPENAI_API_KEY)

# Substitua pela sua chave de API
openai.api_key = Config.OPENAI_API_KEY

def get_explanation(verse_text):
    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",  # Escolha o modelo apropriado
        messages=[
            {"role": "system", "content": "Você é um assistente teológico que explica versículos da Bíblia de maneira simples, clara e concisa, com profundidade teológica, sem se aprofundar em jargões complicados."},
            {"role": "user", "content": f"Explique o seguinte versículo bíblico de forma simples e direta: {verse_text}"}
        ],
        temperature=0.7,
        max_tokens=300,
    )
    return response['choices'][0]['message']['content']

