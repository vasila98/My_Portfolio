from run import db


class Profile(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    profile_img=db.Column(db.String(100))
    profile_name=db.Column(db.String(100))
    about=db.Column(db.Text)

    
class Skills(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    skills_title=db.Column(db.String(100))
    skills_content = db.Column(db.Text) 
    skills_class = db.Column(db.String(50))

class Works(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    work_img=db.Column(db.String(50))
    work_name=db.Column(db.String(100))

class Testimonial(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    client_text=db.Column(db.Text)
    client_name=db.Column(db.String(100))
    client_img=db.Column(db.String(100))


    
