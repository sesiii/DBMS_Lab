# from flask import Flask, render_template, request, redirect, url_for, session, flash
# from flask_sqlalchemy import SQLAlchemy
# from werkzeug.security import generate_password_hash, check_password_hash

# app = Flask(__name__)
# app.secret_key = 'your_secret_key'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sesi@localhost/postgres'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# db = SQLAlchemy(app)

# # User Model
# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     dob = db.Column(db.Date, nullable=False)
#     phone = db.Column(db.String(15), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     caste = db.Column(db.String(20))
    
#     user_type = db.Column(db.String(20), nullable=False)  # admin, citizen, employee, monitor
#     password = db.Column(db.String(256), nullable=False)

# class citizens(db.Model):
#     citizen_id = db.Column(db.Integer, primary_key=True)
#     aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
#     first_name = db.Column(db.String(50), nullable=False)
#     last_name = db.Column(db.String(50), nullable=False)
#     date_of_birth = db.Column(db.Date, nullable=False)
#     phone = db.Column(db.String(15), nullable=False)
#     age = db.Column(db.Integer, nullable=False)
#     caste = db.Column(db.String(20))
#     gender = db.Column(db.String(10), nullable=False)
#     household_id = db.Column(db.Integer, nullable=False)
#     educational_qualification = db.Column(db.String(50))
#     occupation = db.Column(db.String(50))
#     marital_status = db.Column(db.String(20))
#     user_type = db.Column(db.String(20), nullable=False)  # admin, citizen, employee, monitor
#     password = db.Column(db.String(256), nullable=False)

# # Census Model
# class Census(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     year = db.Column(db.Integer, nullable=False)
#     population = db.Column(db.Integer, nullable=False)
#     demographics = db.Column(db.Text, nullable=False)
#     description = db.Column(db.Text)

# # Environmental Data
# class EnvironmentalData(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     issue_type = db.Column(db.String(50), nullable=False)
#     description = db.Column(db.Text)
#     report_date = db.Column(db.Date, nullable=False)
#     rainfall = db.Column(db.Float)
#     groundwater_level = db.Column(db.Float)
#     pollution_data = db.Column(db.Text)

# # Authentication Routes
# @app.route('/register', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         try:
#             aadhar_no = request.form['aadhar_no']
#             first_name = request.form['first_name']
#             last_name = request.form['last_name']
#             dob = request.form['dob']
#             phone = request.form['phone']
#             age = request.form['age']
#             caste = request.form['caste']
#             user_type = request.form['user_type']
#             password = generate_password_hash(request.form['password'])
#             new_user = User(aadhar_no=aadhar_no, first_name=first_name, last_name=last_name,
#                             dob=dob, phone=phone, age=age, caste=caste, user_type=user_type,
#                             password=password)
            
#             db.session.add(new_user)
#             db.session.commit()
#             flash('Registration successful!', 'success')
#             return redirect(url_for('login'))
#         except Exception as e:
#             db.session.rollback()
#             flash(f'Error: {e}', 'danger')
#             return redirect(url_for('register'))
#     return render_template('register.html')

# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         aadhar_no = request.form['aadhar_no']
#         password = request.form['password']
#         user = User.query.filter_by(aadhar_no=aadhar_no).first()
#         if user and check_password_hash(user.password, password):
#             session['user_id'] = user.id
#             session['user_type'] = user.user_type
#             flash('Login successful!', 'success')
#             return redirect(url_for('home'))
#         else:
#             flash('Invalid credentials', 'danger')
#     return render_template('login.html')

# @app.route('/home')
# def home():
#     return render_template('home.html')

# if __name__ == '__main__':
#     with app.app_context():
#         db.create_all()
#     app.run(debug=True)


