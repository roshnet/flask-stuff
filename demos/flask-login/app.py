# Flask Login Demo..

from flask import Flask
from flask import session, url_for, redirect
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

app = Flask(__name__)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'unauth_message'
app.config['SECRET_KEY'] = 'some-secret-key'


@login_manager.user_loader
def load_user(user_id):
	return User(user_id)


class User(UserMixin):
	def __init__(self, id):
		self.id = id


@app.route('/')
def index():
	return '''
		<a href="/login/">Login</a>
		<br>
		<a href="/protected/">Protected</a>
		<br>
		<a href="/logout/">Log Out</a>
		<br>
	'''


@app.route('/unauth_message')
def unauth_message():
	return 'Man, did you just try to fuck this site?'


@app.route('/protected/')
@login_required
def protected():
	return 'This shit is protected.'


@app.route('/login/')
def login():
	login_user(User(1))
	return 'Logged In'


@app.route('/logout/')
def logout():
	logout_user()
	return 'Logged Out'


if __name__ == '__main__':
	app.run(debug=True)









