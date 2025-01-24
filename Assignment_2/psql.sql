sudo -u postgres psql -- create a new database
CREATE DATABASE final; -- create the database 


\c final -- connect to the database

-- create the tables

CREATE TABLE households (
    household_id SERIAL PRIMARY KEY,
    address VARCHAR(200) NOT NULL,
    number_of_members INTEGER NOT NULL,
    income INTEGER
);

CREATE TABLE citizens (
    citizen_id SERIAL PRIMARY KEY,
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

CREATE TABLE land_records (
    land_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    area_acres DECIMAL NOT NULL,
    crop_type VARCHAR(200)
);

CREATE TABLE panchayat_employees (
    employee_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    role VARCHAR(200)
);

CREATE TABLE assets (
    asset_id SERIAL PRIMARY KEY,
    type VARCHAR(200) NOT NULL,
    household_id INTEGER,
    FOREIGN KEY (household_id) REFERENCES households(household_id),
    value DECIMAL NOT NULL,
    location VARCHAR(200),
    name VARCHAR(200),
    installation_date DATE
);

CREATE TABLE welfare_schemes (
    scheme_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    eligibility VARCHAR(200),
    benefits VARCHAR(200),
    start_date DATE,
    end_date DATE
);

CREATE TABLE scheme_enrollments (
    enrollment_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    scheme_id INTEGER,
    FOREIGN KEY (scheme_id) REFERENCES welfare_schemes(scheme_id),
    enrollment_date DATE NOT NULL
);

CREATE TABLE vaccinations (
    vaccination_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    vaccine_type VARCHAR(200) NOT NULL,
    date DATE NOT NULL
);

CREATE TABLE census_data (
    census_id SERIAL PRIMARY KEY,
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

CREATE TABLE tax (
    tax_id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    payment_date DATE NOT NULL,
    status VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200),
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

CREATE TABLE income (
    income_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    amount DECIMAL NOT NULL,
    income_date DATE NOT NULL,
    source VARCHAR(200),
    financial_year VARCHAR(200)
);

CREATE TABLE expenditure (
    expenditure_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    amount DECIMAL NOT NULL,
    expenditure_date DATE NOT NULL,
    purpose VARCHAR(200),
    category VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200)
);

CREATE TABLE service (
    service_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    type VARCHAR(200) NOT NULL,
    status VARCHAR(200),
    request_date DATE
);

CREATE TABLE service_requests (
    request_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    service_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service(service_id),
    request_date DATE NOT NULL,
    status VARCHAR(200)
);

-- insert data into the tables(populating the tables)
