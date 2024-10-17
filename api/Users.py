from flask import flash, request, render_template, jsonify, url_for, redirect, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from api import app_views



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