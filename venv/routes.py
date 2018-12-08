# importing flask
from flask import Flask,request, render_template
#instanciating the application
app = Flask(__name__)

#setting up the routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses')
def courses():
    return render_template('courses.html')

@app.route('/categories')
def categories():
    return render_template('categories.html')

@app.route('/course_details')
def course_details():
    return render_template('courses-detail.html')

@app.route('/instructor')
def instuctor():
    return render_template('instructor.html')

@app.route('/instuctor_profile')
def instuctor_profile():
    return render_template('profile-teacher.html')

@app.route('/about')
def about():
    return render_template('about-us.html')

@app.route('/faq')
def faq():
    return render_template('faq.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')


if __name__ == '__main__':
	app.run(debug=True)
