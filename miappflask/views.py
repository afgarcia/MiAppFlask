from flask import render_template, redirect, flash, url_for
from flask_login import login_required, login_user, logout_user, current_user

from miappflask import app
from miappflask.forms import AddArticuloForm, LoginForm, RegisterForm
from miappflask.models import db, User, Articulo


@app.route('/')
def index():
    return render_template('index.html', register_form=RegisterForm(), login_form=LoginForm())


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        user = User(username=form.username.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Tu cuenta ha sido creada')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user, True)
            return redirect(url_for('get_articulos'))
        flash('Usuario o contraseña inválida')
    return render_template('login.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    flash('Ha cerrado exitosamente la sesión.')
    return redirect(url_for('login'))


@app.route('/Articulos/<int:id>')
@login_required
def get_articulo(id):
    articulo = Articulo.query.filter_by(id=id).first()
    articulos = Articulo.query.filter_by(user=current_user).all()

    if articulo is None:
        return render_template('404.html'), 404
    if articulo.user != current_user:
        return render_template('403.html'), 403
    return render_template('articulo.html', articulo=articulo, articulos=articulos)


@app.route('/articulos')
@login_required
def get_articulos():
    articulos = Articulo.query.filter_by(user=current_user).all()
    return render_template('articulos.html', articulos=articulos)


@app.route('/add_articulo', methods=['GET', 'POST'])
@login_required
def add_articulo():
    form = AddArticuloForm()

    if form.validate_on_submit():
        articulo = Articulo(name=form.name.data, description=form.description.data)
        articulo.user = current_user
        db.session.add(articulo)
        db.session.commit()
        flash('Tu articulo ha sido guardado')
        return redirect(url_for('get_articulos'))
    return render_template('add_articulo.html', form=form)