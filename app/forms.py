from flask.ext.wtf import Form
from wtforms import StringField, BooleanField, IntegerField, DecimalField, DateField, SelectField
from wtforms.validators import DataRequired, Length

class LoginForm(Form):
	openid = StringField('openid', validators=[DataRequired()])
	remember_me = BooleanField('remember_me', default=False)

class ContribForm(Form):
	amount = IntegerField('amount', validators=[DataRequired()])
	date = DateField('date', format='%m/%d/%Y' ,validators=[DataRequired()])
	cause = StringField('cause', validators=[DataRequired()])
	cat = SelectField('cat', choices=[('education', 'education'), ('income', 'income'), ('health', 'health')], validators=[DataRequired()])

	