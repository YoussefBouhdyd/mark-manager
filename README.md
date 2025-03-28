# Mark-Manger

Mark-Manger is a simple web application designed for students and teachers. Teachers can insert students' grades, and students can access their grades through their accounts.

## Features
- **Teacher Dashboard**: Add, update, and manage student grades.
- **Student Access**: View grades through individual accounts.
- **User Authentication**: Secure login system for teachers and students.
- **Simple and Intuitive UI**: Easy navigation and interaction.

## Installation

### Prerequisites
- Python (>=3.8)
- Flask
- SQLite (or any preferred database)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/mark-mange.git
   cd mark-mange
   ```
2. Create and Activate Virtul Environment
   
   for `Mac` and `Linux` users
   ```bash
   python3 -m venv mark-ve
   source mark-ve/bin/activate
   ```
   for `Windows` users
   ```bash
   python -m venv mark-ve
   source mark-ve\Scripts\activate
   ```
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
5. Initialise the database
   ```bash
   flask db init
   flask db migrate -m "Recreating migrations"
   flask db upgrade
   ```
5. Run the application:
   ```bash
   python app.py
   ```
6. Open your browser and visit:
   ```
   http://127.0.0.1:5000
   ```

## Usage
1. **Teacher Login**: Teachers can log in and enter student grades.
2. **Student Login**: Students can log in and view their grades.
3. **Admin Panel (Optional)**: Manage users and system settings.

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Database**: SQLite / MySQL (configurable)
