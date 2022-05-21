from flask import Flask, render_template, request, flash, redirect, url_for
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from wtforms import IntegerField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Optional
from flask_bootstrap import Bootstrap

from calc1rm import Calc1rm
from squat_overload import squat_overload_func

import os


class InputForm(FlaskForm):
    weight = IntegerField(label='Weight', validators=[DataRequired()])
    reps = IntegerField(label='Reps', default=1, validators=[DataRequired()])
    workout = SelectField(label='Workout', choices=[('overload', 'Squat Overload'),
                                                    ('nothing', 'Nothing'),
                                                    ('also', 'Also Nothing')])
    submit = SubmitField(label='Submit')


class MaxForm(FlaskForm):
    new_max = IntegerField(label='New Max', validators=[DataRequired()])
    workout = SelectField(label='Workout', choices=[('squat', 'Squat'),
                                                    ('deadlift', 'Deadlift'),
                                                    ('bench', 'Bench'),
                                                    ('overhead', 'Overhead')])
    submit = SubmitField(label='Update Maxes (Blank = no change)')


class OneRmForm(FlaskForm):
    weight = IntegerField(label='Weight', validators=[DataRequired()])
    reps = IntegerField(label='Reps', validators=[DataRequired()])
    submit = SubmitField(label='Calculate')


# APP SETUP
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['flask_key']
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PG_DB_URL', 'sqlite:///users.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
Bootstrap(app)
login_manager = LoginManager()
login_manager.init_app(app)
db = SQLAlchemy(app)


# CREATE USER CONFIG FOR DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(1000), nullable=False)
    squat_max = db.Column(db.Integer, nullable=True)
    deadlift_max = db.Column(db.Integer, nullable=True)
    bench_max = db.Column(db.Integer, nullable=True)
    overhead_max = db.Column(db.Integer, nullable=True)


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['GET', 'POST'])
def home():
    program_form = InputForm()
    if program_form.validate_on_submit():
        weight = program_form.weight.data
        reps = program_form.reps.data
        calc = Calc1rm()
        one_rm = calc.calc_one_rm(weight=weight, reps=reps)
        max_dict = calc.max_reps
        if program_form.workout.data == 'overload':  # REPLACE WITH A DICT FUNC OF WORKOUT PLANS
            overload = squat_overload_func(one_rm=one_rm, max_dict=max_dict)
            return render_template('workout.html', days=overload, one_rm=one_rm)
        return render_template('index.html', form=program_form)
    return render_template('index.html', form=program_form)


@app.route('/calc_1rm', methods=['GET', 'POST'])
def one_rm():
    one_rm_form = OneRmForm()
    if one_rm_form.validate_on_submit():
        weight = one_rm_form.weight.data
        reps = one_rm_form.reps.data
        calc = Calc1rm()
        one_rm = calc.calc_one_rm(weight=weight, reps=reps)
        return render_template('one_rm.html', form=one_rm_form, one_rm=one_rm)
    return render_template('one_rm.html', form=one_rm_form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        if User.query.filter_by(email=request.form.get('email')).first():
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        new_user = User(
            email=request.form.get('email'),
            password=generate_password_hash(request.form.get('password'), method='pbkdf2:sha256', salt_length=8),
            name=request.form.get('name')
        )
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        flash('You were successfully logged in.')
        return redirect(url_for('my_page'))

    return render_template("register.html")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if not user:
            # Wrong user
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
            # Password incorrect
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            # All good
            login_user(user)
            flash('You were successfully logged in.')
            return redirect(url_for('my_page'))
    return render_template('login.html')


@app.route('/my_page', methods=['GET', 'POST'])
@login_required
def my_page():
    max_form = MaxForm()
    if max_form.validate_on_submit():
        if max_form.workout.data == 'squat':
            current_user.squat_max = max_form.new_max.data
            flash(f'Squat max updated!')
        if max_form.workout.data == 'deadlift':
            current_user.deadlift_max = max_form.new_max.data
            flash(f'Deadlift max updated!')
        if max_form.workout.data == 'bench':
            current_user.bench_max = max_form.new_max.data
            flash(f'Bench max updated!')
        if max_form.workout.data == 'overhead':
            current_user.overhead_max = max_form.new_max.data
            flash(f'Overhead max updated!')
        db.session.commit()
        return redirect((url_for('my_page')))
    return render_template('my_page.html', max_form=max_form)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logged out.')
    return redirect(url_for('home'))


if __name__ == '__main__':
    app.run(debug=True)
