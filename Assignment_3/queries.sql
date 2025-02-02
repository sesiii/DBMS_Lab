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