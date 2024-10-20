import flask

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def html_func1():
    return render_template("TEST.html")
    #return render_template("index.html")

# @app.route('/blog/')
# def html_func2():
#     return (render_template("blog.html")
#
# @app.route('/contacts/'))
# def html_func3():
#     return render_template("contacts.html")

if __name__ == '__main__':
    app.run()


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

