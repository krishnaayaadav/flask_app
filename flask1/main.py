from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
   # return '<h1>Welcome to flask home page</h1>'
   return render_template('home.html')

@app.route('/about-us')
def about_us():
   return '<h1>Welcome to about us page</h1>'


if __name__ == '__main__':
   app.run(debug=True)