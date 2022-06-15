# ask the application to import Flask module from flask package
from flask import Flask
from flask import render_template

# define instance of application
app = Flask(__name__)
# Home page
@app.route("/")
def home():
	return render_template('home.html', token = "Hello my first app in Flask+React")

# about us page
@app.route('/about')
def about():
	return "About us page"
# define function that will be executed if we access route
if __name__ == '__main__':
    app.run(debug=True)
