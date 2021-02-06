from flask import Flask, redirect, render_template, url_for, flash
from flask_login import LoginManager, login_required, UserMixin, login_user, logout_user, current_user
from flask_sqlalchemy import SQLAlchemy
from forms import loginForm, registration
from werkzeug.security import generate_password_hash, check_password_hash

app=Flask(__name__)
app.config.from_pyfile('config.cfg')
login_manager=LoginManager()
login_manager.init_app(app)
login_manager.session_protection = 'strong'
login_manager.login_view='login'
db=SQLAlchemy(app)

# Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    emailID = db.Column(db.String(120), unique=True, nullable=False)
    mobileNo = db.Column(db.Integer, unique=True, nullable=False)
    passwd=db.Column(db.String(20), nullable=False)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route("/home")
@login_required
def index():
    return render_template('index.html', name=current_user.name)
@app.route('/')
@app.route("/register", methods=['POST', 'GET'])
def register():
    reg_form=registration()
    if reg_form.validate_on_submit():
        hashPass=generate_password_hash(reg_form.passwd.data, method='sha256')
        user=User(name=reg_form.name.data, userID=reg_form.userID.data\
            , emailID= reg_form.emailID.data, mobileNo=reg_form.mobileNo.data, passwd=hashPass)
        db.session.add(user)
        db.session.commit()
        flash('Account Created Successfully', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=reg_form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(userID=form.userID.data).first()
        if user:
            if check_password_hash(user.passwd, form.passwd.data):
                login_user(user)
                return redirect(url_for('index'))
        flash('Invalid Credentials', 'error')
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

if __name__=="__main__":
    app.run(debug=False, host='0.0.0.0', port=5000)
