from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
import csv


app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
# Not actual sensitive information, haha.
Bootstrap(app)


class CafeForm(FlaskForm):
    cafe = StringField('Cafe Name', validators=[DataRequired()])
    location = StringField('Cafe Location', validators=[DataRequired()], render_kw={"placeholder": "https://"})
    open = StringField('Opening Time (ex. 8AM)', validators=[DataRequired()])
    close = StringField('Closing Time (ex. 9PM)', validators=[DataRequired()])
    coffee_rating = SelectField('Coffee Rating', choices=[('☕', '☕'), ('☕☕', '☕☕'), ('☕☕☕', '☕☕☕'),
                                                          ('☕☕☕☕', '☕☕☕☕'), ('☕☕☕☕☕', '☕☕☕☕☕')])
    wifi_rating = SelectField('Wifi Strength Rating', validators=[DataRequired()],
                              choices=[('✘', '✘'), ('💪', '💪'), ('💪💪', '💪💪'), ('💪💪💪', '💪💪💪'),
                                       ('💪💪💪💪', '💪💪💪💪'), ('💪💪💪💪💪', '💪💪💪💪💪')])
    power = SelectField('Power Socket Availability', validators=[DataRequired()],
                        choices=[('✘', '✘'), ('🔌', '🔌'), ('🔌🔌', '🔌🔌'), ('🔌🔌🔌', '🔌🔌🔌'),
                                 ('🔌🔌🔌🔌', '🔌🔌🔌🔌'), ('🔌🔌🔌🔌🔌', '🔌🔌🔌🔌🔌')])
    submit = SubmitField('Submit')


@app.route("/")
def home():
    return render_template("index.html")


@app.route('/add', methods=['POST', 'GET'])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open('cafe-data.csv', 'a+', newline='') as file:
            file.write(f"{form.cafe.data},{form.location.data},{form.open.data},{form.close.data},"
                       f"{form.coffee_rating.data},{form.wifi_rating.data},{form.power.data}\n")
    return render_template('add.html', form=form)


@app.route('/cafes')
def cafes():
    with open('cafe-data.csv', newline='') as csv_file:
        csv_data = csv.reader(csv_file, delimiter=',')
        list_of_rows = []
        for row in csv_data:
            list_of_rows.append(row)
    return render_template('cafes.html', cafes=list_of_rows)


if __name__ == '__main__':
    app.run(debug=True)
