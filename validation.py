# TODO - Validate data via backend before displaying data to frontend

def check_for_empty_field(string, redirect_link):
    if string == "":
        flash("Field cannot be empty")
        return redirect(url_for(redirect_link))