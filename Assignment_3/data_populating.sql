
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

INSERT INTO vaccinations VALUES
(1, 6, 'Polio', '2024-01-15'),
(2, 7, 'Polio', '2024-02-20'),
(3, 8, 'Polio', '2024-03-10'),
(4, 13, 'Polio', '2024-04-01');  