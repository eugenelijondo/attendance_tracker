from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Teacher, Student
from random import randint
from datetime import datetime
from faker import Faker
import random
from helpers import associate_student_with_teacher, dissociate_student_from_teacher, mark_student_attendance, mark_teacher_attendance

fake = Faker()

# Create an SQLite database engine
engine = create_engine('sqlite:///attendance_tracker.db', echo=True)

# Create a session
Session = sessionmaker(bind=engine)
db_session = Session()

def populate():
    # Create users (students and teachers)
    teachers = []
    students = []

    # Generate passwords for teachers
    for i in range(7):
        password = None
        while password is None:
            password = fake.password()
        teachers.append(Teacher(username="teacher_" + str(i+1), name=fake.name(), email=fake.email(), password=password, role='teacher'))

    # Generate students
    for i in range(115):
        students.append(Student(username="student_" + str(i+1), name=fake.name(), roll_number=randint(5000, 10000), role='student'))

    all_users = students + teachers
    
    # Add users to the session and commit changes
    db_session.add_all(all_users)
    db_session.commit()
    
    # Assign teachers to students
    for student in students:
        teacher = teachers[randint(0, len(teachers)-1)]
        associate_student_with_teacher(student, teacher)
        
    print("Database populated with %s students and %s teachers." % (len(students), len(teachers)))
    db_session.commit()
    
    # Dissociate teachers from students
    for student in students:
        dissociate_student_from_teacher(student)

    # Add attendance for all users
    start_date = fake.date_between(start_date='-2y', end_date='today')  # Start date for generating random dates
    end_date = datetime.now()  # End date for generating random dates
    attendance_statuses = ['Present', 'Absent', 'Late']  # Possible attendance statuses
    
    for user in all_users:
        random_date = fake.date_time_between(start_date=start_date, end_date=end_date)
        attendance_status = random.choice(attendance_statuses)
        if isinstance(user, Teacher):  # Check if the user is a teacher
            mark_teacher_attendance(user.id, random_date, attendance_status)
        else:
            mark_student_attendance(user.id, random_date, attendance_status)
    db_session.commit()

# Main code execution
if __name__ == "__main__":
    populate()  # Populate the database with data
