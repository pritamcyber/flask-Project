
from flaskblog import db,login_managers
from flask_login import UserMixin

@login_managers.user_loader
def load_user(user_id):
    return user.query.get(int(user_id))
class user(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=False, nullable=False)
    last_name = db.Column(db.String(20), unique=False, nullable=False)
      
    email = db.Column(db.String(120), unique=True, nullable=False)
    image_file = db.Column(db.String(20), nullable=False, default='person.png')
    job = db.Column(db.String(50), nullable=True )
    phone_no = db.Column(db.String(20),unique=True, nullable=False, default='9910020341')

    password = db.Column(db.String(60), nullable=False)
    work_experience = db.relationship('WorkExperience', backref='user_experience', lazy=True)
    education = db.relationship('Education', backref='user_education', lazy=True)
    Skill = db.relationship('Skill', backref='user_skill', lazy=True)


    def __repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class Education(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    education = db.Column(db.String(100), nullable=False)
    year_from = db.Column(db.String(50),nullable=False)
    year_to = db.Column(db.String(50),nullable=False)
    insitute = db.Column(db.String(50),nullable = True,default = 'Self')
    address = db.Column(db.Text, nullable=True)
    dicription = db.Column(db.Text, nullable=True)
                                                                               
    user_id1 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Education('{self.education}')"

class Skill(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    skill_of = db.Column(db.String(100), nullable=False)
    level  = db.Column(db.Integer, nullable=True, default=3)
    dicription = db.Column(db.Text, nullable=True)
    user_id2 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Skill('{self.skill_of}')"

class WorkExperience(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    experience_of = db.Column(db.String(100), nullable=False)#this shows what kind of experiece do you have like poste or desgination 

    year_from = db.Column(db.String(50),nullable=False)
    year_to = db.Column(db.String(50),nullable=False) # this show how long you have worked like that 

    work_dicription = db.Column(db.Text,nullable = True)# this shows discription of that work 
    experience_at  = db.Column(db.String(100), nullable=False, default="Private Limited")#this shows where do you get that experience from like office name 
    # dicription = db.Column(db.Text, nullable=True)
    user_id3 = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"WorkExperience('{self.experience_of}', '{self.work_dicription}')"

    