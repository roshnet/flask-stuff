
from flask import Flask
from flask import render_template, request

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
	return render_template('input.html')


@app.route('/process', methods=['GET', 'POST'])
def process():
	name = request.form['user-name']
	phone = request.form['user-phone']
	email = request.form['user-email']
	user_data = dict()
	user_data['name'] = name
	user_data['email'] = email
	user_data['phone'] = phone
	return render_template('output.html', data=user_data)


if __name__ == '__main__':
	app.run(debug=True)