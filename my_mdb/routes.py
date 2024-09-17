from flask import render_template, request, redirect, url_for
from my_mdb import app, db
from my_mdb.models import User

#Launch route
@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Auth route
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    form = LoginForm()
    return render_template("/pages/auth.html", title='Login', form=form)

#Register route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    return render_template("/pages/register.html", title='Register',form=form)

#Main route (auth validation)
@app.route("/main", methods=("GET", "POST"))
def main():
    if request.method == "POST":
            user = User(username=request.form.get("username"))
            db.session.add(username)
            db.session.commit()
            return redirect(url_for("auth")) 
    return render_template("/pages/main.html", title='My Movies')
    
