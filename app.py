from flask import Flask, render_template, request, redirect, url_for
import time

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form.get('name')
        organization = request.form.get('organization')
        email = request.form.get('email')
        phone = request.form.get('phone')
        message = request.form.get('message')

        error_messages = {}
        if not name:
            error_messages['name'] = "Name is required"
        if not organization:
            error_messages['organization'] = "Organization name is required"
        if not email:
            error_messages['email'] = "Email is required"
        elif not email.count('@') == 1 or not email.count('.') >= 1:
            error_messages['email'] = "Invalid email format"
        if not phone:
            error_messages['phone'] = "Phone number is required"
        elif not phone.isdigit()==1 or len(phone)<10:
            error_messages['phone']="Invalid phone format"
        if not message:
            error_messages['message'] = "Message is required"

        if error_messages:
            return render_template('form.html', error_messages=error_messages, name=name, organization=organization, email=email, phone=phone, message=message)
        else:
            success_message="form submitted succesfully"
            # Process the form data (e.g., send email, store in database)
            return render_template('form.html', success_message=success_message)
    except Exception as e:
        return f"An error occurred: {e}"

if __name__ == '__main__':
    app.run(debug=True)
