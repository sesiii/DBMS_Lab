

from flask import Flask, render_template, request, redirect, url_for, session, flash, jsonify
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import inspect, or_, cast, String, distinct

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sesi@localhost/postgres'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://22CS10038:Qsxnkpwdc%402005@10.5.18.70:5432/22CS10038'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    caste = db.Column(db.String(20))
    user_type = db.Column(db.String(20), nullable=False)  # admin, citizen, employee, monitor
    password = db.Column(db.String(256), nullable=False)

    # Tax Model
class Tax(db.Model):
        id = db.Column(db.Integer, primary_key=True)
        citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.citizen_id'), nullable=False)
        amount = db.Column(db.Float, nullable=False)
        year = db.Column(db.Integer, nullable=False)
        description = db.Column(db.Text, nullable=True)

class households(db.Model):
    household_id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(200), nullable=True)
    

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
    citizen_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    role=db.Column(db.String(20), nullable=False)

class panchayat_employee_request(db.Model):
    citizen_id = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(256), nullable=False)
    role=db.Column(db.String(20), nullable=False)
    
class citizens(db.Model):
    citizen_id = db.Column(db.Integer, primary_key=True)
    aadhar_no = db.Column(db.String(12), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    date_of_birth = db.Column(db.Date, nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)  # Updated column name
    caste = db.Column(db.String(20), nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    household_id = db.Column(db.Integer, nullable=False)
    educational_qualification = db.Column(db.String(50), nullable=True)
    occupation = db.Column(db.String(50), nullable=True)
    marital_status = db.Column(db.String(20), nullable=True)
    password = db.Column(db.String(256), nullable=True)
    # user_type = db.Column(db.String(20), nullable=False)

# Census Model
class census(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    population = db.Column(db.Integer, nullable=False)
    demographics = db.Column(db.Text, nullable=False)
    description = db.Column(db.Text)

# Environmental Data
class environmental_data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    issue_type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    report_date = db.Column(db.Date, nullable=False)
    rainfall = db.Column(db.Float, nullable=True)
    groundwater_level = db.Column(db.Float, nullable=True)
    pollution_data = db.Column(db.Text, nullable=True)

    # Welfare Schemes Model
class welfare_schemes(db.Model):
    scheme_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(200))
    eligibility = db.Column(db.String(200))
    benefits = db.Column(db.String(200))
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)

# Scheme Enrollments Model
class scheme_enrollments(db.Model):
    enrollment_id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.citizen_id'))
    scheme_id = db.Column(db.Integer, db.ForeignKey('welfare_schemes.scheme_id'))

    enrollment_date = db.Column(db.Date, nullable=False)
# Service Model
class service(db.Model):
    service_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200))
    request_date = db.Column(db.Date)


    # Income Model
class income(db.Model):
    income_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric, nullable=False)
    income_date = db.Column(db.Date, nullable=False)
    source = db.Column(db.String(200))
    financial_year = db.Column(db.String(200))
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.citizen_id'))

# Expenditure Model
class expenditure(db.Model):
    expenditure_id = db.Column(db.Integer, primary_key=True)
    amount = db.Column(db.Numeric, nullable=False)
    expenditure_date = db.Column(db.Date, nullable=False)
    purpose = db.Column(db.String(200))
    category = db.Column(db.String(200))
    payment_mode = db.Column(db.String(200))
    financial_year = db.Column(db.String(200))

# Vaccinations Model
class vaccinations(db.Model):
    vaccination_id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer, nullable=False)
    vaccine_type = db.Column(db.String(200), nullable=False)
    date = db.Column(db.Date, nullable=False)

# Assets Model
class assets(db.Model):
    asset_id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(200), nullable=False)
    value = db.Column(db.Numeric, nullable=False)
    location = db.Column(db.String(200))
    name = db.Column(db.String(200))
    installation_date = db.Column(db.Date)

# Land Records Model
class land_records(db.Model):
    land_id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer)
    area_acres = db.Column(db.Numeric, nullable=False)
    crop_type = db.Column(db.String(200))

# Service Requests Model
class service_requests(db.Model):
    request_id = db.Column(db.Integer, primary_key=True)
    citizen_id = db.Column(db.Integer, db.ForeignKey('citizens.citizen_id'))
    service_id = db.Column(db.Integer, db.ForeignKey('service.service_id'))
    request_date = db.Column(db.Date, nullable=False)
    status = db.Column(db.String(200))
    description = db.Column(db.Text)
    type = db.Column(db.String(256))
    
def get_citizen_details(citizen_id):
    try:
        citizen = citizens.query.filter_by(citizen_id=citizen_id).first()
        if citizen:
            return {
                'user_id': citizen.citizen_id,
                'aadhar_no': citizen.aadhar_no,
                'first_name': citizen.first_name,
                'last_name': citizen.last_name,
                'date_of_birth': citizen.date_of_birth,
                'phone_number': citizen.phone_number,
                'caste': citizen.caste,
                'gender': citizen.gender,
                'household_id': citizen.household_id,
                'educational_qualification': citizen.educational_qualification,
                'occupation': citizen.occupation,
                'marital_status': citizen.marital_status
            }
        return None
    except Exception as e:
        print(e)
        return None
# Helper function to get all table names from the database
def get_all_tables():
    inspector = inspect(db.engine)
    return inspector.get_table_names()

# Helper function to get table data
def get_table_data(table_name):
    try:
        # Get table class from the model classes
        model_class = None
        for cls in [User, citizen_temp, admin, panchayat_employee, citizens, census, environmental_data,panchayat_employee_request,Tax,welfare_schemes,service,service_requests,income,expenditure,assets,land_records, vaccinations, scheme_enrollments, households]:
            if cls.__tablename__ == table_name:
                model_class = cls
                break
        
        if model_class:
            # Get column names
            columns = [column.name for column in model_class.__table__.columns]
            
            # Get rows
            rows = []
            query_result = db.session.query(model_class).all()
            for item in query_result:
                row = []
                for column in columns:
                    row.append(getattr(item, column))
                rows.append(row)
            
            return {
                'name': table_name,
                'columns': columns,
                'rows': rows
            }
        return None
    except Exception as e:
        print(f"Error getting table data: {e}")
        return None

