from flask import render_template,redirect,url_for,request
# from admin.routes import blog,feedback,skills,project,
from run import app

@app.route('/')
def index():
    from models import Profile
    from models import Skills
    from models import Works
    from models import Testimonial
    from models import Contact
    prof= Profile.query.get(1)
    skills = Skills.query.all()
    works=Works.query.all()
    contact = Contact.query.all()
    testimonial=Testimonial.query.all()
    return render_template("app/index.html",prof=prof,skills=skills,works=works,testimonial=testimonial, contact=contact)

@app.route('/admin/contact', methods=['GET', 'POST'])
def Contact():

    from models import Contact
    from run import db
    contact = Contact.query.all()
    if request.method=="POST":
        user_name = request.form["user_name"]
        user_email = request.form["user_email"]
        user_message = request.form["user_message"]
        cnt = Contact(
            user_name = user_name,
            user_email =  user_email,
            user_message = user_message
        )
        db.session.add(cnt)
        db.session.commit()
        return redirect("/")
    return render_template("admin/contact.html", contact=contact)


@app.route("/contactDelete/<int:id>", methods=["GET","POST"])
def contact_delete(id):
    from models import Contact
    from run import db
    contact = Contact.query.filter_by(id=id).first()
    db.session.delete(contact)
    db.session.commit()
    return redirect ("/admin/contact")

      
    
