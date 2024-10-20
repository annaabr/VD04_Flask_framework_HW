from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/blog/')
def blog():
    return render_template('blog.html')

@app.route('/contacts/')
def contacts():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run(debug=True)

# app = Flask(__name__)
# @app.route('/')
# @app.route('/<name>/')
# def index(name="незнакомец"):
#     return f'Hello, {name}!'


# @app.route('/new/')
# def new():
#     return 'new page'

# @app.route('/')
# @app.route('/<password>/')
# def index(password=None):
#     if password=='1234':
#         return f'Доступ разрешен!'
#     else:
#         return 'Доступ запрещен!'

# @app.route('/')
# def html_func():
#     html = """
#     <h1>тестовый запуск локального сервера</h1>
#     <p>А это просто текст</p>
#     """
#     return html

