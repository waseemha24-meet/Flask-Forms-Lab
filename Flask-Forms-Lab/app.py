from flask import Flask, jsonify, request, render_template, redirect, url_for
import random

app = Flask(  # Create a flask app
	__name__,
	template_folder='templates',  # Name of html file folder
	static_folder='static'  # Name of directory for static files
)


usernamex = "waseem"
passwordx = "123"


@app.route('/' , methods=['GET', 'POST'])  # '/' for the default page
def login():
	if request.method == 'POST':
		username=request.form['username']
		password=request.form['password']
		if usernamex == username and passwordx == password:
			return redirect(url_for('home'))
	else:
		return render_template('login.html')


facebook_friends=["Loai","Yonathan","Adan", "George", "Fouad", "Celina"]
@app.route('/home' , methods=['GET', 'POST'] , )
def home():
	return render_template('home.html' , friends = facebook_friends)


@app.route('/friend_axists/<string:name>' , methods=['GET', 'POST'])
def hello_name_route(name):
	return render_template('friend_exists.html' , methods=['GET', 'POST'] , facebook_friends=facebook_friends , name = name)

if __name__ == "__main__":  # Makes sure this is the main process
	app.run( # Starts the site
		debug=True
	)