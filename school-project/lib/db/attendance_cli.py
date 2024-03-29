from helpers import (associate_student_with_teacher, dissociate_student_from_teacher,
                        mark_student_attendance, mark_teacher_attendance,
                        update_attendance_status, view_student_attendance,
                        view_teacher_attendance, generate_student_attendance_report,
                        generate_teacher_attendance_report)


if __name__ == "__main__":
    while True:
        print("Attendance Tracker CLI")
        print("1. Mark Student Attendance")
        print("2. Mark Teacher Attendance")
        print("3. Update Attendance Status")
        print("4. View Student Attendance")
        print("5. View Teacher Attendance")
        print("6. Generate Student Attendance Report")
        print("7. Generate Teacher Attendance Report")
        print("8. Quit the program")
        
        option = input("Enter your option (1-8): ")

        if option == "1":
            student_id = int(input("Enter student ID: "))
            date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
            status = input("Enter attendance status (Present/Absent): ")
            mark_student_attendance(student_id, date, status)
        elif option == "2":
            teacher_id = int(input("Enter teacher ID: "))
            date = input("Enter date (YYYY-MM-DD HH:MM:SS): ")
            status = input("Enter attendance status (Present/Absent): ")
            mark_teacher_attendance(teacher_id, date, status)
        elif option == "3":
            user_id = int(input("Enter user ID: "))
            new_status = input("Enter new attendance status (Present/Absent): ")
            update_attendance_status(user_id, new_status)
        elif option == "4":
            student_id = int(input("Enter student ID: "))
            view_student_attendance(student_id)
        elif option == "5":
            teacher_id = int(input("Enter teacher ID: "))
            view_teacher_attendance(teacher_id)
        elif option == "6":
            student_id = int(input("Enter student ID: "))
            generate_student_attendance_report(student_id)
        elif option == "7":
            teacher_id = int(input("Enter teacher ID: "))
            generate_teacher_attendance_report(teacher_id)
        elif option == "8":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid Option! Please enter a number from 1 to 8.")
