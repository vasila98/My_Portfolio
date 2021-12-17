from flask import Flask, render_template


from run import app

@app.route("/admin",methods=["GET","POST"])
def admin():
    from models import Profile
    from run import db
    about = Profile.query.all()
    if request.method=="POST":
        profile_name = request.form["profile_name"]
        profile_name = request.form["skills_content"]
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