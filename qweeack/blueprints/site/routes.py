from flask import Blueprint, render_template, redirect, request, flash

site = Blueprint('site', __name__, template_folder='site_templates')

@site.route("/")
def stocks():


    our_class = "Monitor all your Stocks"
    return render_template("stocks.html", coolmessage = our_class)








    
    