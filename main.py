from flask import Flask, render_template, redirect, request
from data.loginform import LoginForm
from data import db_session
from data.users import User
from data.add_date import Add_date


from data.user_function import user_func  # Отдельнвя функция инициализации базы данных
from ctypes  import *



app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

email = ''

@app.route('/', methods=['GET', 'POST'])
def login():

    global email

    form = LoginForm()
    
    print(form.email.data)
    if form.email.data == 'test@gmail.com':  # Проверка почты
        return redirect('/safespace')
    else:
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)

@app.route('/safespace', methods=['GET', 'POST'])
def SafeSpace():
    form = Add_date()
    ex =  request.form.get('text_box')
    print(ex)
    return render_template('safespace.html', title='koko') 

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')