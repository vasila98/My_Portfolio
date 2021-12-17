from flask import render_template,redirect,url_for,request
# from admin.routes import blog,feedback,skills,project,

@app.route('/')
def index():
    from models import Profile
    prof= Profile.query.all()
    return render_template("app/index.html",prof=prof)