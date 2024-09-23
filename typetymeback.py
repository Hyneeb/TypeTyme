from flask import Flask, request, render_template, jsonify
import requests
from database import add_user, check_info, find_stats, update_stats

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route("/home.html")
def home1():
    return render_template("home.html")
@app.route('/home', methods = ['POST'])
def winner_winner():
    data = request.json
    wpm = round(data['wpm'])
    print(data['wins'])
    print(find_stats(data['name']))
    wins = find_stats(data['name'])[0] + data['wins']
    print(wins)
    update_stats({'wins': wins, 'name': data['name'], 'wpm': wpm})
    return jsonify({'message': 'congratulations, stats updated'})



@app.route('/signup.html')
def signup():
    return render_template('signup.html')

@app.route('/signup', methods=['POST'])
def handle_signup():
    data = request.json
    if add_user(data):
        return jsonify({"message": "User signed up successfully", 'value': True, 'name': data['username']})
    else:
        return jsonify({"message": "User was unable to sign up successfully", 'value': False, 'name': None})


@app.route("/login.html")
def login():
    return render_template('login.html')

@app.route("/login", methods = ['POST'])
def handle_login():
    # check_info() will return a number from 1-3
    # returning 1 means email not found
    # returning 2 means password doesn't match
    # returning 3 means everything is good
    data = request.json
    result = check_info(data)
    if result[0] == 1:
        return jsonify({"message": "This Email is not valid", 'value': False, 'name': None})
    elif result[0] == 2:
        return jsonify({'message': "Password is incorrect", 'value': False, 'name': None})
    else:
        return jsonify({'message': 'Login Successful', 'value': True, 'name': result[1]})
    
@app.route("/account.html")
def account():
    return render_template('account.html')

@app.route('/account', methods = ['POST'])
def stats():
    data = request.json
    print(data)
    stats = find_stats(data['name'])
    if stats:
        return jsonify({'wins': stats[0], 'WPM': stats[1], 'value': True})
    return jsonify({'wins': 0, 'WPM': 0, 'value': False})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)