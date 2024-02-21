import psycopg2

conn = psycopg2.connect(
    database="student", user="postgres", password="Li@200386", host="localhost", port="5432"
)
cur = conn.cursor()

# Task 2, part a: 
def read_student_info(student_number): 
    cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
    student_info = cur.fetchone()
    if student_info: 
        print("Student Information: ")
        print(student_info)
    else: 
        print("Student not found. ")

# Task 2, part b: 
def insert_student(): 
    while True:
        student_number = input("Enter student number to insert: ")
        cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
        existing_student = cur.fetchone()
        if existing_student: 
            print("The student number you entered already exists. Please enter a different student number.")
        else: 
            name = input("Enter the student's name: \n")
            age = int(input("Enter the student's age: \n"))
            gender = input("Enter the student's gender (M/F): \n")
            department = input("Enter the student's department name: \n")
            cur.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s)",
            (student_number, name, age, gender, department))
            conn.commit()
            print("Student added successfully. ")
            break

# Task 2, part c: 
def update_student_info(student_number): 
    cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
    student_info = cur.fetchall()
    if student_info:
        print("Current student information: ")
        for row in student_info:
            print(row)
    else:
        print("The student number you entered is not available. \n")
        return
    name = input("Enter new name: ")
    age = input("Enter new age: ")
    gender = input("Enter new gender: ")
    department = input("Enter new dept: ")
    cur.execute("UPDATE student SET sname = %s, sage = %s, sgender = %s, sdept = %s WHERE sno = %s",
                (name, age, gender, department, student_number))
    conn.commit()
    print("Student information updated successfully. ")

# Task 2, part d: 
def delete_student(student_number): 
    cur.execute("SELECT * FROM sc WHERE sno = %s", (student_number,))
    enrolled_courses = cur.fetchall()
    if enrolled_courses: 
        cur.execute("DELETE FROM sc WHERE sno = %s", (student_number,))
        print("Enrollment records deleted. ")
    cur.execute("DELETE FROM student WHERE sno = %s", (student_number,))
    conn.commit()
    print("Student information deleted successfully. ")

while True:
    print("\nSelect an option: ")
    print("1. Read student information")
    print("2. Insert new student")
    print("3. Update student information")
    print("4. Delete student")
    print("5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1': 
        student_number = input("Enter student number: ")
        read_student_info(student_number)
    elif choice == '2': 
        insert_student()
    elif choice == '3': 
        student_number = input("Enter student number to update: ")
        update_student_info(student_number)
    elif choice == '4': 
        student_number = input("Enter student number to delete: ")
        delete_student(student_number)
    elif choice == '5': 
        break
    else:
        print("Invalid choice. Please try again. ")

cur.close()
conn.close()