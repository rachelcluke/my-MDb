from flask import render_template, request, redirect, url_for
from my_mdb import app, db
from my_mdb.models import User

#Launch route
@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Auth route
@app.route("/auth")
def auth():
    return render_template("/pages/auth.html", title='Login')

#Register route
@app.route("/register")
def register():
    return render_template("/pages/register.html", title='Register')

#Main route (auth validation)
@app.route("/main", methods=("GET", "POST"))
def main():
    if request.method == "POST":
            user = User(username=request.form.get("username"))
            db.session.add(username)
            db.session.commit()
            return redirect(url_for("auth")) 
    return render_template("/pages/main.html", title='My Movies')
    
    """
    if form.validate_on_submit():
        try:
            user = MyMDB_Userser.query.filter_by(email=form.email.data).first()
            if check_password_hash(user.pwd, form.pwd.data):
                login_user(user)
            else:
                flash("Invalid username or password - please try again.", "login error")
        finally: return render_template("/pages/main.html", title='My Movies')
        """

"""
error = None
if form.validate_on_submit():
    try:
        user = MyMDB_Userser.query.filter_by(email=form.email.data).first()
        if check_password_hash(user.pwd, form.pwd.data):
            login_user(user)
            return redirect(url_for('/pages/main.html'))
        else:
            flash("Invalid username or password - please try again.", "login error")
    except Exception as e:
        flash(e, "login error")


@login_manager.user_loader
def load_user(user_id):
    return MyMDB_User.query.get(int(user_id))

@app.before_request
def session_handler():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=5)

#TODO - register route + logout session

"""