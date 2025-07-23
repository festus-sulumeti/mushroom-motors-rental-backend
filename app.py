from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins="*", methods=["GET", "POST", "PUT", "DELETE"], allow_headers="*")




# Hardcoded admin credentials
ADMIN_EMAIL = 'admin@gmail.com'
ADMIN_PASSWORD = 'password'


@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    else:
        return jsonify({'success': False, 'message': 'Invalid credentials'}), 401


if __name__ == '__main__':
    app.run(debug=True)
