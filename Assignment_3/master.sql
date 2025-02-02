drop table if EXISTS
households, citizens, land_records, panchayat_employees, assets, welfare_schemes, scheme_enrollments, vaccinations, census_data, tax, income, expenditure, service, service_requests;

create table households(
    household_id SERIAL PRIMARY KEY,
    address VARCHAR(200) NOT NULL,
    number_of_members INTEGER NOT NULL,
    income INTEGER
);

create table citizens(
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

create table land_records(
    land_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    area_acres DECIMAL NOT NULL,
    crop_type VARCHAR(200)
);

create table panchayat_employees(
    employee_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    role VARCHAR(200)
);

create table assets(
    asset_id SERIAL PRIMARY KEY,
    type VARCHAR(200) NOT NULL,
    value DECIMAL NOT NULL,
    location VARCHAR(200),
    name VARCHAR(200),
    installation_date DATE
);

create table welfare_schemes(
    scheme_id SERIAL PRIMARY KEY,
    name VARCHAR(200) NOT NULL,
    description VARCHAR(200),
    eligibility VARCHAR(200),
    benefits VARCHAR(200),
    start_date DATE,
    end_date DATE
);

create table scheme_enrollments(
    enrollment_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    scheme_id INTEGER,
    FOREIGN KEY (scheme_id) REFERENCES welfare_schemes(scheme_id),
    enrollment_date DATE NOT NULL
);

create table vaccinations(
    vaccination_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    vaccine_type VARCHAR(200) NOT NULL,
    date DATE NOT NULL
);

create table census_data(
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

create table tax(
    tax_id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    payment_date DATE NOT NULL,
    status VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200),
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)
);

create table income(
    income_id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    income_date DATE NOT NULL,
    source VARCHAR(200),
    financial_year VARCHAR(200)
);

create table expenditure(
    expenditure_id SERIAL PRIMARY KEY,
    amount DECIMAL NOT NULL,
    expenditure_date DATE NOT NULL,
    purpose VARCHAR(200),
    category VARCHAR(200),
    payment_mode VARCHAR(200),
    financial_year VARCHAR(200)
);

create table service(
    service_id SERIAL PRIMARY KEY,
    type VARCHAR(200) NOT NULL,
    status VARCHAR(200),
    request_date DATE
);

create table service_requests(
    request_id SERIAL PRIMARY KEY,
    citizen_id INTEGER,
    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),
    service_id INTEGER,
    FOREIGN KEY (service_id) REFERENCES service(service_id),
    request_date DATE NOT NULL,
    status VARCHAR(200)
);



INSERT INTO households (household_id, address, number_of_members, income) VALUES
(1, 'Main Street, Ward 1', 4, 80000),
(2, 'Temple Road, Ward 2', 3, 60000),
(3, 'Agricultural Lane, Ward 3', 5, 240000),
(4, 'River Side, Ward 1', 2, 90000),
(5, 'School Street, Ward 2', 6, 300000),
(6, 'Market Road, Ward 3', 4, 120000),
(7, 'Village Center, Ward 1', 3, 75000),
(8, 'Riverside Colony, Ward 2', 5, 180000),
(9, 'Farm Quarters, Ward 3', 4, 95000),
(10, 'Green Avenue, Ward 1', 6, 220000);  -- Sarpanch's household

