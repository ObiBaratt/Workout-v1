from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from calc1rm import Calc1rm
from squat_overload import SquatWorkout


class InputForm(FlaskForm):
    weight = IntegerField(label='Weight', validators=[DataRequired()])
    reps = IntegerField(label='Reps', default=1, validators=[DataRequired()])
    submit = SubmitField(label='Submit')


def create_app():
    app = Flask(__name__)
    app.secret_key = "DSfajs ;j32j23pt"
    # Bootstrap(app)

    return app


app = create_app()


def squat_workouts(one_rm, max_dict):
    squat = SquatWorkout(one_rm=one_rm, max_dict=max_dict)
    return squat.day1(), squat.day2(), squat.day3()


@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if form.validate_on_submit():
        weight = form.weight.data
        reps = form.reps.data
        calc = Calc1rm()
        one_rm = calc.calc_one_rm(weight=weight, reps=reps)
        max_dict = calc.max_reps
        squat = SquatWorkout(one_rm=one_rm, max_dict=max_dict)
        return f'<h1>Day 1:</h1>{squat.day1()}' \
               f'<h1>Day 2:</h1>{squat.day2()}' \
               f'<h1>Day 3:</h1>{squat.day3()}'

    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
