from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
app.app_context().push()


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    content = db.Column(db.Text)
    comments = db.relationship('Comment', backref='post')

    def __init__(self, title, content):
        self.title = title
        self.content = content


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id'))

    def __init__(self, content, post):
        self.content = content
        self.post_id = post.id


@app.route('/')
def index():
    post1 = Post(title='Primeiro post', content='Conteúdo do primeiro post')
    post2 = Post(title='Segundo post', content='Conteúdo do segundo post')
    post3 = Post(title='Terceiro post', content='Conteúdo do terceiro post')

    db.session.add_all([post1, post2, post3])
    db.session.commit()

    posts = Post.query.all()
    return render_template('index.html', posts=posts)


@app.route('/<int:id>/insere_comentario', methods=["GET", "POST"])
def insere_comentario(id):
    post = Post.query.filter_by(id=id).first()

    if request.method == 'POST':
        content = request.form.get('content')
        if content:
            comment = Comment(content=content, post=post)
            db.session.add(comment)
            db.session.commit()

            return redirect(url_for('lista_posts'))

    return render_template("novo_comentario.html", post=post)


@app.route('/posts')
def lista_posts():
    posts = Post.query.all()
    return render_template("posts.html", posts=posts)


if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)