from flask import flash, request, render_template, jsonify, url_for, redirect, make_response
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_mail import Mail, Message
from api import app_views

@app_views.route('/sendcontactform', methods=['POST'])
def sendcontactform():
    app.config['MAIL_SERVER'] = 'smtp.mail.yahoo.com'
    app.config['MAIL_PORT'] = 587
    app.config['MAIL_USE_TLS'] = True
    app.config['MAIL_USE_SSL'] = False
    app.config['MAIL_USERNAME'] = 'luvpascal.ojukwu@yahoo.com'
    app.config['MAIL_PASSWORD'] = 'nvfolnadxvdepvxk'
    mail = Mail(app)
    json_data = request.json
    body = f"{json_data['message']} \n\nEmail: {json_data['email']}\n\nRegards,\n{json_data['name']} "
    msg = Message('Customer Mail', sender='luvpascal.ojukwu@yahoo.com', recipients=['luvpascal.ojukwu@yahoo.com'],body=body)
    mail.send(msg)
    response_data = {
                'status': 'success',
                'message': 'Thank you for reaching out to us, we have received your message, we will get in touch with you soon'
            }

    return jsonify(response_data), 200