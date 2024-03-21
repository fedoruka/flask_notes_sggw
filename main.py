from flask import Flask, request, redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.sqlite'
app.config['SECRET_KEY'] = 'tutaj wartosc'
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), unique=True)
    password = db.Column(db.String(32))


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/notes', methods=['POST', 'GET'])
@login_required
def handle_notes():
    if request.method == 'POST':
        data = request.form
        note = Note(
            content=data["content"],
            user_id=current_user.id    
        )
        db.session.add(note)
        db.session.commit()
        return redirect(url_for("handle_notes"))
    elif request.method == 'GET':
        notes = Note.query.filter_by(user_id=current_user.id)
        return render_template('notes.html', notes=notes, user_name=current_user.username)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.form
        print(data['password'])
        hashed_password = generate_password_hash(data['password'], method='scrypt')
        new_user = User(username=data['username'], password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.form
        user = User.query.filter_by(username=data['username']).first()
        if not user or not check_password_hash(user.password, data['password']):
            return render_template('login.html')
        
        login_user(user)
        return redirect(url_for("handle_notes"))
    return render_template('login.html')

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    # with app.app_context():
    #     db.create_all()
    app.run(port=8000, debug=True)