@app.route('/add_income/<int:citizen_id>', methods=['POST'])
def add_income(citizen_id):
    try:
        new_income = income(
            amount=request.form['amount'],
            income_date=datetime.now(),
            source=request.form['source'],
            financial_year=request.form['financial_year'],
            citizen_id=citizen_id
        )
        db.session.add(new_income)
        db.session.commit()
        flash('Income information added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('citizen'))

@app.route('/add_land_record/<int:citizen_id>', methods=['POST'])
def add_land_record(citizen_id):
    try:
        new_land_record = land_records(
            citizen_id=citizen_id,
            area_acres=request.form['area_acres'],
            crop_type=request.form['crop_type']
        )
        db.session.add(new_land_record)
        db.session.commit()
        flash('Land record added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('citizen'))

@app.route('/search_table', methods=['POST'])
def search_table():
    try:
        table_name = request.form.get('table_name')
        search_term = request.form.get('search_term')
        
        if not table_name or not search_term:
            return jsonify({'error': 'Missing parameters'}), 400

        # Get the appropriate model class based on table name
        model_class = None
        for cls in [User, citizen_temp, admin, panchayat_employee, citizens, census, 
                   environmental_data, panchayat_employee_request, Tax, welfare_schemes,
                   service, service_requests, income, expenditure, assets, land_records, 
                   vaccinations, scheme_enrollments, households]:
            if cls.__tablename__ == table_name:
                model_class = cls
                break
        
        if not model_class:
            return jsonify({'error': 'Invalid table name'}), 400

        # Get all columns of the table
        columns = [column.key for column in model_class.__table__.columns]
        
        # Build dynamic query for searching across all columns
        search_filters = []
        for column in columns:
            # Convert the column value to string for searching
            search_filters.append(
                cast(getattr(model_class, column), String).ilike(f'%{search_term}%')
            )
            
        # Execute the search query
        results = db.session.query(model_class).filter(or_(*search_filters)).all()
        
        # Format results
        formatted_results = []
        for result in results:
            row = []
            for column in columns:
                value = getattr(result, column)
                # Convert special types to string for JSON serialization
                if isinstance(value, (datetime, Decimal, date)):
                    value = str(value)
                row.append(value)
            formatted_results.append(row)

        return jsonify({
            'name': table_name,
            'columns': columns,
            'rows': formatted_results
        })

    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/add_scheme_enrollment/<int:citizen_id>', methods=['POST'])
def add_scheme_enrollment(citizen_id):
    try:
        new_enrollment = scheme_enrollments(
            citizen_id=citizen_id,
            scheme_id=request.form['scheme_id'],
            enrollment_date=datetime.now()
        )
        db.session.add(new_enrollment)
        db.session.commit()
        flash('Scheme enrollment successful!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('citizen'))

@app.route('/add_service_request/<int:citizen_id>', methods=['POST'])
def add_service_request(citizen_id):
    try:
        print(citizen_id)
        service_id = request.form.get('service_id')
        print(service_id)
        description = request.form.get('description')
        request_type = request.form.get('type')
        
        if not service_id or not description or not request_type:
            flash('All fields are required.', 'danger')
            return redirect(url_for('citizen'))
        
        new_request = service_requests(
            citizen_id=citizen_id,
            service_id=service_id,
            request_date=datetime.now(),
            status='Pending',
            description=description,
            type=request_type
        )
        
        db.session.add(new_request)
        db.session.commit()
        flash('Service request submitted successfully!', 'success')
    except Exception as e:
        print(e)
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('citizen'))

@app.route('/add_vaccination/<int:citizen_id>', methods=['POST'])
def add_vaccination(citizen_id):
    try:
        new_vaccination = vaccinations(
            citizen_id=citizen_id,
            vaccine_type=request.form['vaccine_type'],
            date=request.form['date']
        )
        db.session.add(new_vaccination)
        db.session.commit()
        flash('Vaccination record added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('citizen'))

def send_employee_request(citizen_id, role, password):
    try:
        citizen = citizens.query.get(citizen_id)
        if citizen:
            new_request = panchayat_employee_request(
                citizen_id=citizen.citizen_id,
                role=role,
                password=citizen.password
            )
            print("jgvgahva")
            db.session.add(new_request)
            db.session.commit()
            return True
    except Exception as e:
        db.session.rollback()
        print(f"Error sending request: {e}")
        return False
    return False

# Authentication Routes
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        try:
            aadhar_no = request.form['aadhar_no']
            first_name = request.form['first_name']
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

def get_id_from_aadhar(aadhar):
    citizen = citizens.query.filter_by(aadhar_no=aadhar).first()
    if citizen:
        return citizen.citizen_id
    return None

@app.route('/login', methods=['GET', 'POST'])
def login():
    
    if request.method == 'POST':
        id = request.form['user_id']
        password = request.form['password']
        user_type = request.form['user_type']
        user = None
        session['user_type'] = user_type

        if(user_type=='Government_Moniter'):
            return redirect(url_for('stats'))
        
        if user_type == 'citizen':
            user = citizens.query.filter_by(aadhar_no=id).first()
        elif user_type == 'admin':
            user = admin.query.filter_by(id=id).first()
        elif user_type == 'panchayat_employee':
            cit_id=get_id_from_aadhar(id)
            user = panchayat_employee.query.filter_by(citizen_id=cit_id).first()
            


        print(user)
        print(user_type)
        print(check_password_hash(user.password,password))
        print(user.password)
        if (user and user_type=='panchayat_employee' ) or (user and user_type=='citizen' and (check_password_hash(user.password, password)) or (user_type == "admin" and password == user.password)):
            #session['user_id'] = user.id if hasattr(user, 'id') else user.aadhar_no
            if hasattr(user,'id'):
                session['user_id'] = user.id
            elif user_type=='citizen':
                session['user_id'] = user.aadhar_no
            if(user_type=='panchayat_employee'):
                cit_id=get_id_from_aadhar(id)
                session['user_id']=cit_id
            flash('Login successful!', 'success')
            if user_type == 'admin':
                return redirect(url_for('admin_bhai'))
            elif user_type == 'panchayat_employee':
                return redirect(url_for('panchayat_employee_dashboard'))
            else:
                session['user_id'] = user.citizen_id
                return redirect(url_for('citizen'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')


@app.route('/filetax/<int:citizen_id>', methods=['GET', 'POST'])
def file_tax(citizen_id):
    if request.method == 'POST':
        try:
            tax_amount = request.form['tax_amount']
            tax_year = request.form['tax_year']
            tax_description = request.form['tax_description']
            
            new_tax = Tax(
                citizen_id=citizen_id,
                amount=tax_amount,
                year=tax_year,
                description=tax_description
            )
            
            db.session.add(new_tax)
            db.session.commit()
            flash('Tax filed successfully!', 'success')
            return redirect(url_for('citizen'))  
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('file_tax', citizen_id=citizen_id))  
    return render_template('file_tax.html', citizen_id=citizen_id)


@app.route('/logout')
def logout():
    try:
        session.pop('user_id', None)
        session.pop('user_type', None)
        print("logout")
        
    except Exception as e:
        print(e)
    return redirect(url_for('home'))
    

@app.route('/')
def home():
    return render_template('home_2.html')

@app.route('/edit_vaccination/<int:id>', methods=['GET', 'POST'])
def edit_vaccination(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        data = db.session.query(vaccinations).get_or_404(id)
        
        if request.method == 'POST':
            try:
                data.citizen_id = int(request.form['citizen_id'])
                data.vaccine_type = request.form['vaccine_type']
                data.date = datetime.strptime(request.form['date'], '%Y-%m-%d').date()
                
                db.session.commit()
                flash('Vaccination data updated successfully!', 'success')
                return redirect(url_for('panchayat_employee_table') + '?table_name=vaccinations')
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating vaccination data: {str(e)}', 'danger')
        
        return render_template('edit_vaccination.html', 
                             data=data,
                             current_time="2025-03-01 20:03:33",
                             current_user="")
    
    except Exception as e:
        flash(f'Error accessing vaccination data: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=vaccinations')
    
@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_citizen(id):
    citizen = citizens.query.filter_by(citizen_id=id).first()
    if not citizen:
        flash('Citizen not found', 'danger')
        return redirect(url_for('citizen'))
        
    if request.method == 'POST':
        try:
            citizen.first_name = request.form['first_name']
            citizen.last_name = request.form['last_name']
            citizen.date_of_birth = request.form['dob']
            citizen.phone_number = request.form['phone']
            citizen.caste = request.form['caste']
            citizen.gender = request.form['gender']
            citizen.household_id = request.form['household_id']
            citizen.educational_qualification = request.form['educational_qualification']
            citizen.occupation = request.form['occupation']
            citizen.marital_status = request.form['marital_status']
            
            db.session.commit()
            flash('Profile updated successfully!', 'success')
            return redirect(url_for('citizen'))
        except Exception as e:
            db.session.rollback()
            flash(f'Error: {e}', 'danger')
            return redirect(url_for('edit_citizen', id=id))
            
    return render_template('edit_citizen.html', citizen_details=citizen)


@app.route('/citizen')
def citizen():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    citizen_details = get_citizen_details(session['user_id'])
    # Get available schemes and services for dropdowns
    schemes = welfare_schemes.query.all()
    services = service.query.all()
    return render_template('citizen.html', 
                         citizen_details=citizen_details,
                         schemes=schemes,
                         services=services)
from datetime import datetime, date
from decimal import Decimal

from flask import Flask, render_template, jsonify
from sqlalchemy import extract, func, case

# @app.route('/stats')
# def stats():    
#     try:
#         # Get filter parameters
#         filters = {
#             'gender_filter': request.args.get('gender_filter'),
#             'education_filter': request.args.get('education_filter'),
#             'age_filter': request.args.get('age_filter'),
#             'year_from': request.args.get('year_from'),
#             'year_to': request.args.get('year_to'),
#             'global_search': request.args.get('global_search'),
#             'group_by': request.args.get('global_group_by')
#         }
        
#         # Debug log to see what filters are being received
#         print(f"Received filters: {filters}")

#         # Base query
#         base_query = db.session.query(citizens)

#         # Apply filters
#         if filters['global_search']:
#             search_term = f"%{filters['global_search']}%"
#             base_query = base_query.filter(
#                 or_(
#                     citizens.first_name.ilike(search_term),
#                     citizens.last_name.ilike(search_term),
#                     citizens.gender.ilike(search_term),
#                     citizens.educational_qualification.ilike(search_term),
#                     citizens.occupation.ilike(search_term),
#                     citizens.caste.ilike(search_term)
#                 )
#             )

#         if filters['gender_filter']:
#             base_query = base_query.filter(citizens.gender == filters['gender_filter'])

#         if filters['education_filter']:
#             base_query = base_query.filter(citizens.educational_qualification == filters['education_filter'])
#         if filters['year_from'] and filters['year_to']:
#             base_query = base_query.filter(
#                 extract('year', citizens.date_of_birth).between(
#                     int(filters['year_from']), 
#                     int(filters['year_to'])
#                 )
#             )

#         # Calculate basic stats from filtered query
#         total_citizens = base_query.count()
        
#         # Calculate literacy rate
#         citizens_with_no_education = base_query.filter(
#             citizens.educational_qualification.ilike('%none%')
#         ).count()
#         literacy_rate = ((total_citizens - citizens_with_no_education) / total_citizens * 100) if total_citizens > 0 else 0

#         # Calculate average age
#         current_year = 2025
#         avg_age = db.session.query(
#             func.avg(current_year - extract('year', citizens.date_of_birth))
#         ).select_from(base_query.subquery()).scalar() or 0

#         # Count total households
#         total_households = base_query.distinct(citizens.household_id).count()

#         # Function to get grouped stats
#         def get_grouped_stats(query, group_column):
#             if filters['group_by'] and filters['group_by'] != 'none':
#                 group_by_col = getattr(citizens, filters['group_by'])
#                 return query.group_by(group_column, group_by_col).all()
#             return query.group_by(group_column).all()

#         # Gender Statistics
#         gender_query = base_query.with_entities(
#             case(
#                 (citizens.gender.is_(None), 'Not Specified'),
#                 else_=citizens.gender
#             ).label('gender'),
#             func.count(citizens.citizen_id).label('count')
#         )
#         gender_stats = get_grouped_stats(gender_query, 'gender')

#         # Age Distribution
#         age_query = base_query.with_entities(
#             case(
#                 (current_year - extract('year', citizens.date_of_birth) <= 14, '0-14'),
#                 (current_year - extract('year', citizens.date_of_birth) <= 24, '15-24'),
#                 (current_year - extract('year', citizens.date_of_birth) <= 54, '25-54'),
#                 (current_year - extract('year', citizens.date_of_birth) <= 64, '55-64'),
#                 else_='65+'
#             ).label('age_group'),
#             func.count(citizens.citizen_id).label('count')
#         )
#         age_stats = get_grouped_stats(age_query, 'age_group')

#         # Education Distribution
#         education_query = base_query.with_entities(
#             case(
#                 (citizens.educational_qualification.is_(None), 'Not Specified'),
#                 else_=citizens.educational_qualification
#             ).label('education'),
#             func.count(citizens.citizen_id).label('count')
#         )
#         education_stats = get_grouped_stats(education_query, 'education')

#         # Birth Rate Trends
#         birth_rate_query = base_query.with_entities(
#             extract('year', citizens.date_of_birth).label('year'),
#             func.count(citizens.citizen_id).label('birth_count')
#         )
#         birth_rate_stats = get_grouped_stats(birth_rate_query, 'year')
#         print(birth_rate_stats)
#         # Get unique values for filter dropdowns
#         filter_options = {
#             'gender': db.session.query(citizens.gender).distinct().all(),
#             'education': db.session.query(citizens.educational_qualification).distinct().all(),
#             'caste': db.session.query(citizens.caste).distinct().all(),
#             'occupation': db.session.query(citizens.occupation).distinct().all(),
#             'birth_years': db.session.query(
#                 extract('year', citizens.date_of_birth)
#             ).distinct().order_by(
#                 extract('year', citizens.date_of_birth)
#             ).all()
#         }

#         # Available columns for grouping
#         available_columns = [
#             ('none', 'No Grouping'),
#             ('gender', 'Gender'),
#             ('educational_qualification', 'Education'),
#             ('caste', 'Caste'),
#             ('occupation', 'Occupation')
#         ]

#         return render_template(
#             'stats.html',
#             current_datetime="2025-03-02 11:36:54",
#             current_user='',
#             total_population=total_citizens,
#             literacy_rate=round(literacy_rate, 2),
#             avg_age=round(avg_age, 1),
#             total_households=total_households,
#             education_stats=education_stats,
#             gender_stats=gender_stats,
#             age_stats=age_stats,
#             birth_rate_stats=birth_rate_stats,
#             available_columns=available_columns,
#             filter_options=filter_options,
#             selected_filters=filters,  # Pass the filters to the template
#             selected_group_by=filters['group_by']
#         )

#     except Exception as e:
#         print(f"Error in stats route: {str(e)}")
#         return f"An error occurred: {str(e)}", 500
    
@app.route('/stats')
def stats():    
    try:
        # Get filter parameters
        filters = {
            'gender_filter': request.args.get('gender_filter'),
            'education_filter': request.args.get('education_filter'),
            'age_filter': request.args.get('age_filter'),
            'year_from': request.args.get('year_from'),
            'year_to': request.args.get('year_to'),
            'global_search': request.args.get('global_search'),
            'group_by': request.args.get('global_group_by')
        }
        
        # Debug log to see what filters are being received
        print(f"Received filters: {filters}")

        # Base query
        base_query = db.session.query(citizens)

        # Apply filters
        if filters['global_search']:
            search_term = f"%{filters['global_search']}%"
            base_query = base_query.filter(
                or_(
                    citizens.first_name.ilike(search_term),
                    citizens.last_name.ilike(search_term),
                    citizens.gender.ilike(search_term),
                    citizens.educational_qualification.ilike(search_term),
                    citizens.occupation.ilike(search_term),
                    citizens.caste.ilike(search_term)
                )
            )

        if filters['gender_filter']:
            base_query = base_query.filter(citizens.gender == filters['gender_filter'])

        if filters['education_filter']:
            base_query = base_query.filter(citizens.educational_qualification == filters['education_filter'])
            
        if filters['age_filter']:
            current_year = 2025
            age_ranges = {
                '0-14': (0, 14),
                '15-24': (15, 24),
                '25-54': (25, 54),
                '55-64': (55, 64),
                '65+': (65, 200)  # Upper bound for seniors
            }
            if filters['age_filter'] in age_ranges:
                min_age, max_age = age_ranges[filters['age_filter']]
                # Calculate birth years for the age range
                max_birth_year = current_year - min_age
                min_birth_year = current_year - max_age
                base_query = base_query.filter(
                    extract('year', citizens.date_of_birth).between(min_birth_year, max_birth_year)
                )
                
        if filters['year_from'] and filters['year_to']:
            base_query = base_query.filter(
                extract('year', citizens.date_of_birth).between(
                    int(filters['year_from']), 
                    int(filters['year_to'])
                )
            )

        # Calculate basic stats from filtered query
        total_citizens = base_query.count()
        
        # Calculate literacy rate
        citizens_with_no_education = base_query.filter(
            citizens.educational_qualification.ilike('%none%')
        ).count()
        literacy_rate = ((total_citizens - citizens_with_no_education) / total_citizens * 100) if total_citizens > 0 else 0

        # Calculate average age
        current_year = 2025
        avg_age_query = db.session.query(
            func.avg(current_year - extract('year', citizens.date_of_birth))
        )
        filtered_subquery = base_query.with_entities(citizens.citizen_id).subquery()
        avg_age = avg_age_query.filter(citizens.citizen_id.in_(filtered_subquery)).scalar() or 0

        # Count total households
        total_households = base_query.distinct(citizens.household_id).count()

        # Gender Statistics with grouping
        selected_group_by = filters['group_by']
        
        # Function to create properly grouped statistics
        def get_grouped_stats(select_columns, group_columns, label_map=None):
            # Start with base entities we're selecting
            query = base_query.with_entities(*select_columns)
            
            # Add group by columns
            if group_columns:
                query = query.group_by(*group_columns)
            
            # Execute the query
            results = query.all()
            
            # Convert to dictionaries with proper labels
            formatted_results = []
            for row in results:
                item = {}
                for i, col in enumerate(row._fields):
                    # Map to a friendly label if provided
                    friendly_key = label_map.get(col, col) if label_map else col
                    item[friendly_key] = row[i]
                formatted_results.append(item)
            
            return formatted_results

        # Gender statistics
        if selected_group_by and selected_group_by != 'none':
            group_by_col = getattr(citizens, selected_group_by)
            gender_stats = get_grouped_stats(
                [citizens.gender.label('gender'), 
                 group_by_col.label('group_value'),
                 func.count(citizens.citizen_id).label('count')],
                [citizens.gender, group_by_col],
                {'gender': 'gender', 'group_value': 'group_value', 'count': 'count'}
            )
        else:
            gender_stats = get_grouped_stats(
                [citizens.gender.label('gender'), 
                 func.count(citizens.citizen_id).label('count')],
                [citizens.gender],
                {'gender': 'gender', 'count': 'count'}
            )

        # Age Distribution
        current_year = 2025
        age_case = case(
            (current_year - extract('year', citizens.date_of_birth) <= 14, '0-14'),
            (current_year - extract('year', citizens.date_of_birth) <= 24, '15-24'),
            (current_year - extract('year', citizens.date_of_birth) <= 54, '25-54'),
            (current_year - extract('year', citizens.date_of_birth) <= 64, '55-64'),
            else_='65+'
        ).label('age_group')
        
        if selected_group_by and selected_group_by != 'none':
            group_by_col = getattr(citizens, selected_group_by)
            age_stats = get_grouped_stats(
                [age_case, 
                 group_by_col.label('group_value'),
                 func.count(citizens.citizen_id).label('count')],
                [age_case, group_by_col],
                {'age_group': 'age_group', 'group_value': 'group_value', 'count': 'count'}
            )
        else:
            age_stats = get_grouped_stats(
                [age_case, 
                 func.count(citizens.citizen_id).label('count')],
                [age_case],
                {'age_group': 'age_group', 'count': 'count'}
            )

        # Education Distribution
        if selected_group_by and selected_group_by != 'none':
            group_by_col = getattr(citizens, selected_group_by)
            education_stats = get_grouped_stats(
                [citizens.educational_qualification.label('education'), 
                 group_by_col.label('group_value'),
                 func.count(citizens.citizen_id).label('count')],
                [citizens.educational_qualification, group_by_col],
                {'education': 'education', 'group_value': 'group_value', 'count': 'count'}
            )
        else:
            education_stats = get_grouped_stats(
                [citizens.educational_qualification.label('education'), 
                 func.count(citizens.citizen_id).label('count')],
                [citizens.educational_qualification],
                {'education': 'education', 'count': 'count'}
            )

        # Birth Rate Trends
        year_extract = extract('year', citizens.date_of_birth).label('year')
        if selected_group_by and selected_group_by != 'none':
            group_by_col = getattr(citizens, selected_group_by)
            birth_rate_stats = get_grouped_stats(
                [year_extract, 
                 group_by_col.label('group_value'),
                 func.count(citizens.citizen_id).label('birth_count')],
                [year_extract, group_by_col],
                {'year': 'year', 'group_value': 'group_value', 'birth_count': 'birth_count'}
            )
        else:
            birth_rate_stats = get_grouped_stats(
                [year_extract, 
                 func.count(citizens.citizen_id).label('birth_count')],
                [year_extract],
                {'year': 'year', 'birth_count': 'birth_count'}
            )
        
        # Get unique values for filter dropdowns
        filter_options = {
            'gender': db.session.query(citizens.gender).distinct().all(),
            'education': db.session.query(citizens.educational_qualification).distinct().all(),
            'caste': db.session.query(citizens.caste).distinct().all(),
            'occupation': db.session.query(citizens.occupation).distinct().all(),
            'birth_years': db.session.query(
                extract('year', citizens.date_of_birth)
            ).distinct().order_by(
                extract('year', citizens.date_of_birth)
            ).all()
        }

        # Available columns for grouping
        available_columns = [
            ('none', 'No Grouping'),
            ('gender', 'Gender'),
            ('educational_qualification', 'Education'),
            ('caste', 'Caste'),
            ('occupation', 'Occupation')
        ]

        return render_template(
            'stats.html',
            current_datetime="2025-03-03 08:01:05",
            current_user='sesiii',
            total_population=total_citizens,
            literacy_rate=round(literacy_rate, 2),
            avg_age=round(avg_age, 1),
            total_households=total_households,
            education_stats=education_stats,
            gender_stats=gender_stats,
            age_stats=age_stats,
            birth_rate_stats=birth_rate_stats,
            available_columns=available_columns,
            filter_options=filter_options,
            selected_filters=filters,
            selected_group_by=filters['group_by']
        )

    except Exception as e:
        print(f"Error in stats route: {str(e)}")
        traceback.print_exc()  # This will print the full stack trace
        return f"An error occurred: {str(e)}", 500

    
@app.route('/admin')
def admin_bhai():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    tables = get_all_tables()
    return render_template('admin.html', tables=tables, active_table=None)

@app.route('/get_table_data/<table_name>')
def get_table_data_route(table_name):
    table_data = get_table_data(table_name)
    if table_data:
        return jsonify(table_data)
    return jsonify({"error": f"Table {table_name} not found or error retrieving data"}), 404

@app.route('/admin/<table_name>')
def admin_table(table_name):
    print("Enter")
    tables = get_all_tables()
    table_data = get_table_data(table_name)
    for name in tables:
        print("name:",name)
        print(get_table_data(name))
    print(table_data)
    print(table_name)
    return render_template('admin.html', tables=tables, active_table=table_data)


@app.route('/fetch_data')
def fetch_data():
    table_name = request.args.get('type')  # Get the requested table name
    if not table_name:
        flash('No table specified', 'danger')
        return redirect(url_for('panchayat_employee_dashboard'))

    tables = get_all_tables()
    if table_name not in tables:
        flash('Invalid table name', 'danger')
        return redirect(url_for('panchayat_employee_dashboard'))

    table_data = get_table_data(table_name)  # Fetch table data

    return render_template(
        'table_display.html',
        table_name=table_name,
        table_data=table_data
    )


@app.route('/panchayat_employee_table')
def panchayat_employee_table():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    citizen_details = get_citizen_details(session['user_id'])
    if not citizen_details:
        flash('Citizen details not found', 'danger')
        return redirect(url_for('login'))

    available_tables = [
        'environmental_data',
        'census',
        'welfare_schemes',
        'service',
        'expenditure',
        'vaccinations',
        'tax',
        'income',
        'citizens',
        'service_requests'
    ]

    table_name = request.args.get('table_name')
    table_data = None
    
    if table_name and table_name in available_tables:
        table_data = get_table_data(table_name)

    current_datetime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')

    return render_template(
        'panchayat_employee.html',
        citizen_details=citizen_details,
        tables=available_tables,
        active_table=table_data,
        current_datetime=current_datetime,
        current_user='',
        show_view_tab=True  # Add this flag to maintain tab state
    )
def get_income_details(id):
        try:
            incomes = income.query.filter_by(id=id).all()
            income_list = []
            for inc in incomes:
                income_list.append({
                    'income_id': inc.income_id,
                    'amount': inc.amount,
                    'income_date': inc.income_date,
                    'source': inc.source,
                    'financial_year': inc.financial_year,
                    'citizen_id': inc.citizen_id
                })
            return income_list
        except Exception as e:
            print(f"Error fetching income details: {e}")
            return []

@app.route('/get_income/<int:id>', methods=['GET'])
def get_income(id):
        income_details = get_income_details(id)
        if income_details:
            return jsonify(income_details)
        else:
            return jsonify({'error': 'No income records found for the given citizen ID'}), 404


def get_citizens():
                try:
                    citizens_list = citizens.query.all()
                    result = []
                    for citizen in citizens_list:
                        result.append({
                            'citizen_id': citizen.citizen_id,
                            'aadhar_no': citizen.aadhar_no,
                            'first_name': citizen.first_name,
                            'last_name': citizen.last_name,
                            'date_of_birth': citizen.date_of_birth,
                            'phone_number': citizen.phone_number,
                            'caste': citizen.caste,
                            'gender': citizen.gender,
                            'household_id': citizen.household_id,
                            'educational_qualification': citizen.educational_qualification,
                            'occupation': citizen.occupation,
                            'marital_status': citizen.marital_status
                        })
                    return result
                except Exception as e:
                    print(f"Error fetching citizens details: {e}")
                    return []

@app.route('/get_citizens', methods=['GET'])
def get_citizens_route():
                citizens_details = get_citizens()
                print(citizens_details)
                if citizens_details:
                    return jsonify(citizens_details)
                else:
                    return jsonify({'error': 'No citizen records found'}), 404
def get_tax_details(id):
        try:
            taxes = Tax.query.filter_by(id=id).all()
            tax_list = []
            for tax in taxes:
                tax_list.append({
                    'id': tax.id,
                    'citizen_id': tax.citizen_id,
                    'amount': tax.amount,
                    'year': tax.year,
                    'description': tax.description
                })
            return tax_list
        except Exception as e:
            print(f"Error fetching tax details: {e}")
            return []

@app.route('/get_tax/<int:id>', methods=['GET'])
def get_tax(id):
        tax_details = get_tax_details(id)
        if tax_details:
            return jsonify(tax_details)
        else:
            return jsonify({'error': 'No tax records found for the given citizen ID'}), 404
@app.route('/get_environmental_data/<int:id>')


def get_environmental_data(id):
    try:
        data = environmental_data.query.get_or_404(id)
        return jsonify({
            'issue_type': data.issue_type,
            'description': data.description,
            'rainfall': data.rainfall,
            'groundwater_level': data.groundwater_level,
            'pollution_data': data.pollution_data
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400


from datetime import datetime
from sqlalchemy import desc



@app.route('/add_environmental_data', methods=['POST'])
def add_environmental_data():
    try:
        new_data = environmental_data(
            issue_type=request.form['issue_type'],
            description=request.form['description'],
            report_date=datetime.now(),
            rainfall=float(request.form['rainfall']) if request.form['rainfall'] else None,
            groundwater_level=float(request.form['groundwater_level']) if request.form['groundwater_level'] else None,
            pollution_data=request.form['pollution_data']
        )
        db.session.add(new_data)
        db.session.commit()
        flash('Environmental data added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

from datetime import datetime

@app.route('/edit_welfare_scheme/<int:scheme_id>', methods=['GET', 'POST'])
def edit_welfare_scheme(scheme_id):
    try:
        scheme = welfare_schemes.query.get_or_404(scheme_id)
        
        if request.method == 'POST':
            scheme.name = request.form['name']
            scheme.description = request.form['description']
            scheme.eligibility = request.form['eligibility']
            scheme.benefits = request.form['benefits']
            scheme.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
            scheme.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d') if request.form['end_date'] else None
            
            db.session.commit()
            flash('Welfare scheme updated successfully!', 'success')
            return redirect(url_for('panchayat_employee_table') + '?table_name=welfare_schemes')
        
        return render_template(
            'edit_welfare_scheme.html',
            scheme=scheme,
            current_datetime='2025-03-01 19:21:23',
            current_user=''
        )
    
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating welfare scheme: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=welfare_schemes')



from datetime import datetime
from flask import render_template, request, redirect, url_for, flash

@app.route('/edit_environmental_data/<int:data_id>', methods=['GET', 'POST'])
def edit_environmental_data(data_id):
    print(f"Accessing edit_environmental_data with ID: {data_id}")  
    if 'user_id' not in session:
        print("No user_id in session")  
        return redirect(url_for('login'))

    try:
        print("Querying environmental data")  
        data = db.session.query(environmental_data).get_or_404(data_id)
        current_datetime = "2025-03-01 19:46:15"
        
        if request.method == 'POST':
            print("Processing POST request")  
            try:
                data.issue_type = request.form['issue_type']
                data.description = request.form['description']
                data.rainfall = float(request.form['rainfall']) if request.form['rainfall'] else None
                data.groundwater_level = float(request.form['groundwater_level']) if request.form['groundwater_level'] else None
                data.pollution_data = request.form['pollution_data']
                
                db.session.commit()
                flash('Environmental data updated successfully!', 'success')
                return redirect(url_for('panchayat_employee_table') + '?table_name=environmental_data')
            except Exception as e:
                print(f"Error in POST processing: {str(e)}")  
                db.session.rollback()
                flash(f'Error updating data: {str(e)}', 'danger')
        
        print("Rendering template")  
        citizen_details = get_citizen_details(session['user_id'])
        return render_template('edit_environmental_data.html', 
                             data=data, 
                             current_time=current_datetime,
                             current_user='',
                             citizen_details=citizen_details)
    
    except Exception as e:
        print(f"Error in main try block: {str(e)}")  
        flash(f'Error accessing data: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=environmental_data')
    

    
    
@app.route('/add_census', methods=['POST'])
def add_census():
    try:
        new_census = census(
            year=int(request.form['year']),
            population=int(request.form['population']),
            demographics=request.form['demographics'],
            description=request.form['description']
        )
        db.session.add(new_census)
        db.session.commit()
        flash('Census data added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

@app.route('/edit_census/<int:id>', methods=['GET', 'POST'])
def edit_census(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        data = db.session.query(census).get_or_404(id)
        current_datetime = "2025-03-01 19:56:25"
        
        if request.method == 'POST':
            try:
                # Update census data based on your actual schema
                data.year = request.form['year']
                data.population = request.form['population']
                data.demographics = request.form['demographics']
                data.description = request.form['description']
                
                db.session.commit()
                flash('Census data updated successfully!', 'success')
                return redirect(url_for('panchayat_employee_table') + '?table_name=census')
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating census data: {str(e)}', 'danger')
        
        return render_template('edit_census.html', 
                             data=data, 
                             current_time=current_datetime,
                             current_user='')
    
    except Exception as e:
        flash(f'Error accessing census data: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=census')
    

    
@app.route('/add_service', methods=['POST'])
def add_service():
    try:
        new_service = service(
            type=request.form['type'],
            status=request.form['status'],
            request_date=datetime.now()
        )
        db.session.add(new_service)
        db.session.commit()
        flash('Service added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

@app.route('/edit_service/<int:id>', methods=['GET', 'POST'])
def edit_service(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        data = db.session.query(service).get_or_404(id)
        
        if request.method == 'POST':
            try:
                data.type = request.form['type']
                data.status = request.form['status']
                data.request_date = datetime.strptime(request.form['request_date'], '%Y-%m-%d').date() if request.form['request_date'] else None
                
                db.session.commit()
                flash('Service data updated successfully!', 'success')
                return redirect(url_for('panchayat_employee_table') + '?table_name=service')
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating service data: {str(e)}', 'danger')
        
        return render_template('edit_service.html', 
                             data=data,
                             current_time="2025-03-01 20:03:33",
                             current_user="")
    
    except Exception as e:
        flash(f'Error accessing service data: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=service')
    

@app.route('/update_welfare_scheme/<int:scheme_id>', methods=['POST'])
def update_welfare_scheme(scheme_id):
    try:
        scheme = welfare_schemes.query.get_or_404(scheme_id)
        scheme.name = request.form['name']
        scheme.description = request.form['description']
        scheme.eligibility = request.form['eligibility']
        scheme.benefits = request.form['benefits']
        scheme.start_date = datetime.strptime(request.form['start_date'], '%Y-%m-%d')
        scheme.end_date = datetime.strptime(request.form['end_date'], '%Y-%m-%d')
        
        db.session.commit()
        flash('Welfare scheme updated successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error updating welfare scheme: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

@app.route('/get_welfare_scheme/<int:scheme_id>')
def get_welfare_scheme(scheme_id):
    scheme = welfare_schemes.query.get_or_404(scheme_id)
    return jsonify({
        'name': scheme.name,
        'description': scheme.description,
        'eligibility': scheme.eligibility,
        'benefits': scheme.benefits,
        'start_date': scheme.start_date.strftime('%Y-%m-%d'),
        'end_date': scheme.end_date.strftime('%Y-%m-%d') if scheme.end_date else ''
    })

@app.route('/add_welfare_scheme', methods=['POST'])
def add_welfare_scheme():
    try:
        new_scheme = welfare_schemes(
            name=request.form['name'],
            description=request.form['description'],
            eligibility=request.form['eligibility'],
            benefits=request.form['benefits'],
            start_date=datetime.strptime(request.form['start_date'], '%Y-%m-%d'),
            end_date=datetime.strptime(request.form['end_date'], '%Y-%m-%d') if request.form['end_date'] else None
        )
        db.session.add(new_scheme)
        db.session.commit()
        flash('Welfare scheme added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error adding welfare scheme: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

@app.route('/add_expenditure', methods=['POST'])
def add_expenditure():
    try:
        new_expenditure = expenditure(
            amount=float(request.form['amount']),
            expenditure_date=datetime.now(),
            purpose=request.form['purpose'],
            category=request.form['category'],
            payment_mode=request.form['payment_mode'],
            financial_year=request.form['financial_year']
        )
        db.session.add(new_expenditure)
        db.session.commit()
        flash('Expenditure added successfully!', 'success')
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {str(e)}', 'danger')
    return redirect(url_for('panchayat_employee_dashboard'))

@app.route('/edit_expenditure/<int:id>', methods=['GET', 'POST'])
def edit_expenditure(id):
    if 'user_id' not in session:
        return redirect(url_for('login'))

    try:
        data = db.session.query(expenditure).get_or_404(id)
        
        if request.method == 'POST':
            try:
                data.amount = Decimal(request.form['amount'])
                data.expenditure_date = datetime.strptime(request.form['expenditure_date'], '%Y-%m-%d').date()
                data.purpose = request.form['purpose']
                data.category = request.form['category']
                data.payment_mode = request.form['payment_mode']
                data.financial_year = request.form['financial_year']
                
                db.session.commit()
                flash('Expenditure data updated successfully!', 'success')
                return redirect(url_for('panchayat_employee_table') + '?table_name=expenditure')
            except Exception as e:
                db.session.rollback()
                flash(f'Error updating expenditure data: {str(e)}', 'danger')
        
        return render_template('edit_expenditure.html', 
                             data=data,
                             current_time="2025-03-01 20:03:33",
                             current_user="")
    
    except Exception as e:
        flash(f'Error accessing expenditure data: {str(e)}', 'danger')
        return redirect(url_for('panchayat_employee_table') + '?table_name=expenditure')

# Update the panchayat_employee_dashboard route to include necessary data
@app.route('/panchayat_employee')
def panchayat_employee_dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    citizen_details = get_citizen_details(session['user_id'])
    if not citizen_details:
        flash('Citizen details not found', 'danger')
        return redirect(url_for('login'))

    # List of tables that can be viewed/edited by panchayat employee
    available_tables = [
        'environmental_data',
        'census',
        'welfare_schemes',
        'service',
        'expenditure',
        'vaccinations',
        'assets',
        'land_records',
        'tax',
        'income',
        'citizens',
        'service_requests'
    ]
    print("hi")
    print(available_tables)

    current_datetime = datetime.utcnow().strftime('%Y-%m-%d %H:%M:%S')
    return render_template(
        'panchayat_employee.html',
        citizen_details=citizen_details,
        tables=available_tables,
        active_table=None,
        current_datetime=current_datetime,
        current_user=''
    )

@app.route('/approve_tax', methods=['POST'])
def approve_tax():
    try:
        tax_id = request.args.get('id')
        tax_entry = Tax.query.get(tax_id)
        if tax_entry:
            db.session.delete(tax_entry)
            db.session.commit()
            flash('Tax entry approved and deleted successfully!', 'success')
        else:
            flash('Tax entry not found!', 'danger')
        return redirect(url_for('admin_table', table_name='tax'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('admin_bhai', table_name='tax'))
    

@app.route('/approve_citizen/<int:id>', methods=['POST'])
def approve_citizen(id):
    try:
        temp_user = db.session.get(citizen_temp, id)
        if temp_user:
            new_citizen = citizens(
                citizen_id=temp_user.id,
                aadhar_no=temp_user.aadhar_no,
                first_name=temp_user.first_name,
                last_name=temp_user.last_name,
                date_of_birth=temp_user.dob,
                phone_number=temp_user.phone,  
                caste=temp_user.caste,
                gender=temp_user.gender,
                household_id=temp_user.household_id,
                educational_qualification=temp_user.educational_qualification,
                occupation=temp_user.occupation,
                marital_status=temp_user.marital_status,
                password=temp_user.password
            )

            existing_household = db.session.get(households, temp_user.household_id)
            if not existing_household:
                new_household = households(
                    household_id=temp_user.household_id,
                    address="None"
                )
                db.session.add(new_household)
                db.session.commit()
            # print(temp_user.password)
            db.session.add(new_citizen)
            # print("123")
            db.session.delete(temp_user)
            # print("456")

            db.session.commit()
            print("hi")
            flash('Citizen approved and data migrated successfully!', 'success')
        return redirect(url_for('admin_table', table_name='citizen_temp'))
    except Exception as e:
        db.session.rollback()
        print(e)
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('admin_table', table_name='citizen_temp'))



@app.route('/approve_panchayat_employee/<int:id>', methods=['POST'])
def approve_panchayat_employee(id):
    print(id)
    try:
        temp_employee = db.session.get(panchayat_employee_request, id)
        if temp_employee:
            new_employee = panchayat_employee(
                citizen_id=temp_employee.citizen_id,
                password=temp_employee.password,
                role=temp_employee.role
            )
            
            # Add the new permanent panchayat employee record
            db.session.add(new_employee)
            
            # Delete the temporary record
            db.session.delete(temp_employee)
            
            # Commit the transaction
            db.session.commit()
            
            flash('Panchayat employee approved and data migrated successfully!', 'success')
        else:
            flash('Temporary panchayat employee record not found!', 'danger')
            
        return redirect(url_for('admin_table', table_name='panchayat_employee_temp'))
    except Exception as e:
        db.session.rollback()
        print(e)
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('admin_table', table_name='panchayat_employee_temp'))
    
@app.route('/decline_panchayat_employee/<int:id>', methods=['POST'])
def decline_panchayat_employee(id):
    try:
        temp_employee = db.session.get(panchayat_employee_request, id)
        if temp_employee:
            db.session.delete(temp_employee)
            db.session.commit()
            flash('Panchayat employee request declined and data deleted successfully!', 'success')
        else:
            flash('Temporary panchayat employee record not found!', 'danger')
        return redirect(url_for('admin_table', table_name='panchayat_employee_temp'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('admin_table', table_name='panchayat_employee_temp'))
    


@app.route('/decline_citizen/<int:id>', methods=['POST'])
def decline_citizen(id):
    try:
        temp_user = db.session.get(citizen_temp, id)
        if temp_user:
            db.session.delete(temp_user)
            db.session.commit()
            flash('Citizen request declined and data deleted successfully!', 'success')
        return redirect(url_for('admin_table', table_name='citizen_temp'))
    except Exception as e:
        db.session.rollback()
        flash(f'Error: {e}', 'danger')
        return redirect(url_for('admin_table', table_name='citizen_temp'))
    
@app.route('/request_employee/<int:id>', methods=['GET', 'POST'])
def request_employee(id):
    if request.method == 'POST':
        role = request.form['role']
        password = request.form['password']
        if send_employee_request(id, role, password):
            flash('Request sent successfully!', 'success')
        else:
            flash('Failed to send request. Check your password.', 'danger')
        return redirect(url_for('citizen'))
    return render_template('request_employee.html', user_id=id)

@app.route('/submit_role_request', methods=['POST'])
def submit_role_request():
    """Handle the form submission and insert data into the database"""
    if request.method == 'POST':
        citizen_id = request.form.get('citizen_id')
        password = request.form.get('password')
        role = request.form.get('role')
        
        if not citizen_id or not password or not role:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': 'All fields are required'})
            flash('All fields are required', 'error')
            return redirect(url_for('index'))
        
        hashed_password = generate_password_hash(password)
        
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            
            cursor.execute(
                'INSERT INTO panchayat_employee_request (citizen_id, password, role) VALUES (?, ?, ?)',
                (citizen_id, hashed_password, role)
            )
            
            conn.commit()
            conn.close()
            
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': True, 'message': 'Your role request has been submitted successfully'})
            
            flash('Your role request has been submitted successfully', 'success')
            return redirect(url_for('index'))
            
        except Exception as e:
            if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
                return jsonify({'success': False, 'message': f'Database error: {str(e)}'})
            
            flash(f'Database error: {str(e)}', 'error')
            return redirect(url_for('index'))
        
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=False)