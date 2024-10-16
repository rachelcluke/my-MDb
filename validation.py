from flask import flash, render_template, request, redirect, url_for, session

def check_for_empty_field(string, redirect_link):
    if string == "":
        flash("Field cannot be empty")
        return redirect(url_for(redirect_link))