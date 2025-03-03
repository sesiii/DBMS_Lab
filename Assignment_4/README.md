# Gram Panchayat Management System (GPMS)

![GPMS Banner](images/village_banner.jpg)

## 📋 Overview

The Gram Panchayat Management System (GPMS) is a comprehensive web application designed to digitize and streamline the administrative operations of village-level local government institutions in India. This system facilitates efficient management of citizen data, welfare schemes, public services, financial records, and statistical analysis.

**Current Version:** 1.0.0  
**Last Updated:** 2025-03-03

## 🌟 Features

### Citizen Management
- Citizen registration and profile management
- Household tracking
- Demographic data collection and analysis
- Vaccination records management

### Administrative Functions
- Multi-level user roles (Admin, Panchayat Employee, Citizen, Government Monitor)
- Role-based access control
- Employee request and approval system
- Data validation and verification

### Welfare & Services
- Welfare scheme enrollment and management
- Service request tracking
- Public infrastructure management
- Document issuing and verification

### Financial Management
- Tax collection and records
- Citizen income tracking
- Expenditure management
- Financial year-wise reporting

### Environmental & Development Data
- Environmental data collection and monitoring
- Census data management
- Land records maintenance
- Asset tracking

### Analytics & Reporting
- Population statistics dashboard
- Gender, age, and education distribution analysis
- Filterable demographic reports
- Data export functionality

## 🛠️ Technology Stack

- **Backend:** Flask (Python web framework)
- **Database:** PostgreSQL
- **ORM:** SQLAlchemy
- **Frontend:** HTML, CSS, JavaScript, Bootstrap 5
- **Authentication:** Session-based with password hashing
- **Additional Libraries:** Font Awesome, Chart.js

## ⚙️ Installation

### Prerequisites
- Python 3.8+
- PostgreSQL 13+
- pip (Python package manager)

### Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/sesiii/DBMS_lab/Assignment_4.git
   
   ```

2. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure database:**
   - Create a PostgreSQL database
   - Update the database URI in `app.py`:
     ```python
     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/database_name'
     ```

5. **Initialize the database:**
   ```bash
   flask shell
   >>> from app import db
   >>> db.create_all()
   >>> exit()
   ```

6. **Start the application:**
   ```bash
   flask run
   ```

7. **Access the application:**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📊 Database Schema

The application uses the following key tables:

- **citizens:** Core citizen demographic data
- **households:** Family unit grouping
- **welfare_schemes:** Government assistance programs
- **scheme_enrollments:** Citizen enrollment in welfare schemes
- **service:** Available public services
- **service_requests:** Citizen requests for services
- **tax:** Tax collection records
- **income:** Citizen income records
- **expenditure:** Panchayat expenditure tracking
- **vaccinations:** Health records for vaccinations
- **environmental_data:** Environmental metrics
- **assets:** Panchayat property and equipment tracking
- **land_records:** Property ownership records
- **census:** Population census data

## 📱 Usage Guide

### User Roles

1. **Admin**
   - System configuration
   - User approval
   - Master data management
   - Complete access to all modules

2. **Panchayat Employee**
   - Service request management
   - Data entry for various modules
   - Report generation
   - Limited administrative functions

3. **Citizen**
   - Profile management
   - Service requests
   - Scheme applications
   - Tax payments
   - Income declarations

4. **Government Monitor**
   - Statistical analysis
   - Report viewing
   - Data monitoring without modification rights

### Core Workflows

1. **Citizen Registration**
   - Fill registration form
   - Submit for verification
   - Admin approval
   - Account activation

2. **Service Request Management**
   - Submit request
   - Request tracking
   - Status updates
   - Resolution documentation

3. **Welfare Scheme Enrollment**
   - View available schemes
   - Check eligibility
   - Submit application
   - Track enrollment status

4. **Tax Management**
   - Submit tax declaration
   - Receive confirmation
   - View payment history

## 📊 Analytics Dashboard

The system includes a comprehensive statistics dashboard that provides:

- Gender distribution analysis
- Age demographic breakdown
- Education level statistics
- Birth rate trends over time

The dashboard supports:
- Multiple filter options
- Grouping by various parameters
- Data export functionality
- Visual representations

## 🤝 Contributing

We welcome contributions to improve the Gram Panchayat Management System!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

Please ensure your code follows the project's coding standards and includes appropriate tests.

## 📜 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Contact

For questions or support, please contact:
coming soon...
---

Made with ❤️ for efficient local governance
