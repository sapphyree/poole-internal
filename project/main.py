# main.py

from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from . import db
from .models import User, Wiki_


main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/profile')
@login_required
def profile():
    return render_template('profile.html', name=current_user.name)


@main.route('/wiki/<wikiid>')
@login_required
def wiki(wikiid):

    wiki = Wiki_.query.filter_by(wikiid=wikiid).first()



    return render_template('wiki.html',wiki=wiki)



@main.route("/createWiki",methods=["POST"])
@login_required
def createWiki():
    title = request.form.get('title')
    image = request.form.get('image')
    description = request.form.get('description')


    # create new user with the form data. Hash the password so plaintext version isn't saved.
    new_wiki = Wiki_(title=title, image=image, description=description)

    # add the new user to the database
    db.session.add(new_wiki)
    db.session.commit()
    return redirect("/profile")