create table citizens(
    citizen_id INTEGER PRIMARY KEY,
    aadhar_no TEXT(50) UNIQUE NOT NULL,
    first_name TEXT(50) NOT NULL,
    last_name TEXT(50) NOT NULL,
    date_of_birth DATE NOT NULL,
    phone_number TEXT(50),
    age INTEGER,
    caste TEXT(50),
    gender TEXT(50) NOT NULL,
    household_id INTEGER NOT NULL,
    FOREIGN KEY (household_id) REFERENCES households(household_id),
    educational_qualification TEXT(50),
    occupation TEXT(50),
    marital_status TEXT(50)
);

create table households(
    household_id INTEGER PRIMARY KEY,
    address TEXT(50) NOT NULL,
    number_of_members INTEGER NOT NULL,
    income INTEGER
);

create table land_records(
    land_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    area_acres DECIMAL NOT NULL,
    crop_type TEXT(50)
);

create table panchayat_employees(
    employee_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    role TEXT(50)
);

create table assets(
    asset_id INTEGER PRIMARY KEY,
    type TEXT(50) NOT NULL,
    value DECIMAL NOT NULL,
    location TEXT(50),
    name TEXT(50),
    installation_date DATE
);

create table welfare_schemes(
    scheme_id INTEGER PRIMARY KEY,
    name TEXT(50) NOT NULL,
    description TEXT(50),
    eligibility TEXT(50),
    benefits TEXT(50),
    start_date DATE,
    end_date DATE
);

create table scheme_enrollments(
    enrollment_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    scheme_id INTEGER,
    FOREIGN KEY (scheme_id) REFERENCES welfare_schemes(scheme_id),
    enrollment_date DATE NOT NULL
);

create table vaccinations(
    vaccination_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    vaccine_type TEXT(50) NOT NULL,
    date DATE NOT NULL
);

create table census_data(
    census_id INTEGER PRIMARY KEY,
    household_id INTEGER,
    FOREIGN KEY (household_id) REFERENCES households(household_id),
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    year INTEGER NOT NULL,
    population INTEGER NOT NULL,
    demographics TEXT(50),
    description TEXT(50),
    event_type TEXT(50),
    event_date DATE
);

create table tax(
    tax_id INTEGER PRIMARY KEY,
    amount DECIMAL NOT NULL,
    payment_date DATE NOT NULL,
    status TEXT(50),
    payment_mode TEXT(50),
    financial_year TEXT(50),
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

create table income(
    income_id INTEGER PRIMARY KEY,
    amount DECIMAL NOT NULL,
    income_date DATE NOT NULL,
    source TEXT(50),
    financial_year TEXT(50)
);

create table expenditure(
    expenditure_id INTEGER PRIMARY KEY,
    amount DECIMAL NOT NULL,
    expenditure_date DATE NOT NULL,
    purpose TEXT(50),
    category TEXT(50),
    payment_mode TEXT(50),
    financial_year TEXT(50)
);

create table service(
    service_id INTEGER PRIMARY KEY,
    type TEXT(50) NOT NULL,
    status TEXT(50),
    request_date DATE
);

create table service_requests(
    request_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    service_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service(service_id),
    request_date DATE NOT NULL,
    status TEXT(50)
);


