from flask import Flask, render_template, redirect, url_for
from forms import registration, loginForm
from flask_login import LoginManager, login_required
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, insert, select
app=Flask(__name__)
app.config['SECRET_KEY']="AA1D1644C4313521A74D6F6D75966"
#login_manager=LoginManager()
#login_manager.init_app(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///auth.db'

db=SQLAlchemy(app)
dbengine=create_engine('sqlite:///auth.db')
# Models
class details(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    emailID = db.Column(db.String(120), unique=True, nullable=False)
    mobileNo = db.Column(db.Integer, unique=True, nullable=False)
class cred(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    passwd=db.Column(db.String(20), nullable=False)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/register", methods=['POST', 'GET'])
def register():
    reg_form=registration()
    if reg_form.validate_on_submit():
        #detail=details(name=reg_form.name, userID=reg_form.userID, emailID= reg_form.emailID, mobileNo=reg_form.mobileNo)
        #creds=cred(userID= reg_form.userID, passwd=reg_form.passwd)
        
    
        dbengine.execute("insert into details(name, userID, emailID, mobileNo) values ('{}', '{}', '{}', {});".format(reg_form.name.data, reg_form.userID.data, reg_form.emailID.data, reg_form.mobileNo.data))
        dbengine.execute("insert into cred(userID, passwd) values ('{}', '{}');".format(reg_form.userID.data, reg_form.passwd.data))
        return redirect(url_for('login'))
    return render_template('register.html', form=reg_form)

@app.route("/login", methods=['POST', 'GET'])
def login():
    form=loginForm()
    if form.validate_on_submit():
        try:
            data=list(dbengine.execute("select userID, passwd from cred where userID='{}';".format(form.userID.data)))
            if data[0][0]==form.userID.data:
                if data[0][1]==form.passwd.data:
                    return redirect('/')
        except:
            pass
        return redirect(url_for('login'))
    return render_template('login.html', form=form)

if __name__=="__main__":
    app.run(debug=True)