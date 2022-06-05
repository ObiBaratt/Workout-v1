from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField, SelectField, StringField, PasswordField
from wtforms.validators import DataRequired, Optional
from flask_ckeditor import CKEditor, CKEditorField


class InputForm(FlaskForm):
    weight = IntegerField(label='Weight', validators=[DataRequired()])
    reps = IntegerField(label='Reps', default=1, validators=[DataRequired()])
    # TODO: Add alternate workouts
    workout = SelectField(label='Workout', choices=[('overload', 'Squat Overload'),
                                                    ('nuckolsSquat', 'Nuckols Squat'),
                                                    ('nuckolsPress', 'Nuckols Press'),
                                                    ('nuckolsDeadlift', 'Nuckols Deadlift')])
    submit = SubmitField(label='Submit')


class MaxForm(FlaskForm):
    new_max = IntegerField(label='New Max', validators=[DataRequired()])
    exercise = SelectField(label='Exercise', choices=[('squat', 'Squat'),
                                                      ('deadlift', 'Deadlift'),
                                                      ('bench', 'Bench'),
                                                      ('overhead', 'Overhead')])
    submit = SubmitField(label='Update Maxes (Blank = no change)')


class OneRmForm(FlaskForm):
    weight = IntegerField(label='Weight', validators=[DataRequired()])
    reps = IntegerField(label='Reps', validators=[DataRequired()])
    submit = SubmitField(label='Calculate')


class RegisterForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    submit = SubmitField("Register")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class NoteForm(FlaskForm):
    notes = CKEditorField("Update Notes", validators=[DataRequired()])
    submit = SubmitField("Update Notes")
