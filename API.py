from flask import Flask, request, jsonify
import re

app = Flask(__name__)

def is_valid_email(email):
    # Vérification simple de l'email
    regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(regex, email) is not None

@app.route('/check_email', methods=['POST'])
def check_email():
    data = request.json
    email = data.get('email', '')
    if is_valid_email(email):
        return jsonify({'status': 'valid', 'email': email}), 1
    else:
        return jsonify({'status': 'invalid', 'email': email}), 0

if __name__ == '__main__':
    app.run(debug=True)
