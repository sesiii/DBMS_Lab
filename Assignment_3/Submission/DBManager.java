import java.sql.*;
import java.util.ArrayList;
import java.util.List;

public class DBManager {

    public static void main(String[] args) {
        // Database connection parameters.
        String url = "jdbc:postgresql://10.5.18.69:5432/22CS10020";
        String user = "22CS10020";
        String password = "22CS10020";

        int queryNum = 0;

        try (Connection conn = DriverManager.getConnection(url, user, password)) {
            System.out.println("Database connected successfully.\n");
            Statement stmt = conn.createStatement();

            // --- DROP TABLES ---
            String[] dropQueries = {
                "DROP TABLE IF EXISTS citizens CASCADE",
                "DROP TABLE IF EXISTS households CASCADE",
                "DROP TABLE IF EXISTS land_records CASCADE",
                "DROP TABLE IF EXISTS panchayat_employees CASCADE",
                "DROP TABLE IF EXISTS assets CASCADE",
                "DROP TABLE IF EXISTS vaccinations CASCADE",
                "DROP TABLE IF EXISTS welfare_schemes CASCADE",
                "DROP TABLE IF EXISTS scheme_enrollments CASCADE",
                "DROP TABLE IF EXISTS census_data CASCADE",
                "DROP TABLE IF EXISTS tax CASCADE",
                "DROP TABLE IF EXISTS income CASCADE",
                "DROP TABLE IF EXISTS expenditure CASCADE",
                "DROP TABLE IF EXISTS service CASCADE",
                "DROP TABLE IF EXISTS service_requests CASCADE"
            };

            System.out.println("Dropping existing tables (if any)...");
            for (String q : dropQueries) {
                queryNum++;
                try {
                    stmt.executeUpdate(q);
                    // Uncomment the next line for detailed feedback:
                    // System.out.println("Query " + queryNum + " executed successfully: Table dropped.");
                } catch (SQLException e) {
                    System.err.println("Query " + queryNum + " failed: " + e.getMessage());
                }
            }
            System.out.println("All tables dropped successfully.\n");

            // --- CREATE TABLES ---
            String[] createQueries = {
                "CREATE TABLE households(" +
                    " household_id SERIAL PRIMARY KEY," +
                    " address VARCHAR(200) NOT NULL," +
                    " number_of_members INTEGER NOT NULL," +
                    " income INTEGER" +
                    ");",

                "CREATE TABLE citizens(" +
                    " citizen_id SERIAL PRIMARY KEY," +
                    " aadhar_no VARCHAR(200) UNIQUE NOT NULL," +
                    " first_name VARCHAR(200) NOT NULL," +
                    " last_name VARCHAR(200) NOT NULL," +
                    " date_of_birth DATE NOT NULL," +
                    " phone_number VARCHAR(200)," +
                    " age INTEGER," +
                    " caste VARCHAR(200)," +
                    " gender VARCHAR(200) NOT NULL," +
                    " household_id INTEGER NOT NULL," +
                    " FOREIGN KEY (household_id) REFERENCES households(household_id)," +
                    " educational_qualification VARCHAR(200)," +
                    " occupation VARCHAR(200)," +
                    " marital_status VARCHAR(200)" +
                    ");",

                "CREATE TABLE land_records (" +
                    " record_id SERIAL PRIMARY KEY," +
                    " citizen_id INTEGER," +
                    " area_acres NUMERIC(5,2)," +
                    " crop_type VARCHAR(200)" +
                    ");",

                "CREATE TABLE panchayat_employees (" +
                    " emp_id SERIAL PRIMARY KEY," +
                    " citizen_id INTEGER," +
                    " role VARCHAR(200)" +
                    ");",

                "CREATE TABLE assets (" +
                    " asset_id SERIAL PRIMARY KEY," +
                    " type VARCHAR(200)," +
                    " cost INTEGER," +
                    " location VARCHAR(200)," +
                    " description VARCHAR(200)," +
                    " installation_date DATE" +
                    ");",

                "CREATE TABLE welfare_schemes(" +
                    " scheme_id SERIAL PRIMARY KEY," +
                    " name VARCHAR(200) NOT NULL," +
                    " description VARCHAR(200)," +
                    " eligibility VARCHAR(200)," +
                    " benefits VARCHAR(200)," +
                    " start_date DATE," +
                    " end_date DATE" +
                    ");",

                "CREATE TABLE scheme_enrollments(" +
                    " enrollment_id SERIAL PRIMARY KEY," +
                    " citizen_id INTEGER," +
                    " FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)," +
                    " scheme_id INTEGER," +
                    " FOREIGN KEY (scheme_id) REFERENCES welfare_schemes(scheme_id)," +
                    " enrollment_date DATE NOT NULL" +
                    ");",

                "CREATE TABLE vaccinations (" +
                    " vaccination_id SERIAL PRIMARY KEY," +
                    " citizen_id INTEGER," +
                    " vaccine_name VARCHAR(200)," +
                    " date DATE" +
                    ");",

                "CREATE TABLE census_data(" +
                    " census_id SERIAL PRIMARY KEY," +
                    " household_id INTEGER," +
                    " FOREIGN KEY (household_id) REFERENCES households(household_id)," +
                    " citizen_id INTEGER," +
                    " FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)," +
                    " year INTEGER NOT NULL," +
                    " population INTEGER NOT NULL," +
                    " demographics VARCHAR(200)," +
                    " description VARCHAR(200)," +
                    " event_type VARCHAR(200)," +
                    " event_date DATE" +
                    ");",

                "CREATE TABLE tax(" +
                    " tax_id SERIAL PRIMARY KEY," +
                    " amount DECIMAL NOT NULL," +
                    " payment_date DATE NOT NULL," +
                    " status VARCHAR(200)," +
                    " payment_mode VARCHAR(200)," +
                    " financial_year VARCHAR(200)," +
                    " citizen_id INTEGER," +
                    " FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)" +
                    ");",

                "CREATE TABLE income(" +
                    " income_id SERIAL PRIMARY KEY," +
                    " amount DECIMAL NOT NULL," +
                    " income_date DATE NOT NULL," +
                    " source VARCHAR(200)," +
                    " financial_year VARCHAR(200)" +
                    ");",

                "CREATE TABLE expenditure(" +
                    " expenditure_id SERIAL PRIMARY KEY," +
                    " amount DECIMAL NOT NULL," +
                    " expenditure_date DATE NOT NULL," +
                    " purpose VARCHAR(200)," +
                    " category VARCHAR(200)," +
                    " payment_mode VARCHAR(200)," +
                    " financial_year VARCHAR(200)" +
                    ");",

                "CREATE TABLE service(" +
                    " service_id SERIAL PRIMARY KEY," +
                    " type VARCHAR(200) NOT NULL," +
                    " status VARCHAR(200)," +
                    " request_date DATE" +
                    ");",

                "CREATE TABLE service_requests(" +
                    " request_id SERIAL PRIMARY KEY," +
                    " citizen_id INTEGER," +
                    " FOREIGN KEY (citizen_id) REFERENCES citizens(citizen_id)," +
                    " service_id INTEGER," +
                    " FOREIGN KEY (service_id) REFERENCES service(service_id)," +
                    " request_date DATE NOT NULL," +
                    " status VARCHAR(200)" +
                    ");"
            };

            System.out.println("Creating tables...");
            for (String q : createQueries) {
                queryNum++;
                try {
                    stmt.executeUpdate(q);
                    // Uncomment the next line for detailed feedback:
                    // System.out.println("Query " + queryNum + " executed successfully: Table created.");
                } catch (SQLException e) {
                    System.err.println("Query " + queryNum + " failed: " + e.getMessage());
                }
            }
            System.out.println("All tables created successfully.\n");

            // --- INSERT DATA ---
            String[] insertQueries = {
                "INSERT INTO households VALUES " +
                    "(1, 'Main Street, Ward 1', 4, 80000), " +
                    "(2, 'Temple Road, Ward 2', 3, 60000), " +
                    "(3, 'Agricultural Lane, Ward 3', 5, 240000), " +
                    "(4, 'River Side, Ward 1', 2, 90000), " +
                    "(5, 'School Street, Ward 2', 6, 300000), " +
                    "(6, 'Market Road, Ward 3', 4, 120000), " +
                    "(7, 'Village Center, Ward 1', 3, 75000), " +
                    "(8, 'Riverside Colony, Ward 2', 5, 180000), " +
                    "(9, 'Farm Quarters, Ward 3', 4, 95000), " +
                    "(10, 'Green Avenue, Ward 1', 6, 220000);",

                "INSERT INTO citizens VALUES " +
                    "(1, '123456789012', 'Rajesh', 'Kumar', '1975-03-15', '9876543210', 48, 'General', 'Male', 1, 'Graduate', 'Teacher', 'Married'), " +
                    "(2, '234567890123', 'Priya', 'Sharma', '1980-07-22', '8765432109', 43, 'SC', 'Female', 1, 'High School', 'Farmer', 'Married'), " +
                    "(3, '345678901234', 'Amit', 'Patel', '1990-11-05', '7654321098', 33, 'General', 'Male', 2, 'Diploma', 'Small Business', 'Single'), " +
                    "(4, '456789012345', 'Sunita', 'Devi', '1985-05-18', '6543210987', 38, 'OBC', 'Female', 1, 'Graduate', 'Agricultural Worker', 'Married'), " +
                    "(5, '567890123456', 'Vikram', 'Singh', '1970-09-30', '5432109876', 53, 'General', 'Male', 4, 'Post Graduate', 'Government Employee', 'Married'), " +
                    "(6, '678901234567', 'Neha', 'Gupta', '2005-02-14', '9988776655', 18, 'General', 'Female', 5, '10th Class', 'Student', 'Single'), " +
                    "(7, '789012345678', 'Rahul', 'Verma', '2002-09-20', '8877665544', 21, 'SC', 'Male', 6, '12th Class', 'College Student', 'Single'), " +
                    "(8, '890123456789', 'Meera', 'Kumari', '2010-06-15', '7766554433', 13, 'OBC', 'Female', 7, '10th Class', 'Student', 'Single'), " +
                    "(9, '901234567890', 'Suresh', 'Yadav', '1985-11-25', '6655443322', 38, 'General', 'Male', 8, 'Graduate', 'Small Farmer', 'Married'), " +
                    "(10, '012345678901', 'Kavita', 'Devi', '1990-04-10', '5544332211', 33, 'SC', 'Female', 9, '10th Class', 'Agricultural Laborer', 'Married'), " +
                    "(11, '135792468024', 'Ramesh', 'Mahto', '1965-08-30', '9999888777', 58, 'General', 'Male', 10, 'Graduate', 'Sarpanch', 'Married'), " +
                    "(12, '246813579135', 'Anita', 'Mahto', '1970-04-12', '1122334455', 54, 'General', 'Female', 10, 'Graduate', 'Housewife', 'Married'), " +
                    "(13, '369258147036', 'Rohit', 'Mahto', '2024-01-01', '5544667788', 0, 'General', 'Male', 10, NULL, 'Child', 'Single'), " +
                    "(14, '147258369014', 'Raj', 'Patel', '2020-05-05', '8899001122', 3, 'General', 'Male', 2, NULL, 'Child', 'Single');",

                "INSERT INTO land_records VALUES " +
                    "(1, 2, 5.5, 'Wheat'), " +
                    "(2, 4, 3.2, 'Rice'), " +
                    "(3, 5, 2.8, 'Sugarcane'), " +
                    "(4, 9, 1.5, 'Rice'), " +
                    "(5, 11, 2.0, 'Wheat'), " +
                    "(6, 12, 1.2, 'Rice');",

                "INSERT INTO panchayat_employees VALUES " +
                    "(1, 11, 'Sarpanch'), " +
                    "(2, 5, 'Secretary'), " +
                    "(3, 3, 'Revenue Collector'), " +
                    "(4, 14, 'Clerk');",

                "INSERT INTO assets VALUES " +
                    "(1, 'Toilet', 5000, 'Phulera', 'Main Road Light', '2024-01-15'), " +
                    "(2, 'Community Hall', 50000, 'Phulera', 'Market Light', '2024-02-20'), " +
                    "(3, 'Street Light', 50000, 'Phulera', 'School Light', '2024-03-10');",

                "INSERT INTO vaccinations VALUES " +
                    "(1, 6, 'Polio', '2024-01-15'), " +
                    "(2, 7, 'Polio', '2024-02-20'), " +
                    "(3, 8, 'Polio', '2024-03-10'), " +
                    "(4, 13, 'Polio', '2024-04-01');",

                "INSERT INTO welfare_schemes VALUES " +
                    "(1, 'Pradhan Mantri Awas Yojana', 'Housing for All', 'Below Poverty Line Families', 'Free Housing', '2022-01-01', '2024-12-31'), " +
                    "(2, 'PM Kisan Samman Nidhi', 'Direct Income Support to Farmers', 'Small and Marginal Farmers', 'Financial Assistance ₹6000/Year', '2019-02-24', NULL), " +
                    "(3, 'National Social Assistance Programme', 'Social Security for Elderly', 'Senior Citizens, Widows', 'Pension and Financial Support', '2020-04-01', NULL), " +
                    "(4, 'Mid-Day Meal Scheme', 'School Nutrition Programme', 'School Children (6-14 years)', 'Free Nutritious Meal', '2021-06-15', NULL), " +
                    "(5, 'Pradhan Mantri Matru Vandana Yojana', 'Maternity Benefit Programme', 'Pregnant and Lactating Women', 'Cash Incentive ₹5000', '2017-09-01', NULL);",

                "INSERT INTO scheme_enrollments VALUES " +
                    "(1, 1, 1, '2022-06-15'), " +
                    "(2, 3, 2, '2022-07-20'), " +
                    "(3, 4, 3, '2022-08-10'), " +
                    "(4, 2, 4, '2022-09-05'), " +
                    "(5, 5, 5, '2022-10-12');",

                "INSERT INTO census_data VALUES " +
                    "(1, 1, 1, 2023, 4, 'Rural Family', 'Household Census Data', 'Population Survey', '2023-03-15'), " +
                    "(2, 2, 3, 2023, 3, 'Working Class Family', 'Household Census Data', 'Population Survey', '2023-03-16'), " +
                    "(3, 3, 4, 2023, 4, 'Middle-Income Family', 'Household Census Data', 'Population Survey', '2023-03-17'), " +
                    "(4, 4, 5, 2023, 2, 'Small Family', 'Household Census Data', 'Population Survey', '2023-03-18'), " +
                    "(5, 5, 6, 2023, 3, 'Young Professional Family', 'Household Census Data', 'Population Survey', '2023-03-19');",

                "INSERT INTO tax VALUES " +
                    "(1, 5000.00, '2023-03-15', 'Paid', 'Online', '2023-2024', 1), " +
                    "(2, 3000.00, '2023-04-10', 'Pending', 'Cash', '2023-2024', 2), " +
                    "(3, 7000.00, '2023-05-05', 'Paid', 'Card', '2023-2024', 3), " +
                    "(4, 4000.00, '2023-06-20', 'Paid', 'UPI', '2023-2024', 4), " +
                    "(5, 6000.00, '2023-07-25', 'Pending', 'Cheque', '2023-2024', 5);",

                "INSERT INTO income VALUES " +
                    "(1, 50000.00, '2024-04-15', 'Government Subsidy', '2023-2024'), " +
                    "(2, 75000.00, '2024-05-10', 'Agricultural Sale', '2023-2024'), " +
                    "(3, 60000.00, '2024-06-20', 'Rent', '2023-2024');",

                "INSERT INTO expenditure VALUES " +
                    "(1, 30000.00, '2024-04-20', 'School Supplies', 'Education', 'Cash', '2023-2024'), " +
                    "(2, 20000.00, '2024-05-15', 'Medical Expenses', 'Health', 'Card', '2023-2024'), " +
                    "(3, 25000.00, '2024-06-10', 'Household Repairs', 'Maintenance', 'Online', '2023-2024');",

                "INSERT INTO service VALUES " +
                    "(1, 'Internet', 'Active', '2024-03-10'), " +
                    "(2, 'Electricity', 'Inactive', '2024-02-05'), " +
                    "(3, 'Water Supply', 'Active', '2024-01-20');",

                "INSERT INTO service_requests VALUES " +
                    "(1, 1, 1, '2024-03-15', 'Completed'), " +
                    "(2, 2, 2, '2024-02-10', 'Pending'), " +
                    "(3, 3, 3, '2024-01-25', 'Completed');"
            };

            System.out.println("\nInserting data into tables...");
            for (String q : insertQueries) {
                queryNum++;
                try {
                    stmt.executeUpdate(q);
                } catch (SQLException e) {
                    System.err.println("Query " + queryNum + " failed: " + e.getMessage());
                }
            }
            System.out.println("Data inserted successfully.\n");

            // --- SELECT QUERIES ---
            String[] selectQueries = {
                "SELECT c.first_name, c.last_name FROM citizens c JOIN land_records l ON c.citizen_id = l.citizen_id WHERE l.area_acres > 1;",
                "SELECT c.first_name, c.last_name FROM citizens c JOIN households h ON c.household_id = h.household_id WHERE c.gender = 'Female' AND c.occupation = 'Student' AND c.age BETWEEN 5 AND 18 AND h.income < 100000;",
                "SELECT SUM(l.area_acres) AS total_rice_area FROM land_records l WHERE l.crop_type = 'Rice';",
                "SELECT COUNT(*) AS young_10th_pass FROM citizens WHERE date_of_birth > '2000-01-01' AND educational_qualification = '10th Class';",
                "SELECT c.first_name, c.last_name FROM citizens c JOIN panchayat_employees p ON c.citizen_id = p.citizen_id JOIN land_records l ON c.citizen_id = l.citizen_id WHERE l.area_acres > 1;",
                "SELECT c.first_name, c.last_name FROM citizens c JOIN households h ON c.household_id = h.household_id WHERE h.household_id = (SELECT household_id FROM citizens WHERE citizen_id = (SELECT citizen_id FROM panchayat_employees WHERE role = 'Sarpanch'));",
                "SELECT COUNT(*) AS total_street_lights FROM assets WHERE type = 'Street Light' AND location = 'Phulera' AND EXTRACT(YEAR FROM installation_date) = 2024;",
                "SELECT COUNT(*) AS total_vaccinations FROM vaccinations v JOIN citizens child ON v.citizen_id = child.citizen_id JOIN citizens parent ON child.household_id = parent.household_id WHERE EXTRACT(YEAR FROM v.date) = 2024 AND parent.educational_qualification = '10th Class';",
                "SELECT COUNT(*) AS total_boy_births FROM citizens WHERE gender = 'Male' AND EXTRACT(YEAR FROM date_of_birth) = 2024;",
                "SELECT COUNT(DISTINCT c.citizen_id) AS total_citizens FROM citizens c WHERE c.household_id IN (SELECT DISTINCT household_id FROM panchayat_employees pe JOIN citizens emp ON pe.citizen_id = emp.citizen_id);"
            };

            System.out.println("Executing SELECT queries...");
            for (String q : selectQueries) {
                queryNum++;
                // System.out.println("\n=== Query " + queryNum + " ===");
                try (ResultSet rs = stmt.executeQuery(q)) {
                    List<String[]> rows = new ArrayList<>();
                    ResultSetMetaData rsmd = rs.getMetaData();
                    int colCount = rsmd.getColumnCount();
                    String[] headers = new String[colCount];
                    int[] colWidths = new int[colCount];
                    for (int i = 1; i <= colCount; i++) {
                        headers[i - 1] = rsmd.getColumnName(i);
                        colWidths[i - 1] = headers[i - 1].length();
                    }
                    while (rs.next()) {
                        String[] row = new String[colCount];
                        for (int i = 1; i <= colCount; i++) {
                            String value = rs.getString(i);
                            if (value == null) {
                                value = "NULL";
                            }
                            row[i - 1] = value;
                            colWidths[i - 1] = Math.max(colWidths[i - 1], value.length());
                        }
                        rows.add(row);
                    }
                    printTable(headers, rows, colWidths);
                } catch (SQLException e) {
                    System.err.println("Query " + queryNum + " failed: " + e.getMessage());
                }
            }

            stmt.close();
        } catch (SQLException ex) {
            System.err.println("Database connection failed: " + ex.getMessage());
        }
    }

    public static void printTable(String[] headers, List<String[]> rows, int[] colWidths) {
        // Build a border line.
        StringBuilder border = new StringBuilder("+");
        for (int width : colWidths) {
            border.append("-".repeat(width + 2)).append("+");
        }
        System.out.println(border);

        // Build header row.
        StringBuilder headerRow = new StringBuilder("|");
        for (int i = 0; i < headers.length; i++) {
            headerRow.append(" ").append(String.format("%-" + colWidths[i] + "s", headers[i])).append(" |");
        }
        System.out.println(headerRow);
        System.out.println(border);

        // Print each row.
        for (String[] row : rows) {
            StringBuilder rowStr = new StringBuilder("|");
            for (int i = 0; i < row.length; i++) {
                rowStr.append(" ").append(String.format("%-" + colWidths[i] + "s", row[i])).append(" |");
            }
            System.out.println(rowStr);
        }
        System.out.println(border);
    }
}