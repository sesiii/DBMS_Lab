
#include <iostream>
#include <pqxx/pqxx>
#include <string>
#include <vector>
#include <iomanip>

/**
 * Print a horizontal line for the table
 * @param widths Vector containing column widths
 */
void printTableLine(const std::vector<int>& widths) {
    std::cout << "+";
    for (int width : widths) {
        std::cout << std::string(width + 2, '-') << "+";
    }
    std::cout << std::endl;
}

/**
 * Executes a PostgreSQL query and prints the results in a tabular format
 * @param conn Database connection object
 * @param query SQL query string to execute
 * @param queryNum Query number for labeling
 */
void executeQuery(pqxx::connection& conn, const std::string& query, int queryNum) {
    try {
        pqxx::work txn(conn);
        pqxx::result res = txn.exec(query);

        if (res.empty()) {
            std::cout << "Query " << queryNum << ": No results found.\n\n";
            return;
        }

        // Calculate column widths
        std::vector<int> columnWidths(res.columns(), 0);
        
        // Check column names lengths
        for (size_t i = 0; i < res.columns(); ++i) {
            columnWidths[i] = std::string(res.column_name(i)).length();
        }

        // Check data lengths
        for (const auto& row : res) {
            for (size_t i = 0; i < row.size(); ++i) {
                std::string value = row[i].is_null() ? "NULL" : row[i].c_str();
                columnWidths[i] = std::max(columnWidths[i], static_cast<int>(value.length()));
            }
        }

        // Print query number
        std::cout << "Query " << queryNum << " Results:\n";

        // Print top border
        printTableLine(columnWidths);

        // Print header
        std::cout << "|";
        for (size_t i = 0; i < res.columns(); ++i) {
            std::cout << " " << std::setw(columnWidths[i]) << std::left 
                     << res.column_name(i) << " |";
        }
        std::cout << std::endl;

        // Print separator
        printTableLine(columnWidths);

        // Print data rows
        for (const auto& row : res) {
            std::cout << "|";
            for (size_t i = 0; i < row.size(); ++i) {
                std::string value = row[i].is_null() ? "NULL" : row[i].c_str();
                std::cout << " " << std::setw(columnWidths[i]) << std::left << value << " |";
            }
            std::cout << std::endl;
        }

        // Print bottom border
        printTableLine(columnWidths);
        std::cout << std::endl;

        txn.commit();
    } catch (const std::exception& e) {
        std::cerr << "Query " << queryNum << " failed: " << e.what() << std::endl << std::endl;
    }
}

