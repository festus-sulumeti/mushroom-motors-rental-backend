from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from config import DATABASE_CONFIG
from models import db, User, Car

app = Flask(__name__)

# Configure PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = (
    f"postgresql://{DATABASE_CONFIG['user']}:{DATABASE_CONFIG['pw']}"
    f"@{DATABASE_CONFIG['host']}:{DATABASE_CONFIG['port']}/{DATABASE_CONFIG['db']}"
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# CORS
CORS(app, supports_credentials=True)

# Init DB
db.init_app(app)

# ----------------- Admin Login -----------------
ADMIN_EMAIL = 'admin@gmail.com'
ADMIN_PASSWORD = 'password'

@app.route('/admin/login', methods=['POST'])
def admin_login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if email == ADMIN_EMAIL and password == ADMIN_PASSWORD:
        return jsonify({'success': True, 'message': 'Login successful'}), 200
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

# ----------------- Auth Routes -----------------
@app.route('/api/auth/signup', methods=['POST'])
def signup():
    data = request.get_json()
    name, email, password = data.get('name'), data.get('email'), data.get('password')

    if not all([name, email, password]):
        return jsonify({'success': False, 'message': 'Missing required fields'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'success': False, 'message': 'Email already registered'}), 409

    hashed_password = generate_password_hash(password)
    new_user = User(name=name, email=email, password_hash=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'success': True, 'message': 'User registered successfully'}), 201

@app.route('/api/auth/login', methods=['POST'])
def user_login():
    data = request.get_json()
    email, password = data.get('email'), data.get('password')

    if not email or not password:
        return jsonify({'success': False, 'message': 'Email and password are required'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({
            'success': True,
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'name': user.name,
                'email': user.email,
                'is_admin': user.is_admin
            }
        }), 200
    return jsonify({'success': False, 'message': 'Invalid credentials'}), 401

# ----------------- User Routes -----------------
@app.route('/api/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify({'users': [
        {'id': u.id, 'name': u.name, 'email': u.email, 'role': 'Admin' if u.is_admin else 'Customer'}
        for u in users
    ]}), 200

@app.route('/api/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({'success': False, 'message': 'User not found'}), 404

    db.session.delete(user)
    db.session.commit()
    return jsonify({'success': True, 'message': 'User deleted successfully'}), 200

@app.route('/api/users/count', methods=['GET'])
def get_user_count():
    count = User.query.count()
    return jsonify({'count': count}), 200

# ----------------- Car Routes -----------------
@app.route('/api/cars', methods=['GET'])
def get_cars():
    cars = Car.query.all()
    return jsonify({'cars': [
        {'id': c.id, 'name': c.name, 'model': c.model, 'status': c.status}
        for c in cars
    ]}), 200

@app.route('/api/cars', methods=['POST'])
def add_car():
    data = request.get_json()
    name, model, status = data.get('name'), data.get('model'), data.get('status', 'Available')

    if not name or not model:
        return jsonify({'success': False, 'message': 'Missing name or model'}), 400

    new_car = Car(name=name, model=model, status=status)
    db.session.add(new_car)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Car added successfully', 'car': {
        'id': new_car.id, 'name': new_car.name, 'model': new_car.model, 'status': new_car.status
    }}), 201

@app.route('/api/cars/<int:car_id>', methods=['DELETE'])
def delete_car(car_id):
    car = Car.query.get(car_id)
    if not car:
        return jsonify({'success': False, 'message': 'Car not found'}), 404

    db.session.delete(car)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Car deleted successfully'}), 200

@app.route('/api/cars/<int:car_id>', methods=['PUT'])
def update_car(car_id):
    car = Car.query.get(car_id)
    if not car:
        return jsonify({'success': False, 'message': 'Car not found'}), 404

    data = request.get_json()
    car.name = data.get('name', car.name)
    car.model = data.get('model', car.model)
    car.status = data.get('status', car.status)

    db.session.commit()
    return jsonify({'success': True, 'message': 'Car updated successfully'}), 200

@app.route('/api/cars/count', methods=['GET'])
def get_car_count():
    count = Car.query.count()
    return jsonify({'count': count}), 200

# ----------------- Run Server -----------------
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
