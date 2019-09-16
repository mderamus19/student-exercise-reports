import sqlite3

class Student():

    def __init__(self, first, last, handle, cohort):
        self.first_name = first
        self.last_name = last
        self.slack_handle = handle
        self.student_cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name} is in {self.student_cohort}'

class Cohort():

    def __init__(self, cohortName):
        self.Name = cohortName

    def __repr__(self):
        return f'{self.Name}'

class Exercise():

    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} {self.language}'

class Javascript():

    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} {self.language}'

class Python():

    def __init__(self, id, name, language):
        self.id = id
        self.name = name
        self.language = language

    def __repr__(self):
        return f'{self.name} {self.language}'

class Student_Cohort():

    def __init__(self, id, first_name, last_name, cohort):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name } {self.cohort}'

class Instructor_Cohort():

    def __init__(self, id, first_name, last_name, cohort):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.cohort = cohort

    def __repr__(self):
        return f'{self.first_name} {self.last_name } {self.cohort}'

class StudentExerciseReports():

    """Methods for reports on the Student Exercises database"""

    def __init__(self):
        self.db_path = "/Users/misty/workspace/python/StudentExercises/studentexercises.db"

    def all_students(self):

        """Retrieve all students with the cohort name"""

        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student(row[1], row[2], row[3], row[5])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            select student_Id,
                s.first_name,
                s.last_name,
                s.slack_handle,
                s.student_cohort_Id,
                c.Name
            from Student s
            join Cohort c on s.student_cohort_Id = c.Id
            order by s.student_cohort_Id
            """)

            all_students = db_cursor.fetchall()

            for student in all_students:
                print(student)

    def all_cohorts(self):
        '''Retrieve all cohorts'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Cohort(row[0])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT c.Name
            FROM Cohort c
                            """)
        all_cohorts = db_cursor.fetchall()
        for cohort in all_cohorts:
            print(cohort)

    def all_exercises(self):
        '''Retrieve all exercises'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Exercise(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise_Id,
            exercise_name,
            exercise_language
            FROM exercise
                            """)

            all_exercises = db_cursor.fetchall()
            for exercise in all_exercises:
                print(exercise)

    def all_js_exercises(self):
        '''Retrieve all javascript exercises'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Javascript(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise_Id,
            exercise_name,
            exercise_language
            FROM exercise
            WHERE exercise_language = "Javascript"
                            """)

            all_js_exercises = db_cursor.fetchall()
            for javascript in all_js_exercises:
                print(javascript)

    def all_py_exercises(self):
        '''Retrieve all python exercises'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Python(row[0], row[1], row[2])
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise_Id,
            exercise_name,
            exercise_language
            FROM exercise
            WHERE exercise_language = "Python"
                            """)

            all_py_exercises = db_cursor.fetchall()
            for python in all_py_exercises:
                print(python)

    def all_csharp_exercises(self):
        '''Retrieve all C# exercises'''
        with sqlite3.connect(self.db_path) as conn:
            db_cursor = conn.cursor()

            db_cursor.execute("""
            SELECT exercise_name,
            exercise_language
            FROM exercise
            WHERE exercise_language = "C#"
                            """)

# conditional to check the length of all csharp exercises
            all_csharp_exercises = db_cursor.fetchall()
            if len(all_csharp_exercises) == 0:
                print("There are no C# exercises!")
            else:
                for csharp in all_csharp_exercises:
                    print(csharp)

    def all_students_cohorts(self):
        '''Retrieve all students and cohort names'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Student_Cohort(row[0], row[1], row[2], row [3])
            db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT student_Id,
        first_name,
        last_name,
        c.Name
        FROM Cohort c
        JOIN student s
        ON c.Id = s.student_cohort_Id
                          """)

        all_students_cohorts = db_cursor.fetchall()
        for studentCohort in all_students_cohorts:
            print(studentCohort)

    def all_instructors_cohorts(self):
        '''Retrieve all instructors and cohort names'''
        with sqlite3.connect(self.db_path) as conn:
            conn.row_factory = lambda cursor, row: Instructor_Cohort(row [0],row[1], row[2], row[3])
            db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT instructor_Id,
        first_name,
        last_name,
        c.Name
        FROM Cohort c
        JOIN instructor i
        ON c.Id = i.instructor_cohort_Id
                          """)

        all_instructors_cohorts = db_cursor.fetchall()
        for instructorCohort in all_instructors_cohorts:
            print(instructorCohort)

reports = StudentExerciseReports()
reports.all_students()
reports.all_cohorts()
reports.all_exercises()
reports.all_js_exercises()
reports.all_py_exercises()
reports.all_csharp_exercises()
reports.all_students_cohorts()
reports.all_instructors_cohorts()
