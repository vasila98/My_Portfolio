from flask import render_template,redirect,url_for,request
# from admin.routes import blog,feedback,skills,project,
from run import app

@app.route('/')
def index():
    from models import Profile
    from models import Skills
    from models import Works
    from models import Testimonial
    prof= Profile.query.get(1)
    skills = Skills.query.all()
    works=Works.query.all()
    testimonial=Testimonial.query.all()
    return render_template("app/index.html",prof=prof,skills=skills,works=works,testimonial=testimonial)