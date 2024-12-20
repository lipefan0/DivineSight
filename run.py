from flask import Flask
from app.main.routes.routes import bp, bible

app = Flask(__name__)

app.register_blueprint(bp, url_prefix='/api')  # URL prefix para as rotas principais
app.register_blueprint(bible, url_prefix='/bible')  # URL prefix para as rotas da Bíblia

if __name__ == '__main__':
    app.run(debug=True, port=5001)
