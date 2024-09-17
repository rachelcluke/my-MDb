from flask import render_template, request, redirect, url_for
from my_mdb import app, db
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from my_mdb.models import User, LoginForm, RegisterForm

#Launch route
@app.route("/")
def index():
    return render_template("/pages/launch.html")

#Auth route
@app.route("/auth", methods=['GET', 'POST'])
def auth():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('main'))
    return render_template("/pages/auth.html", title='Login', form=form)

#Register route
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    #password encryption
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data)
        new_user = User(username=form.username.data, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("auth"))

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

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for("auth"))
    
