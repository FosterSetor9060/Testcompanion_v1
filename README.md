TestCompanion Web App
Welcome to TestCompanion! This platform provides you with a range of powerful features to manage and customize your experience. Explore the following sections to make the most out of the application:

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)

## Features

1. **User Management**: 
   - User records of your company or business are properly managed.

2. **Question and answer setup**: 
   - Efficiently created question for test and administer them to applicants or students.

3. **Mail Settings**: 
   - Configure email forwarding seamlessly with the Email Setup feature.
     Ensure effective communication and streamline the forwarding of important messages.

4. **View Reports**: 
   - Detailed reports on test summary, each applicant/student's infomations e.g grade can be generated and viewed anytime.

5. **Email Notifications**: 
   - Both Admins and applicants receive automated email notifications when test is conducted ensuring up-to-date records.

6. **Attendance Management**: 
   - A comprehensive module allowing admins and staff to mark, set, and manage attendance entries efficiently.

7. **User-Friendly Dashboard**: 
   - An intuitive dashboard for tracking  Test and performance analytics.

## Technologies

- **Backend**: Flask (Python)
- **Database**: SQLAlchemy (MySQL)
- **Frontend**: HTML, CSS, JavaScript (Bootstrap)
- **Email Integration**: Flask-Mail for automated email notifications

## Installation

### Prerequisites

Ensure you have the following installed on your machine:
- Python 3.8+
- Virtualenv
- MySQL
- and othe dependencies in the requirements.txt file

### Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/FosterSetor9060/Testcompanion_v1
.git
   cd Testcompanion_v1


Setting up Database

CREATE database TestCompanion;
CREATE  user 'TestCompanion'@'localhost' identified by 'TestCompanion';


Create a virtual environment:
virtualenv venv
source venv/bin/activate


Install dependencies:
pip install -r requirements.txt
Set up your database and update the configuration in config.py.

Run the migrations to set up the database schema:

flask db upgrade
Start the development server:

flask run

Usage
 Users
The Users section allows you to efficiently manage user accounts. Designate roles, and organize users as per your system's requirements, users are the members who can create and manage their candidates and administer test to them accordlingly.

 Mail Settings
Configure email forwarding seamlessly with the Email Setup feature. Ensure effective communication and streamline the forwarding of important messages. Follow the provided steps to set up email server settings and optimize your email workflow.

 Tests
The Tests section is designed for applicants to complete assessments as part of the application process. Administer and manage tests efficiently, review results, and make informed decisions based on applicants' performances. This feature simplifies the evaluation process and enhances your recruitment procedures.

 Profile
Customize your personal profile in the Profile section. Update your details, change preferences, and tailor MainBoard to suit your needs. Your profile is your space on MainBoard, so make it uniquely yours.


API Endpoints

1. POST /attendance/<user_id>: Clock in staff for the day.
2. POST /clockInOut/<user_id>: Record clock-in and out time.
3. GET /attendancereport/<user_id>: Generate attendance reports.
4. POST /revokehourboard/<user_id>: Revoke an attendance record.
5. POST:GET:DELETE /userboard/<user_id> staff recods
6. POST:GET /profileboard/<user_id> Manage personal profile

Contributing

We welcome contributions to improve AttendanceHub! Here's how you can help:

Fork the project.

Create a feature branch: git checkout -b my-new-feature.
Commit your changes: git commit -m 'Add some feature'.
Push to the branch: git push origin my-new-feature.
Open a Pull Request.


Once the web app is running, you can access the different features by navigating to the respective sections:

Users: Manage user accounts, roles, and permissions.
Mail Settings: Configure email forwarding and communication settings.
Tests: Administer assessments for applicants and review test results.
Profile: Customize your personal profile and preferences.