int main() {
    try {
        // Establish database connection
        pqxx::connection conn(
            "dbname=22CS10020 "
            "user=22CS10020 "
            "password=22CS10020 "
            "host=10.5.18.69 "
            "port=5432"
        );

        // Array of SQL queries to execute
        std::string queries[] = {
            // "DROP TABLE IF EXISTS citizens CASCADE; "
            // "DROP TABLE IF EXISTS households CASCADE; "
            // "DROP TABLE IF EXISTS land_records CASCADE; "
            // "DROP TABLE IF EXISTS panchayat_employees CASCADE; "
            // "DROP TABLE IF EXISTS assets CASCADE; "
            // "DROP TABLE IF EXISTS vaccinations CASCADE; "
            // "DROP TABLE IF EXISTS welfare_schemes CASCADE; "
            // "DROP TABLE IF EXISTS scheme_enrollments CASCADE; "
            // "DROP TABLE IF EXISTS census_data CASCADE; "
            // "DROP TABLE IF EXISTS tax CASCADE; "
            // "DROP TABLE IF EXISTS income CASCADE; "
            // "DROP TABLE IF EXISTS expenditure CASCADE; "
            // "DROP TABLE IF EXISTS service CASCASE;"
            // "DROP TABLE IF EXIXTS servive_requests CASCADE;",

            
            // "create table households("
            // "    household_id SERIAL PRIMARY KEY,"
            // "    address VARCHAR(200) NOT NULL,"
            // "    number_of_members INTEGER NOT NULL,"
            // "    income INTEGER"
            // ");"

            // "create table citizens("
            // "    citizen_id SERIAL PRIMARY KEY,"
            // "    aadhar_no VARCHAR(200) UNIQUE NOT NULL,"
            // "    first_name VARCHAR(200) NOT NULL,"
            // "    last_name VARCHAR(200) NOT NULL,"
            // "    date_of_birth DATE NOT NULL,"
            // "    phone_number VARCHAR(200),"
            // "    age INTEGER,"
            // "    caste VARCHAR(200),"
            // "    gender VARCHAR(200) NOT NULL,"
            // "    household_id INTEGER NOT NULL,"
            // "    FOREIGN KEY (household_id) REFERENCES households(household_id),"
            // "    educational_qualification VARCHAR(200),"
            // "    occupation VARCHAR(200),"
            // "    marital_status VARCHAR(200)"
            // ");"

            // "create table land_records("
            // "    land_id SERIAL PRIMARY KEY,"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            // "    area_acres DECIMAL NOT NULL,"
            // "    crop_type VARCHAR(200)"
            // ");"

            // "create table panchayat_employees("
            // "    employee_id SERIAL PRIMARY KEY,"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            // "    role VARCHAR(200)"
            // ");"

            // "create table assets("
            // "    asset_id SERIAL PRIMARY KEY,"
            // "    type VARCHAR(200) NOT NULL,"
            // "    value DECIMAL NOT NULL,"
            // "    location VARCHAR(200),"
            // "    name VARCHAR(200),"
            // "    installation_date DATE"
            // ");"

            // "create table welfare_schemes("
            // "    scheme_id SERIAL PRIMARY KEY,"
            // "    name VARCHAR(200) NOT NULL,"
            // "    description VARCHAR(200),"
            // "    eligibility VARCHAR(200),"
            // "    benefits VARCHAR(200),"
            // "    start_date DATE,"
            // "    end_date DATE"
            // ");"

            // "create table scheme_enrollments("
            // "    enrollment_id SERIAL PRIMARY KEY,"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            // "    scheme_id INTEGER,"
            // "    FOREIGN KEY (scheme_id) REFERENCES welfare_schemes(scheme_id),"
            // "    enrollment_date DATE NOT NULL"
            // ");"

            // "create table vaccinations("
            // "    vaccination_id SERIAL PRIMARY KEY,"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            // "    vaccine_type VARCHAR(200) NOT NULL,"
            // "    date DATE NOT NULL"
            // ");"

            // "create table census_data("
            // "    census_id SERIAL PRIMARY KEY,"
            // "    household_id INTEGER,"
            // "    FOREIGN KEY (household_id) REFERENCES households(household_id),"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            // "    year INTEGER NOT NULL,"
            // "    population INTEGER NOT NULL,"
            // "    demographics VARCHAR(200),"
            // "    description VARCHAR(200),"
            // "    event_type VARCHAR(200),"
            // "    event_date DATE"
            // ");"

            // "create table tax("
            // "    tax_id SERIAL PRIMARY KEY,"
            // "    amount DECIMAL NOT NULL,"
            // "    payment_date DATE NOT NULL,"
            // "    status VARCHAR(200),"
            // "    payment_mode VARCHAR(200),"
            // "    financial_year VARCHAR(200),"
            // "    citizen_id INTEGER,"
            // "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)"
            // ");"

            // "create table income("
            // "    income_id SERIAL PRIMARY KEY,"
            // "    amount DECIMAL NOT NULL,"
            // "    income_date DATE NOT NULL,"
            // "    source VARCHAR(200),"
            // "    financial_year VARCHAR(200)"
            // ");"

            // "create table expenditure("
            // "    expenditure_id SERIAL PRIMARY KEY,"
            // "    amount DECIMAL NOT NULL,"
            // "    expenditure_date DATE NOT NULL,"
            // "    purpose VARCHAR(200),"
            // "    category VARCHAR(200),"
            // "    payment_mode VARCHAR(200),"
            // "    financial_year VARCHAR(200)"
            // ");"

            // "create table service("
            // "    service_id SERIAL PRIMARY KEY,"
            // "    type VARCHAR(200) NOT NULL,"
            // "    status VARCHAR(200),"
            // "    request_date DATE"
            // ");"

            "create table service_requests("
            "    request_id SERIAL PRIMARY KEY,"
            "    citizen_id INTEGER,"
            "    FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id),"
            "    service_id INTEGER,"
            "    FOREIGN KEY (service_id) REFERENCES service(service_id),"
            "    request_date DATE NOT NULL,"
            "    status VARCHAR(200)"
            ");"


            // Query 1: Citizens owning land > 1 acre
            "SELECT c.first_name, c.last_name "
            "FROM citizens c "
            "JOIN land_records l ON c.citizen_id = l.citizen_id "
            "WHERE l.area_acres > 1;",

            // Query 2: Female students from low-income households
            "SELECT c.first_name, c.last_name "
            "FROM citizens c "
            "JOIN households h ON c.household_id = h.household_id "
            "WHERE c.gender = 'Female' "
            "AND c.occupation = 'Student' "
            "AND c.age BETWEEN 5 AND 18 "
            "AND h.income < 100000;",

            // Query 3: Total rice cultivation area
            "SELECT SUM(l.area_acres) AS total_rice_area "
            "FROM land_records l "
            "WHERE l.crop_type = 'Rice';",

            // Query 4: Count of young citizens with 10th class education
            "SELECT COUNT(*) AS young_10th_pass "
            "FROM citizens "
            "WHERE date_of_birth > '2000-01-01' "
            "AND educational_qualification = '10th Class';",

            // Query 5: Panchayat employees owning land
            "SELECT c.first_name, c.last_name "
            "FROM citizens c "
            "JOIN panchayat_employees p ON c.citizen_id = p.citizen_id "
            "JOIN land_records l ON c.citizen_id = l.citizen_id "
            "WHERE l.area_acres > 1;",

            // Query 6: Sarpanch's household members
            "SELECT c.first_name, c.last_name "
            "FROM citizens c "
            "JOIN households h ON c.household_id = h.household_id "
            "WHERE h.household_id = ("
                "SELECT household_id "
                "FROM citizens "
                "WHERE citizen_id = ("
                    "SELECT citizen_id "
                    "FROM panchayat_employees "
                    "WHERE role = 'Sarpanch'"
                ")"
            ");",

            // Query 7: Street lights in Phulera installed in 2024
            "SELECT COUNT(*) AS total_street_lights "
            "FROM assets "
            "WHERE type = 'Street Light' "
            "AND location = 'Phulera' "
            "AND EXTRACT(YEAR FROM installation_date) = 2024;",

            // Query 8: Vaccinations for children of 10th pass parents in 2024
            "SELECT COUNT(*) AS total_vaccinations "
            "FROM vaccinations v "
            "JOIN citizens child ON v.citizen_id = child.citizen_id "
            "JOIN citizens parent ON child.household_id = parent.household_id "
            "WHERE EXTRACT(YEAR FROM v.date) = 2024 "
            "AND parent.educational_qualification = '10th Class';",

            // Query 9: Male births in 2024
            "SELECT COUNT(*) AS total_boy_births "
            "FROM citizens "
            "WHERE gender = 'Male' "
            "AND EXTRACT(YEAR FROM date_of_birth) = 2024;",

            // Query 10: Count of citizens in panchayat employee households
            "SELECT COUNT(DISTINCT c.citizen_id) AS total_citizens "
            "FROM citizens c "
            "WHERE c.household_id IN ("
                "SELECT DISTINCT household_id "
                "FROM panchayat_employees pe "
                "JOIN citizens emp ON pe.citizen_id = emp.citizen_id"
            ");"
        };

        // Execute each query and print results
        for (size_t i = 0; i < sizeof(queries)/sizeof(queries[0]); ++i) {
            executeQuery(conn, queries[i], i + 1);
        }

    } catch (const std::exception& e) {
        std::cerr << "Database connection failed: " << e.what() << std::endl;
        return 1;
    }

    return 0;
}