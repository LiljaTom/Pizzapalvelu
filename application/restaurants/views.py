from application import app, db
from flask import render_template, request, redirect, url_for
from flask_login import login_required, current_user

from application.restaurants.models import Restaurant
from application.restaurants.forms import RestaurantForm

@app.route("/restaurants/new/")
def restaurants_form():
    return render_template("restaurants/new.html", form = RestaurantForm())

@app.route("/restaurants/", methods=["POST"])
def restaurants_create():
    form = RestaurantForm(request.form)

    if not form.validate():
        return render_template("restaurants/new.html", form = form)

    r = Restaurant(form.name.data)
    r.address = form.address.data
    r.city = form.city.data
    r.postcode = form.postcode.data
    r.account_id = current_user.id 

    db.session().add(r)
    db.session().commit()

    return redirect(url_for("restaurants_index"))

@app.route("/restaurants", methods=["GET"])
def restaurants_index():
    return render_template("restaurants/list.html", restaurants= Restaurant.query.all())