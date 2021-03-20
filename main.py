from flask import Flask, render_template, redirect, request
from data.loginform import LoginForm
from data import db_session
from data.users import User
from data.registerform import RegisterForm

from data.safety import Security

from data.user_function import user_func  # Отдельнвя функция инициализации базы данных
from ctypes  import *
sp = Security.set_password  # Функция превращения пароля в хеш
ch = Security.check_password  # Функция проверки хеша и пароля


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

df = 'Москва, ул. Псковская, 11'
city = df  # Адрес школы
check1 = ''
check2 = ''
hash_password = ''
email = ''
flag_for_login = ''
money = 0


@app.route('/', methods=['GET', 'POST'])
def login():
    global flag_for_login
    global money
    global hash_password
    global email
    flag_for_login = False
    form = LoginForm()
    
    print(form.email.data)
    if form.email.data == 'test@gmail.com':  # Проверка почты
           
                
        return redirect('/safespace')

    else:
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')