from flask import Flask, render_template, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sesi@localhost/postgres'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class citizen_temp(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    caste = db.Column(db.String(20))
    gender = db.Column(db.String(10), nullable=False)
    household_id = db.Column(db.Integer, nullable=False)
    educational_qualification = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    marital_status = db.Column(db.String(20))
    password = db.Column(db.String(256), nullable=False)

class admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)

class panchayat_employee(db.Model):
    aadhar_no = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)




class citizens(db.Model):
    citizen_id = db.Column(db.Integer, primary_key=True)
    aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    caste = db.Column(db.String(20))
    gender = db.Column(db.String(10), nullable=False)
    household_id = db.Column(db.Integer, nullable=False)
    educational_qualification = db.Column(db.String(50))
    occupation = db.Column(db.String(50))
    marital_status = db.Column(db.String(20))
    user_type = db.Column(db.String(20), nullable=False)  # admin, citizen, employee, monitor
    password = db.Column(db.String(256), nullable=False)

# Census Model
class Census(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    demographics = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)



# Environmental Data
class EnvironmentalData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    report_date = db.Column(db.Date, nullable=False)
    rainfall = db.Column(db.Float)
    groundwater_level = db.Column(db.Float)
    pollution_data = db.Column(db.Text)

# Authentication Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            aadhar_no = request.form['aadhar_no']
            # if len(aadhar_no) != 12 or not aadhar_no.isdigit():
            #     flash('Aadhar number must be a 12-digit number', 'danger')
            #     return redirect(url_for('register'))
            
            # if citizen_temp.query.filter_by(aadhar_no=aadhar_no).first() or citizens.query.filter_by(aadhar_no=aadhar_no).first():
            #     flash('Aadhar number already exists', 'danger')
            #     return redirect(url_for('register'))
            
            first_name = request.form['first_name']
            
            phone = request.form['phone']
            # if len(phone) != 10 or not phone.isdigit():
            #     flash('Phone number must be a 10-digit number', 'danger')
            #     return redirect(url_for('register'))
            last_name = request.form['last_name']
            dob = request.form['dob']
            phone = request.form['phone']
            caste = request.form['caste']
            gender = request.form['gender']
            household_id = request.form['household_id']
            educational_qualification = request.form['educational_qualification']
            occupation = request.form['occupation'] 
            marital_status = request.form['marital_status']
            password = generate_password_hash(request.form['password'])
            new_user = citizen_temp(aadhar_no=aadhar_no, first_name=first_name, last_name=last_name,
                            dob=dob, phone=phone, caste=caste, gender=gender, household_id=household_id,
                            educational_qualification=educational_qualification, occupation=occupation, marital_status=marital_status,
                            password=password)
            
            
            db.session.add(new_user)
            db.session.commit()
            flash('Registration successful!', 'success')
            return redirect(url_for('login'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('register'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['user_id']
        password = request.form['password']
        user_type = request.form['user_type']
        user = None
        session['user_type'] = user_type
        if user_type == 'citizen':
            user = citizen_temp.query.filter_by(aadhar_no=id).first()
            #return redirect(url_for('citizen'))
        elif user_type == 'admin':
            user = admin.query.filter_by(id=id).first()
        elif user_type == 'panchayat_employee':
            user = panchayat_employee.query.filter_by(aadhar_no=id).first()
            #return redirect(url_for('panchayat_employee'))
        if user and check_password_hash(user.password, password):
            session['aadhar_no'] = user.id
            flash('Login successful!', 'success')
            if user_type == 'panchayat_employee':
                return redirect(url_for('panchayat_employee'))
            return redirect(url_for('citizen'))
        elif user_type == "admin" and password == user.password:
            session['user_id'] = user.id
            flash('Login successful!', 'success')   
            return redirect(url_for('admin_bhai'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/citizen')
def citizen():
    return render_template('citizen.html')

@app.route('/admin')
def admin_bhai():
    return render_template('admin.html')

@app.route('/panchayat_employee')
def panchayat_employee_dashboard():
    return render_template('panchayat_employee.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)