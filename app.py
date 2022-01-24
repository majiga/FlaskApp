from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

@app.route('/diversity/')
def diversity():
    return render_template('diversity.html')

@app.route('/leadership/')
def leadership():
    return render_template('leadership.html')

@app.route('/about/')
def about():
    return render_template('about.html', utc_dt=datetime.datetime.utcnow())


if __name__ == "__main__":
    app.run(debug=True)