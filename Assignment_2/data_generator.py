import random
from faker import Faker

fake = Faker()

def generate_citizens(num=10):
    citizens = []
    for _ in range(num):
        citizen = {
            "citizen_id": _ + 1,
            "aadhar_no": fake.unique.numerify("##########"),
            "first_name": fake.first_name(),
            "last_name": fake.last_name(),
            "date_of_birth": fake.date_of_birth(minimum_age=18, maximum_age=90),
            "phone_number": fake.phone_number(),
            "age": random.randint(18, 90),
            "caste": random.choice(["General", "OBC", "SC", "ST"]),
            "gender": random.choice(["Male", "Female", "Other"]),
            "household_id": random.randint(1, num // 2),
            "educational_qualification": random.choice(
                ["Primary", "Secondary", "Graduate", "Postgraduate", "None"]
            ),
            "occupation": random.choice(["Farmer", "Teacher", "Doctor", "Engineer", "Unemployed"]),
            "marital_status": random.choice(["Single", "Married", "Widowed", "Divorced"]),
        }
        citizens.append(citizen)
    return citizens

def generate_households(num=30):
    households = []
    for _ in range(num):
        household = {
            "household_id": _ + 1,
            "address": fake.address(),
            "number_of_members": random.randint(1, 10),
            "income": random.randint(10000, 500000),
        }
        households.append(household)
    return households

def generate_land_records(num=30):
    land_records = []
    for _ in range(num):
        record = {
            "land_id": _ + 1,
            "citizen_id": random.randint(1, 10),
            "area_acres": round(random.uniform(0.30, 30), 2),
            "crop_type": random.choice(["Rice", "Wheat", "Corn", "None"]),
        }
        land_records.append(record)
    return land_records

def generate_panchayat_employees(num=3):
    employees = []
    for _ in range(num):
        employee = {
            "employee_id": _ + 1,
            "citizen_id": random.randint(1, 50),
            "role": random.choice(["Clerk", "Supervisor", "Manager", "Secretary", "Peon","Doctor","Engineer","Teacher","Nurse"]),
        }
        employees.append(employee)
    return employees

def generate_assets(num=30):
    assets = []
    for _ in range(num):
        asset = {
            "asset_id": _ + 1,
            "type": random.choice(["Land", "Building", "Vehicle", "Machinery"]),
            "value": round(random.uniform(5000, 500000), 2),
            "location": fake.city(),
            "name": fake.word(),
            "installation_date": fake.date_between(start_date="-10y", end_date="today"),
        }
        assets.append(asset)
    return assets

def generate_welfare_schemes(num=3):
    schemes = []
    for _ in range(num):
        scheme = {
            "scheme_id": _ + 1,
            "name": fake.sentence(nb_words=3),
            "description": fake.text(max_nb_chars=50),
            "eligibility": "Residents with income < 200,000",
            "benefits": "Monthly stipend of $100",
            "start_date": fake.date_between(start_date="-5y", end_date="today"),
            "end_date": fake.date_between(start_date="today", end_date="+5y"),
        }
        schemes.append(scheme)
    return schemes

def generate_scheme_enrollments(num=30):
    enrollments = []
    for _ in range(num):
        enrollment = {
            "enrollment_id": _ + 1,
            "citizen_id": random.randint(1, 10),
            "scheme_id": random.randint(1, 3),
            "enrollment_date": fake.date_between(start_date="-2y", end_date="today"),
        }
        enrollments.append(enrollment)
    return enrollments

def generate_vaccinations(num=30):
    vaccinations = []
    for _ in range(num):
        vaccination = {
            "vaccination_id": _ + 1,
            "citizen_id": random.randint(1, 10),
            "vaccine_type": random.choice(["Covid-19", "Flu", "Hepatitis", "Polio"]),
            "date": fake.date_between(start_date="-2y", end_date="today"),
        }
        vaccinations.append(vaccination)
    return vaccinations

def generate_census_data(num=30):
    census = []
    for _ in range(num):
        data = {
            "census_id": _ + 1,
            "household_id": random.randint(1, 30),
            "citizen_id": random.randint(1, 10),
            "year": random.randint(2000, 2023),
            "population": random.randint(1, 10),
            "demographics": fake.text(max_nb_chars=50),
            "description": fake.text(max_nb_chars=50),
            "event_type": random.choice(["Birth", "Death", "Migration"]),
            "event_date": fake.date_between(start_date="-10y", end_date="today"),
        }
        census.append(data)
    return census

def generate_tax_data(num=10):
    taxes = []
    for _ in range(num):
        tax = {
            "tax_id": _ + 1,
            "amount": round(random.uniform(1000, 50000), 2),
            "payment_date": fake.date_between(start_date="-5y", end_date="today"),
            "status": random.choice(["Paid", "Pending", "Overdue"]),
            "payment_mode": random.choice(["Online", "Cash", "Cheque", "Bank Transfer"]),
            "financial_year": f"{random.randint(2018, 2023)}-{random.randint(2019, 2024)}",
            "citizen_id": random.randint(1, 10),
        }
        taxes.append(tax)
    return taxes

def generate_income_data(num=10):
    incomes = []
    for _ in range(num):
        income = {
            "income_id": _ + 1,
            "amount": round(random.uniform(5000, 100000), 2),
            "income_date": fake.date_between(start_date="-5y", end_date="today"),
            "source": random.choice(["Salary", "Business", "Rent", "Investment"]),
            "financial_year": f"{random.randint(2018, 2023)}-{random.randint(2019, 2024)}",
        }
        incomes.append(income)
    return incomes

def generate_expenditure_data(num=10):
    expenditures = []
    for _ in range(num):
        expenditure = {
            "expenditure_id": _ + 1,
            "amount": round(random.uniform(1000, 50000), 2),
            "expenditure_date": fake.date_between(start_date="-5y", end_date="today"),
            "purpose": fake.sentence(nb_words=3),
            "category": random.choice(["Healthcare", "Education", "Groceries", "Travel", "Utilities"]),
            "payment_mode": random.choice(["Online", "Cash", "Cheque", "Bank Transfer"]),
            "financial_year": f"{random.randint(2018, 2023)}-{random.randint(2019, 2024)}",
        }
        expenditures.append(expenditure)
    return expenditures

def generate_services(num=5):
    services = []
    for _ in range(num):
        service = {
            "service_id": _ + 1,
            "type": random.choice(["Water Connection", "Electricity Connection", "Waste Disposal", "Road Maintenance"]),
            "status": random.choice(["Active", "Pending", "Completed"]),
            "request_date": fake.date_between(start_date="-5y", end_date="today"),
        }
        services.append(service)
    return services

def generate_service_requests(num=10):
    service_requests = []
    for _ in range(num):
        request = {
            "request_id": _ + 1,
            "citizen_id": random.randint(1, 10),
            "service_id": random.randint(1, 5),
            "request_date": fake.date_between(start_date="-5y", end_date="today"),
            "status": random.choice(["Pending", "In Progress", "Resolved"]),
        }
        service_requests.append(request)
    return service_requests

# Call functions and print sample data
if __name__ == "__main__":
    print("Citizens:", generate_citizens(10))
    print("Households:", generate_households(30))
    print("Land Records:", generate_land_records(30))
    print("Panchayat Employees:", generate_panchayat_employees(3))
    print("Assets:", generate_assets(30))
    print("Welfare Schemes:", generate_welfare_schemes(22))
    print("Scheme Enrollments:", generate_scheme_enrollments(30))
    print("Vaccinations:", generate_vaccinations(30))
    print("Census Data:", generate_census_data(30))
    print("Tax Data:", generate_tax_data(10))
    print("Income Data:", generate_income_data(20))
    print("Expenditure Data:", generate_expenditure_data(40))
    print("Services:", generate_services(35))
    print("Service Requests:", generate_service_requests(25))
