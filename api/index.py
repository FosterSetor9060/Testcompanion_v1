from flask import flash, request, render_template, jsonify, url_for, redirect, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from api import app_views
from model import User, Company



@app_views.route('/home', methods=['GET'])
def home():
    return render_template('index.html')

@app_views.route('/home', methods=['GET'])
@app_views.route('/', methods=['GET'])
def homepage():
    return render_template('index.html')


@app_views.route('/about', methods=['GET'])
def about():
    return render_template('About.html')

@app_views.route('/contact', methods=['GET'])
def contact():
    return render_template('Contact.html')

@app_views.route('/features', methods=['GET'])
def features():
    return render_template('Features.html')

@app_views.route('/signup', methods=['GET'])
def signup():
    return render_template('Signup.html')

@app_views.route('/signin', methods=['GET'])
def signin():
    logout_user()
    return render_template('Signin.html')

@app_views.route('/profileboard/<user_id>', methods=['GET'])
@login_required
def profileboard(user_id):
    user = User.query.filter_by(userid=user_id).first()
    if user:
        com = Company.query.filter_by(companyid=user.company_id).first()
        return render_template('profiledashboard.html',
                               companyname=com.company_name,
                               addr=com.company_address,
                               com_email=com.company_email,
                               email=user.email,
                               web=com.company_website,
                               fn=user.first_name,
                               ln=user.last_name,
                               role=user.role,
                               user_id=user_id)

