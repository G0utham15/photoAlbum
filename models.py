class details(model):
    id = db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    emailID = db.Column(db.String(120), unique=True, nullable=False)
    mobileNo = db.Column(db.number(10), unique=True, nullable=False)
class cred(model):
    id = db.Column(db.Integer, primary_key=True)
    userID = db.Column(db.String(20), unique=True, nullable=False)
    passwd=db.Column(db.String(20), nullable=False)