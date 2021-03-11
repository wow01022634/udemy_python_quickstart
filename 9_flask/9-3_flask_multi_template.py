from flask import Flask
from flask import render_template

app=Flask(__name__)

@app.route('/')
def index():
    name = 'King'
    return render_template('index.html', title='Welcome', username=name,email='king@king.com')

@app.route('/about/')
def about():
    name = 'King'
    return render_template('about.html', title='Welcome', username=name,email='king@king.com')

if __name__=='__main__':
    app.run()