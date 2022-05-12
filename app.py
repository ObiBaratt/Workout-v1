from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired
from flask_bootstrap import Bootstrap
from calc1rm import MaxCalc
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


@app.route('/', methods=['GET', 'POST'])
def home():
    form = InputForm()
    if request.method == 'POST':
        return f'Do something.'
    else:
        return render_template('index.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
