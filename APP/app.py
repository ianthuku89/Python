from flask import Flask, render_template, request, redirect, url_for
import getpass

app = Flask(__name__)

# Your existing user_login function
def user_login(entered_password, user_info):
    if entered_password == user_info["Password"]:
        return True
    else:
        return False

# Routes for the login page
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/validate_login', methods=['POST'])
def validate_login():
    email = request.form['email']
    password = getpass.getpass("Enter your password for login: ")

    # Assuming you have a user_info dictionary (for simplicity, use a global variable here)
    user_info = {"Name": "John", "Email": "john@example.com", "Password": "password123"}

    if email == user_info["Email"] and user_login(password, user_info):
        return f"Login Successful! Welcome back, {user_info['Name']}"
    else:
        return "Invalid login credentials. Please try again."

if __name__ == '__main__':
    app.run(debug=True)