INSERT INTO citizens VALUES
(1, '123456789012', 'Rajesh', 'Kumar', '1975-03-15', '9876543210', 48, 'General', 'Male', 1, 'Graduate', 'Teacher', 'Married'),
(2, '234567890123', 'Priya', 'Sharma', '1980-07-22', '8765432109', 43, 'SC', 'Female', 1, 'High School', 'Farmer', 'Married'),
(3, '345678901234', 'Amit', 'Patel', '1990-11-05', '7654321098', 33, 'General', 'Male', 2, 'Diploma', 'Small Business', 'Single'),
(4, '456789012345', 'Sunita', 'Devi', '1985-05-18', '6543210987', 38, 'OBC', 'Female', 1, 'Graduate', 'Agricultural Worker', 'Married'),
(5, '567890123456', 'Vikram', 'Singh', '1970-09-30', '5432109876', 53, 'General', 'Male', 4, 'Post Graduate', 'Government Employee', 'Married'),
(6, '678901234567', 'Neha', 'Gupta', '2005-02-14', '9988776655', 18, 'General', 'Female', 5, '10th Class', 'Student', 'Single'),
(7, '789012345678', 'Rahul', 'Verma', '2002-09-20', '8877665544', 21, 'SC', 'Male', 6, '12th Class', 'College Student', 'Single'),
(8, '890123456789', 'Meera', 'Kumari', '2010-06-15', '7766554433', 13, 'OBC', 'Female', 7, '10th Class', 'Student', 'Single'),
(9, '901234567890', 'Suresh', 'Yadav', '1985-11-25', '6655443322', 38, 'General', 'Male', 8, 'Graduate', 'Small Farmer', 'Married'),
(10, '012345678901', 'Kavita', 'Devi', '1990-04-10', '5544332211', 33, 'SC', 'Female', 9, '10th Class', 'Agricultural Laborer', 'Married'),
(11, '135792468024', 'Ramesh', 'Mahto', '1965-08-30', '9999888777', 58, 'General', 'Male', 10, 'Graduate', 'Sarpanch', 'Married'),
-- Additional entries for query F, I, and J:
(12, '246813579135', 'Anita', 'Mahto', '1970-04-12', '1122334455', 54, 'General', 'Female', 10, 'Graduate', 'Housewife', 'Married'),
(13, '369258147036', 'Rohit', 'Mahto', '2024-01-01', '5544667788', 0, 'General', 'Male', 10, NULL, 'Child', 'Single'),
(14, '147258369014', 'Raj', 'Patel', '2020-05-05', '8899001122', 3, 'General', 'Male', 2, NULL, 'Child', 'Single');


INSERT INTO land_records VALUES
(1, 2, 5.5, 'Wheat'),
(2, 4, 3.2, 'Rice'),
(3, 5, 2.8, 'Sugarcane'),
(4, 9, 1.5, 'Rice'),
(5, 11, 2.0, 'Wheat'),
(6, 12, 1.2, 'Rice');  -- Additional entry

INSERT INTO panchayat_employees VALUES
(1, 11, 'Sarpanch'),
(2, 5, 'Secretary'),
(3, 3, 'Revenue Collector'),
(4, 14, 'Clerk');  -- New employee

INSERT INTO assets VALUES
(1, 'Street Light', 50000, 'Phulera', 'Main Road Light', '2024-01-15'),
(2, 'Street Light', 50000, 'Phulera', 'Market Light', '2024-02-20'),
(3, 'Street Light', 50000, 'Phulera', 'School Light', '2024-03-10');


INSERT INTO welfare_schemes VALUES 
             (1, 'Pradhan Mantri Awas Yojana', 'Housing for All', 'Below Poverty Line Families', 'Free Housing', '2022-01-01', '2024-12-31'), 
             (2, 'PM Kisan Samman Nidhi', 'Direct Income Support to Farmers', 'Small and Marginal Farmers', 'Financial Assistance ₹6000/Year', '2019-02-24', NULL), 
             (3, 'National Social Assistance Programme', 'Social Security for Elderly', 'Senior Citizens, Widows', 'Pension and Financial Support', '2020-04-01', NULL), 
             (4, 'Mid-Day Meal Scheme', 'School Nutrition Programme', 'School Children (6-14 years)', 'Free Nutritious Meal', '2021-06-15', NULL), 
             (5, 'Pradhan Mantri Matru Vandana Yojana', 'Maternity Benefit Programme', 'Pregnant and Lactating Women', 'Cash Incentive ₹5000', '2017-09-01', NULL);

             
