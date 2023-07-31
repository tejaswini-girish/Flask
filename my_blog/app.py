from flask import Flask, jsonify, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

from sqlalchemy.sql import func

app = Flask(__name__)


@app.route('/')
def index():
    posts = Blogpost.query.all()
    return render_template('index.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:post_id>')
def post(post_id):
    post = Blogpost.query.filter_by(id=post_id).one()
    return render_template('post.html', post=post)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/addpost', methods=['POST'] )
def addpost():
    title = request.form['title']
    subtitle = request.form['subtitle']
    author = request.form['author']

    post = Blogpost(title=title, subtitle=subtitle, author=author, date_posted=datetime.now())

    db.session.add(post)
    db.session.commit()
    return redirect(url_for('index'))







app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Teju-1998@localhost/my_blog'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Blogpost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    subtitle = db.Column(db.String(50))
    author = db.Column(db.String(20))
    date_posted = db.Column(db.DateTime)
    content = db.Column(db.Text)
    
with app.app_context():
    db.create_all()

    # db.session.add(UserInfo('admin'))
    # db.session.commit()

    # users = UserInfo.query.all()
    # print(users)


if __name__ == "__main__":
    app.run(debug=True)
    