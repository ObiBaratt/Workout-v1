from flask import Flask, render_template, request, flash, redirect, url_for

from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user
from flask_ckeditor import CKEditor
from flask_bootstrap import Bootstrap
import os

from inputcleaner import strip_invalid_html
from calc1rm import Calc1rm
from workouts import *
from forms import *

import datetime
current_year = datetime.datetime.today().year

# APP SETUP
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['flask_key']
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('PG_DB_URL', 'sqlite:///users.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    Bootstrap(app)
    return app


app = create_app()
login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)

ckeditor = CKEditor(app)

@app.context_processor
def global_variables():
    return dict(year=current_year)

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
    notes = db.Column(db.String(50000), default='Your notes go here.')
    # workouts = db.Column(db.String(50000), default='[Squat, 1000000]')


db.create_all()


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/programs', methods=['GET', 'POST'])
def programs():
    program_form = InputForm()
    if program_form.validate_on_submit():
        weight = program_form.weight.data
        reps = program_form.reps.data
        calc = Calc1rm()
        one_rm = calc.calc_one_rm(weight=weight, reps=reps)
        # TODO: REPLACE WITH A DICT FUNC OF WORKOUT PLANS
        if program_form.workout.data == 'overload':
            program = SquatOverload(one_rm=one_rm)
            workout = program.return_workouts()
            return render_template('workout.html', days=workout, one_rm=one_rm, name=program.__class__.__name__)
        elif program_form.workout.data == 'nuckolsSquat':
            program = NuckolsSquat(one_rm=one_rm)
            workout = program.return_workouts()
            return render_template('workout.html', days=workout, one_rm=one_rm, name=program.__class__.__name__)
        elif program_form.workout.data == 'nuckolsPress':
            program = NuckolsPress(one_rm=one_rm)
            workout = program.return_workouts()
            return render_template('workout.html', days=workout, one_rm=one_rm, name=program.__class__.__name__)
        elif program_form.workout.data == 'nuckolsDeadlift':
            program = NuckolsDeadlift(one_rm=one_rm)
            workout = program.return_workouts()
            return render_template('workout.html', days=workout, one_rm=one_rm, name=program.__class__.__name__)
        return render_template('programs.html', form=program_form)
    return render_template('programs.html', form=program_form)


@app.route('/about')
def about():
    home_url = url_for('home')
    return f'<h1>Currently Under Construction...Return <a href="{home_url}">to the Home page.</a>'


@app.route('/calc_1rm', methods=['GET', 'POST'])
def one_rm():
    one_rm_form = OneRmForm()
    if one_rm_form.validate_on_submit():
        weight = one_rm_form.weight.data
        reps = one_rm_form.reps.data
        calc = Calc1rm()
        one_rm = calc.calc_one_rm(weight=weight, reps=reps)
        return render_template('one_rm.html', form=one_rm_form, one_rm=one_rm, calc=calc)
    return render_template('one_rm.html', form=one_rm_form)


@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(
            email=form.email.data,
            name=form.name.data,
            password=generate_password_hash(form.password.data, method='pbkdf2:sha256', salt_length=8,)
        )
        db.session.add(new_user)
        db.session.commit()
        login_user(new_user)
        flash('You were successfully logged in')
        return redirect(url_for("my_page"))
    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if not user:
            # Wrong user
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
            # Password incorrect
        elif not check_password_hash(user.password, form.password.data):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            # All good
            login_user(user, remember=True)
            flash('You were successfully logged in', "success")
            return redirect(url_for('my_page'))
    return render_template('login.html', form=form)


@app.route('/testing', methods=['GET', 'POST'])
@login_required
def testing():
    max_form = MaxForm()
    notes = NoteForm(notes=current_user.notes)
    if max_form.submit.data and max_form.validate_on_submit():
        if max_form.exercise.data == 'squat':
            print(max_form.new_max.data)
            current_user.squat_max = max_form.new_max.data
            flash(f'Squat max updated!')
        elif max_form.exercise.data == 'deadlift':
            current_user.deadlift_max = max_form.new_max.data
            flash(f'Deadlift max updated!')
        elif max_form.exercise.data == 'bench':
            current_user.bench_max = max_form.new_max.data
            flash(f'Bench max updated!')
        elif max_form.exercise.data == 'overhead':
            current_user.overhead_max = max_form.new_max.data
            flash(f'Overhead max updated!')
        db.session.commit()
        return redirect((url_for('testing')))
    elif notes.validate_on_submit():
        current_user.notes = strip_invalid_html(notes.data['notes'])
        flash(f'Noted!')
        db.session.commit()
        return redirect((url_for('testing', id='notetab')))
    return render_template('testing.html', max_form=max_form, notes=notes)


@app.route('/my_page', methods=['GET', 'POST'])
@login_required
def my_page():
    max_form = MaxForm()
    notes = NoteForm(notes=current_user.notes)
    if max_form.submit.data and max_form.validate_on_submit():
        if max_form.exercise.data == 'squat':
            print(max_form.new_max.data)
            current_user.squat_max = max_form.new_max.data
            flash(f'Squat max updated!')
        elif max_form.exercise.data == 'deadlift':
            current_user.deadlift_max = max_form.new_max.data
            flash(f'Deadlift max updated!')
        elif max_form.exercise.data == 'bench':
            current_user.bench_max = max_form.new_max.data
            flash(f'Bench max updated!')
        elif max_form.exercise.data == 'overhead':
            current_user.overhead_max = max_form.new_max.data
            flash(f'Overhead max updated!')
        db.session.commit()
        return redirect((url_for('my_page')))
    elif notes.validate_on_submit():
        current_user.notes = strip_invalid_html(notes.data['notes'])
        flash(f'Noted!')
        db.session.commit()
        return redirect((url_for('my_page')))
    return render_template('my_page.html', max_form=max_form, notes=notes)


@app.route('/logout')
def logout():
    logout_user()
    flash('You were successfully logged out.')
    return redirect(url_for('home'))


@login_manager.unauthorized_handler
def unauthorized():
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
