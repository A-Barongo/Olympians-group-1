# 🏥 Olympian Hospital Database

**Olympian Hospital Database** is a command-line application built using **Python** and **SQLAlchemy ORM**, designed to manage hospital operations such as patient records, doctor rosters, and appointment scheduling. This project provides a simple but powerful way to interact with hospital data via a menu-driven CLI interface.

---

## Features

- **Patients**
  - Create, view, search, and delete patients.
  - View all patients or today's registered patients.

- **Doctors**
  - Create, view, search, update, and delete doctors.
  - Filter doctors by name or specialty.

- **Appointments**
  - Schedule, view, update, or cancel appointments.
  - Filter appointments by doctor, patient, or date.
  - View all appointments scheduled for today.

- **Seeding**
  - Use Faker to generate realistic dummy data for testing.

---

##  Tech Stack

- **Python 3**
- **SQLAlchemy (ORM)**
- **SQLite** (for development)
- **Faker** (for generating fake data)
- **CLI Interface** (via `input()`)

---

##  Database Model

### Patient
| Column       | Type         | Description             |
|--------------|--------------|-------------------------|
| id           | Integer (PK) | Unique identifier       |
| name         | String       | Patient full name       |
| age          | Integer      | Patient age             |
| gender       | Enum         | `Male`, `Female`, `Other` |
| registered_at| DateTime     | Timestamp of registration |

###  Doctor
| Column       | Type         | Description             |
|--------------|--------------|-------------------------|
| id           | Integer (PK) | Unique identifier       |
| name         | String       | Doctor full name        |
| specialty    | String       | Medical specialty       |
| created_at   | DateTime     | Timestamp of entry      |

###  Appointment
| Column       | Type         | Description             |
|--------------|--------------|-------------------------|
| id           | Integer (PK) | Unique identifier       |
| patient_id   | Integer (FK) | Linked to `Patient.id`  |
| doctor_id    | Integer (FK) | Linked to `Doctor.id`   |
| date         | Date         | Appointment date        |
| time         | Time         | Appointment time        |
| created_at   | DateTime     | Timestamp of booking    |

---

##  How to Use

### 1. Clone the Repository


git clone https://github.com/yourusername/olympian-hospital-db.git  


cd olympian-hospital-db  

### 2.  Install Dependencies
Make sure you have Python 3 installed.

pip install -r requirements.txt  

### 3.  Setup Database  
Run the following to create and seed the database:  

python seed.py  

This will populate the database with fake doctors, patients, and appointments.  

### 4.  Launch the CLI 

python cli.py  

Follow the on-screen prompts to navigate the application.  

Project Structure   

olympian-hospital-db/
│
├── cli.py               # Command-line interface logic  
├── seed.py              # Script to populate the database  
├── helpers.py           # Helper functions used across the CLI  
├── database/            
│   ├── models.py        # SQLAlchemy ORM models  
│   └── __init__.py      # DB setup and session creation    
│  
├── requirements.txt     # Python dependencies  
└── README.md            # Project documentation  
✅ Sample CLI Menu
sql

1. Create a new Patient  
2. Get all Patients  
3. Get Patient by ID  
4. Search Patients by Name  
5. Get Patients Registered Today  
6. Delete Patient  
...
13. Create a new Appointment  
14. Get All Appointments  
...
23. Exit  
## Future Improvements  
Add user login/authentication for staff.  

Export data to CSV or PDF.  

Web interface using Flask or Django.  
Calendar view for appointments.  

Conflict checker for overlapping appointments.  

## Contributor
Built by :
1. Allan Barongo  
2.Emmanuel Gitau  
3.Paul Ashton   
## License  
This project is licensed under the MIT License.  

## Acknowledgements  
Faker for realistic dummy data.  
SQLAlchemy for ORM and database interaction.  
