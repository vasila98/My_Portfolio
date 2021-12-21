from flask import Flask, render_template, request, redirect

from run import app, db


import os

@app.route("/admin",methods=["GET","POST"])
def admin():
    from models import Profile
    from werkzeug.utils import secure_filename
    prof = Profile.query.all()
    if request.method=='POST':
        file = request.files['profile_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        prf=Profile(
            profile_name=request.form["profile_name"],
            about=request.form["about"],
            profile_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(prf)
        db.session.commit()
        return redirect("/")
    return render_template('admin/profile.html', prof=prof)


@app.route("/profDelete/<int:id>", methods=["GET","POST"])
def about_delete(id):
    from models import Profile
    from run import db
    import os
    prof = Profile.query.filter_by(id=id).first()
    
    filename = prof.profile_img
    os.unlink(os.path.join(filename))
    db.session.delete(prof)
    db.session.commit()
    return redirect ("/admin")


# Admin Skills
@app.route("/admin/skills",methods=["GET","POST"])
def skills():
    from models import Skills
    from run import db
    skills = Skills.query.all()
    if request.method=="POST":
        skills_title = request.form["skills_title"]
        skills_content = request.form["skills_content"]
        skills_class = request.form["skills_class"]
        skill = Skills(
            skills_title = skills_title,
            skills_content = skills_content,
            skills_class = skills_class
        )
        db.session.add(skill)
        db.session.commit()
        return redirect("/")
    return render_template("admin/skills.html", skills=skills)

@app.route("/skillDelete/<int:id>", methods=["GET","POST"])
def skill_delete(id):
    from models import Skills
    from run import db
    skills = Skills.query.filter_by(id=id).first()
    db.session.delete(skills)
    db.session.commit()
    return redirect ("/admin/skills")


@app.route("/admin/portfolio",methods=["GET","POST"])
def Works():
    from models import Works
    from run import db
    from werkzeug.utils import secure_filename
    import os
    works=Works.query.all()
    if request.method=="POST":
        file = request.files['work_img']
        filename= secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        work=Works(
            work_img= os.path.join(app.config['UPLOAD_FOLDER'], filename),
            work_name=request.form["work_name"]
        )
        db.session.add(work)
        db.session.commit()
        return redirect("/")
    return render_template('admin/portfolio.html', works=works) 

@app.route("/workDelete/<int:id>", methods=["GET","POST"])
def works_delete(id):
    from models import Works
    from run import db
    work = Works.query.filter_by(id=id).first()
    db.session.delete(works)
    db.session.commit()
    return redirect ("/admin/portfolio")    


@app.route("/admin/testimonial",methods=["GET","POST"])
def Testimonial():
    from models import Testimonial
    from werkzeug.utils import secure_filename
    testimonial = Testimonial.query.all()
    if request.method=='POST':
        file = request.files['client_img']
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        tst=Testimonial(
            client_text=request.form["client_text"],
            client_name=request.form["client_name"],
            client_img = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        )
        db.session.add(tst)
        db.session.commit()
        return redirect("/")
    return render_template('admin/testimonial.html', testimonal=testimonial)

@app.route("/tstDelete/<int:id>", methods=["GET","POST"])
def Testimonial_delete(id):
    from models import Testimonial
    from run import db
    import os
    testimonial = Testimonial.query.filter_by(id=id).first()
    
    filename = testimonial.client_img
    os.unlink(os.path.join(filename))
    db.session.delete(testimonial)
    db.session.commit()
    return redirect ("/admin/testimonial")   
  




        
# @app.route('/home')
# def home():
#     return render_template("admin/home.html")


# @app.route('/about')
# def about():
#     return render_template("admin/about.html") 

# @app.route('/portfolio')
# def portfolio():
#     return render_template("admin/portfolio.html")

# @app.route('/contact')
# def contact():
#     return render_template("admin/contact.html")           