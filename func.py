from flask import Flask, render_template, request, redirect, url_for, flash
from base import app, db, User


def index():
    add_user()
    return render_template('index.html')


def view_users():
    users_list = User.query.all()
    return render_template('view_users.html', users_list=users_list)


def add_user():
    if request.method == 'POST':

        user = User.query.filter_by(first_name=request.form.get('first_name')).first()
        email = User.query.filter_by(email=request.form.get('email')).first()
        if user is None and email is None:

            first_name = request.form.get('first_name')
            last_name = request.form.get('last_name')
            email = request.form.get('email')
            new_user = User(first_name=first_name,
                            last_name=last_name,
                            email=email)
            try:
                db.session.add(new_user)
                db.session.commit()
                flash(f'Привіт, {request.form.get("first_name")}'
                      f' {request.form.get("last_name")}')
                return view_users()
            except:
                return 'Ошибка добавления'
        else:
            flash(f'Вже бачилися,{request.form.get("first_name")}')
