SELECT c.first_name, c.last_name
FROM citizens c
JOIN land_records l ON c.citizen_id = l.citizen_id
WHERE l.area_acres > 1;


SELECT c.first_name, c.last_name
FROM citizens c
JOIN households h ON c.household_id = h.household_id
WHERE c.gender = 'Female'
  AND c.occupation = 'Student'
  AND h.income < 100000;

  SELECT SUM(l.area_acres) AS total_rice_acres
FROM land_records l
WHERE l.crop_type = 'Rice';

SELECT COUNT(*) AS total_citizens
FROM citizens
WHERE date_of_birth > '2000-01-01'
  AND educational_qualification = '10th class';

SELECT c.first_name, c.last_name
FROM citizens c
JOIN panchayat_employees p ON c.citizen_id = p.citizen_id
JOIN land_records l ON c.citizen_id = l.citizen_id
WHERE l.area_acres > 1;
 

SELECT c.first_name, c.last_name
FROM citizens c
WHERE c.household_id = (
    SELECT p.household_id
    FROM panchayat_employees p
    JOIN citizens pc ON p.citizen_id = pc.citizen_id
    WHERE p.role = 'Sarpanch'
);


SELECT COUNT(*) AS total_street_lights
FROM assets
WHERE type = 'Street Light'
  AND location = 'Phulera'
  AND EXTRACT(YEAR FROM installation_date) = 2024; --psql


SELECT COUNT(*) AS total_vaccinations
FROM vaccinations v
JOIN citizens c ON v.citizen_id = c.citizen_id
WHERE EXTRACT(YEAR FROM v.date) = 2024
  AND c.educational_qualification = '10th class'
  AND c.age <= 18;                                  --psql

SELECT COUNT(*) AS total_boy_births
FROM citizens c
WHERE  gender = 'Male'
  AND EXTRACT(YEAR FROM c.date_of_birth) = 2024;

SELECT COUNT(*) AS total_boy_births
FROM citizens
WHERE gender = 'Male'
  AND YEAR(date_of_birth) = 1995; --mysql

SELECT COUNT(DISTINCT c.citizen_id) AS total_citizens
FROM citizens c
WHERE c.household_id IN (
    SELECT DISTINCT p.household_id
    FROM panchayat_employees p
    JOIN citizens pc ON p.citizen_id = pc.citizen_id
);