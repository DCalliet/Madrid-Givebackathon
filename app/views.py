from flask import render_template, flash, redirect, session, url_for, request, g
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, db, lm, oid
from forms import LoginForm, ContribForm
from models import User, Contributions 



@app.before_request
def before_request():
	g.user = current_user
	if g.user.is_authenticated():
		db.session.add(g.user)
		db.session.commit()

@lm.user_loader
def load_user(id):
	user = User.query.get(int(id))
	return user


@app.route('/')
@app.route('/index')
@login_required
def index():
	user = g.user
	me = User.query.get(user.id)
	print me
	contributions = Contributions.query.filter_by(contributor=me)
	contribs = []
	for cont in contributions:

		obj = {
			'desc': cont.name,
			'date': cont.date,
			'amount': cont.amount
		}
		contribs.append(obj)
		print contribs
	data = {'name':user.name, 'total': user.amount, 'contribs':contribs}
	return render_template('index.html', title="home", user=data)

@app.route('/impact')
@login_required
def impact():
	return render_template('impact.html', title="impact")

@app.route('/news')
@login_required
def news():
	return render_template('news.html', title="news")

@app.route('/give')
@login_required
def give():
	return render_template('give.html', title='give')

@app.route('/login', methods=['GET','POST'])
@oid.loginhandler
def login():
	if g.user is not None and g.user.is_authenticated():
		return redirect(url_for('index'))
	form = LoginForm()
	if form.validate_on_submit():
		session['remember_me'] = form.remember_me.data
		return oid.try_login(form.openid.data, ask_for=['nickname', 'email'])
	return render_template('login.html', form=form, providers=app.config['OPENID_PROVIDERS'], title='login')

@oid.after_login
def after_login(resp):

	if resp.email is None or resp.email == "":
		flash('Invalid login. Please try again.')
		return redirect(url_for('login'))
	user = User.query.filter_by(email=resp.email).first()
	if user is None:
		name = resp.nickname
		if name is None or name == "":
			name = resp.email.split('@')[0]
		user = User(name=name, email=resp.email, amount=0)
		db.session.add(user)
		db.session.commit()
	remember_me = False
	if 'remember_me' in session:
		remember_me = session['remember_me']
		session.pop('remember_me', None)
	login_user(user, remember = remember_me)
	return redirect(request.args.get('next') or url_for('index'))

@app.route('/logout')
def logout():
	logout_user()
	return redirect(url_for('index'))

@app.route('/contribute', methods=['GET', 'POST'])
@login_required
def contribute():
	user = g.user
	form = ContribForm()
	if form.validate_on_submit():
		amount = form.amount.data
		date = form.date.data
		cause = form.cause.data
		contrib = Contributions(contributor=user,name=cause,date=date,amount=amount)
		total = user.amount + amount
		user.amount = total
		db.session.add(contrib)
		db.session.commit()

	return render_template('contribute.html', title="secret", form=form)