INSERT INTO scheme_enrollments VALUES 
             (1, 1, 1, '2022-06-15'), 
             (2, 3, 2, '2022-07-20'), 
             (3, 4, 3, '2022-08-10'), 
             (4, 2, 4, '2022-09-05'), 
             (5, 5, 5, '2022-10-12');

INSERT INTO vaccinations VALUES
(1, 6, 'COVID-19', '2024-01-15'),
(2, 7, 'COVID-19', '2024-02-20'),
(3, 8, 'COVID-19', '2024-03-10'),
(4, 13, 'Polio', '2024-04-01');  -- 2024-born child

INSERT INTO census_data VALUES 
             (1, 1, 1, 2023, 4, 'Rural Family', 'Household Census Data', 'Population Survey', '2023-03-15'), 
             (2, 2, 3, 2023, 3, 'Working Class Family', 'Household Census Data', 'Population Survey', '2023-03-16'), 
             (3, 3, 4, 2023, 4, 'Middle-Income Family', 'Household Census Data', 'Population Survey', '2023-03-17'), 
             (4, 4, 5, 2023, 2, 'Small Family', 'Household Census Data', 'Population Survey', '2023-03-18'), 
             (5, 5, 6, 2023, 3, 'Young Professional Family', 'Household Census Data', 'Population Survey', '2023-03-19');

INSERT INTO income VALUES 
             (1, 50000.00, '2024-04-15', 'Government Subsidy', '2023-2024'), 
             (2, 75000.00, '2024-05-10', 'Agricultural Sale', '2023-2024'), 
             (3, 60000.00, '2024-06-20', 'Rent', '2023-2024');

INSERT INTO tax VALUES 
             (1, 5000.00, '2023-03-15', 'Paid', 'Online', '2023-2024', 1), 
             (2, 3000.00, '2023-04-10', 'Pending', 'Cash', '2023-2024', 2), 
             (3, 7000.00, '2023-05-05', 'Paid', 'Card', '2023-2024', 3), 
             (4, 4000.00, '2023-06-20', 'Paid', 'UPI', '2023-2024', 4), 
             (5, 6000.00, '2023-07-25', 'Pending', 'Cheque', '2023-2024', 5);
#!/bin/bash

# Configuration
NUM_CLIENTS=5
SERVER_IP="127.0.0.1"
SERVER_PORT=80801
TEST_DIR="testfiles"
KEY="DEFPRTVWLMZAYGHQSIUJXKBCNO"  # Sample encryption key

# Create test directory if it doesn't exist
# mkdir -p "$TEST_DIR"

# Function to create a test file
create_test_file() {
    local file_path="$TEST_DIR/a_$1.txt"
    echo "This is a test file for client $1" > "$file_path"
    echo "$file_path"
}

# Function to run a client instance
test_client() {
    local client_num=$1
    local test_file=$(create_test_file "$client_num")
    
    echo "Starting client instance $client_num with file: $test_file"
    
    # Create input file for the client
    local input_file="sample.txt"
    echo "$test_file" > "$input_file"
    echo "$KEY" >> "$input_file"
    echo "No" >> "$input_file"
    
    # Run the client with input redirection
    ./retrieveencfileclient < "$input_file" > "$TEST_DIR/output_$client_num.txt" 2>&1
    
    # Check if encrypted file was created
    if [ -f "${test_file}.enc" ]; then
        echo "Client $client_num: Encryption successful"
    else
        echo "Client $client_num: Encryption failed"
    fi
    
    # Clean up input file
    rm -f "$input_file"
}

# Compile the client if needed
if [ ! -f "./retrieveencfileclient" ]; then
    echo "Compiling client..."
    gcc -o retrieveencfileclient retrieveencfileclient.c
fi

# Ensure the server is running before starting the test
echo "Please ensure the server is running on $SERVER_IP:$SERVER_PORT"
echo "Press Enter to continue..."
read

echo "Starting load test with $NUM_CLIENTS clients..."

# Run multiple clients in parallel
for i in $(seq 1 $NUM_CLIENTS); do
    test_client "$i" &
done

# Wait for all background jobs to finish
wait

