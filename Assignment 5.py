import psycopg2

conn = psycopg2.connect(
    database="stu", user="postgres", password="Li@200386", host="localhost", port="5432"
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
student_number = input("Enter student number: ")
read_student_info(student_number)

# Task 2, part b: 
def insert_student(): 
    student_number = input("Enter student number: ")
    cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
    existing_student = cur.fetchone()
    if existing_student: 
        print("The student number you entered already exists. ")
        return
    name = input("Enter student sname: ")
    age = input("Enter student age: ")
    gender = input("Enter student gender: ")
    department = input("Enter student sdept: ")
    cur.execute("INSERT INTO student VALUES (%s, %s, %s, %s, %s)",
                (student_number, name, age, gender, department))
    conn.commit()
    print("Student added successfully. ")
insert_student()

# Task 2, part c: 
def update_student_info(student_number): 
    cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
    student_info = cur.fetchone()
    if not student_info: 
        print("Student not found. ")
        return
    print("Current Student Information: ")
    print(student_info)
    name = input("Enter new sname: ")
    age = input("Enter new age: ")
    gender = input("Enter new gender: ")
    department = input("Enter new sdept: ")
    cur.execute("UPDATE student SET sname = %s, sage = %s, sgender = %s, sdept = %s WHERE sno = %s",
                (name, age, gender, department, student_number))
    conn.commit()
    print("Student information updated successfully. ")
student_number = input("Enter student number to update: ")
update_student_info(student_number)

# Task 2, part d: 
def delete_student(student_number): 
    cur.execute("SELECT * FROM student WHERE sno = %s", (student_number,))
    student_info = cur.fetchone()
    if not student_info: 
        print("Student not found. ")
        return
    cur.execute("SELECT * FROM sc WHERE sno = %s", (student_number,))
    enrolled_courses = cur.fetchall()
    if enrolled_courses: 
        cur.execute("DELETE FROM sc WHERE sno = %s", (student_number,))
        print("Enrollment records deleted. ")
    cur.execute("DELETE FROM student WHERE sno = %s", (student_number,))
    conn.commit()
    print("Student information deleted successfully. ")
student_number = input("Enter student number to delete: ")
delete_student(student_number)