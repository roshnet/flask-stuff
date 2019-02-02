# Flask Login Demo..

from flask import Flask
from flask import request, flash, render_template
from flask import session, url_for, redirect
from flask_login import (
    LoginManager,
    UserMixin,
    login_user,
    current_user,
    logout_user,
    login_required,
    login_url
)

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'
app.config['SECRET_KEY'] = 'some-secret-key'


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    if request.method == 'GET':
        return render_template('form.html')

    if request.method == 'POST':
        username = request.form['username']
        passwd = request.form['passwd']
        login_user(User(1))
        next_page = request.args.get('next')
        if not next_page:
            next_page = url_for('index')
        if username == 'admin' and passwd == 'admin':
            login_user(User(1))
            print('=========================================================')
            if User.is_authenticated:
                print('YES')
            else:
                print('NOO')
            print('=========================================================')
            return redirect(next_page)
        else:
            return redirect("{}?next={}".format(url_for('login'), next_page))


@app.route('/protected')
@login_required
def protected():
    return 'This shit is protected.'


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged Out'


if __name__ == '__main__':
    app.run(debug=True)