# Print results before cleanup
echo "Results:"
successful_encryptions=$(ls "$TEST_DIR"/*.enc 2>/dev/null | wc -l)
echo "Successful encryptions: $successful_encryptions / $NUM_CLIENTS"

# Check for any error messages in output files
echo -e "\nChecking for errors:"
for i in $(seq 1 $NUM_CLIENTS); do
    if [ -f "$TEST_DIR/output_$i.txt" ]; then
        errors=$(grep -i "error\|failed" "$TEST_DIR/output_$i.txt")
        if [ ! -z "$errors" ]; then
            echo "Client $i errors:"
            echo "$errors"
        fi
    fi
done

# Clean up test files
# echo -e "\nCleaning up test files..."
# rm -rf "$TEST_DIR"

echo "Load test completed with $NUM_CLIENTS requests."

INSERT INTO service VALUES 
             (1, 'Internet', 'Active', '2024-03-10'), 
             (2, 'Electricity', 'Inactive', '2024-02-05'), 
             (3, 'Water Supply', 'Active', '2024-01-20');

INSERT INTO service_requests VALUES 
             (1, 1, 1, '2024-03-15', 'Completed'), 
             (2, 2, 2, '2024-02-10', 'Pending'), 
             (3, 3, 3, '2024-01-25', 'Completed');



-- A. Citizens with >1 acre land
SELECT c.first_name, c.last_name
FROM citizens c
JOIN land_records l ON c.citizen_id = l.citizen_id
WHERE l.area_acres > 1;

-- B. School-going girls in low-income households
SELECT c.first_name, c.last_name
FROM citizens c
JOIN households h ON c.household_id = h.household_id
WHERE c.gender = 'Female'
  AND c.occupation = 'Student'
  AND C.age BETWEEN 5 AND 18
  AND h.income < 100000;

-- C. Total rice cultivation acres
SELECT SUM(l.area_acres) AS total_rice_acres
FROM land_records l
WHERE l.crop_type = 'Rice';

-- D. Post-2000 born with 10th class
SELECT COUNT(*) AS total_citizens
FROM citizens
WHERE date_of_birth > '2000-01-01'
  AND educational_qualification = '10th Class';

-- E. Panchayat employees with >1 acre land
SELECT c.first_name, c.last_name
FROM citizens c
JOIN panchayat_employees p ON c.citizen_id = p.citizen_id
JOIN land_records l ON c.citizen_id = l.citizen_id
WHERE l.area_acres > 1;

-- F. Sarpanch's household members
SELECT c.first_name, c.last_name
FROM citizens c
WHERE c.household_id = (
    SELECT household_id FROM citizens
    WHERE citizen_id = (SELECT citizen_id FROM panchayat_employees WHERE role = 'Sarpanch')
);

-- G. Phulera street lights installed in 2024 (PostgreSQL)
SELECT COUNT(*) AS total_street_lights
FROM assets
WHERE type = 'Street Light'
  AND location = 'Phulera'
  AND EXTRACT(YEAR FROM installation_date) = 2024;

-- H. 2024 vaccinations for 10th class-educated parents' children
SELECT COUNT(*) AS total_vaccinations
FROM vaccinations v
JOIN citizens child ON v.citizen_id = child.citizen_id
JOIN citizens parent ON child.household_id = parent.household_id
WHERE EXTRACT(YEAR FROM v.date) = 2024
  AND parent.educational_qualification = '10th Class';

-- I. Male births in 2024
SELECT COUNT(*) AS total_boy_births
FROM citizens
WHERE gender = 'Male'
  AND EXTRACT(YEAR FROM date_of_birth) = 2024;  

-- J. Citizens in panchayat employee households
SELECT COUNT(DISTINCT c.citizen_id) AS total_citizens_in_panchayat_employee_households
FROM citizens c
WHERE c.household_id IN (
    SELECT DISTINCT household_id
    FROM panchayat_employees pe
    JOIN citizens emp ON pe.citizen_id = emp.citizen_id
);
