create table households(
    household_id INTEGER PRIMARY KEY,
    address VARCHAR(200) NOT NULL,
    number_of_members INTEGER NOT NULL,
    income INTEGER
);
create table citizens(
    citizen_id INTEGER PRIMARY KEY,
    aadhar_no VARCHAR(200) UNIQUE NOT NULL,
    first_name VARCHAR(200) NOT NULL,
    last_name VARCHAR(200) NOT NULL,
    date_of_birth DATE NOT NULL,
    phone_number VARCHAR(200),
    age INTEGER,
    caste VARCHAR(200),
    gender VARCHAR(200) NOT NULL,
    household_id INTEGER NOT NULL,
    FOREIGN KEY (household_id) REFERENCES households(household_id),
    educational_qualification VARCHAR(200),
    occupation VARCHAR(200),
    marital_status VARCHAR(200)
);


create table land_records(
    land_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    area_acres DECIMAL NOT NULL,
    crop_type VARCHAR(200)
);

ALTER TABLE panchayat_employees
ADD COLUMN household_id INTEGER;

create table panchayat_employees(
    employee_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    role VARCHAR(200)
);

UPDATE panchayat_employees pe
SET household_id = h.household_id
FROM households h
WHERE pe.employee_id = h.household_id;


UPDATE panchayat_employees pe
SET household_id = h.household_id
FROM households h
WHERE pe.employee_id = h.household_id;

create table assets(
    asset_id INTEGER PRIMARY KEY,
    type VARCHAR(200) NOT NULL,
    household_id INTEGER,
    FOREIGN KEY (household_id) REFERENCES households(household_id),
    value DECIMAL NOT NULL,
    location VARCHAR(200),
    name VARCHAR(200),
    installation_date DATE
);

create table welfare_schemes(
    scheme_id INTEGER PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    eligibility VARCHAR(200),
    benefits VARCHAR(200),
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
    vaccine_type VARCHAR(200) NOT NULL,
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
    demographics VARCHAR(200),
    description VARCHAR(200),
    event_type VARCHAR(200),
    event_date DATE
);

create table tax(
    tax_id INTEGER PRIMARY KEY,
    amount DECIMAL NOT NULL,
    payment_date DATE NOT NULL,
    status VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200),
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

create table income(
    income_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    amount DECIMAL NOT NULL,
    income_date DATE NOT NULL,
    source VARCHAR(200),
    financial_year VARCHAR(200)
);

create table expenditure(
    expenditure_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    amount DECIMAL NOT NULL,
    expenditure_date DATE NOT NULL,
    purpose VARCHAR(200),
    category VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200)
);

create table service(
    service_id INTEGER PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    type VARCHAR(200) NOT NULL,
    status VARCHAR(200),
    request_date DATE
);

create table service_requests(
    request_id INTEGER PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    service_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service(service_id),
    request_date DATE NOT NULL,
    status VARCHAR(200)
);

