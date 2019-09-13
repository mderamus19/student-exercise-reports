CREATE TABLE Cohort (
Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
Name TEXT NOT NULL UNIQUE 
);
CREATE TABLE student (
	student_Id INTEGER NOT NULL primary key autoincrement,
	first_name Text not null,
	last_name Text not null,
	slack_handle text not null unique,
	student_cohort_Id integer not null,
	Foreign Key (student_cohort_Id)
		references cohort (Id)
);
Create table instructor (
	instructor_Id integer primary key autoincrement,
	first_name text not null,
	last_name text not null,
	slack_handle text not null unique,
	specialty text not null,
	instructor_cohort_Id integer not null unique,
	foreign key (instructor_cohort_Id)
		references cohort (Id)
);
create table exercise (
	exercise_Id integer primary key autoincrement,
	exercise_name text not null,
	exercise_language text not null
);
Create table student_exercise (
	exercise_Id integer,
	student_Id integer, 
	student_exercise_Id integer not null primary key autoincrement,
	Foreign Key (exercise_Id)
		references student (student_Id),
	Foreign Key (student_Id)
		references exercise (exercise_Id)
);
insert into Cohort (Id, [Name])
values (null, "Day Cohort 26");
insert into Cohort (Id, [Name])
values (null, "Day Cohort 33");
insert into Cohort (Id, [Name])
values (null, "Evening Cohort 9");
insert into Cohort (Id, [Name])
values (null, "Day Cohort 35");
insert into Cohort (Id, [Name])
values (null, "Day Cohort 32");
delete from Cohort 
Where name = "Day Cohort 33";
delete from Cohort
Where name = "Day Cohort 35";
delete from Cohort
Where name = "Evening Cohort 9";
insert into exercise (exercise_Id,exercise_name, exercise_language)
values (null, "Journal","Javascript");
insert into exercise (exercise_Id, exercise_name, exercise_language)
values (null, "Tuple", "Python");
insert into exercise (exercise_Id,exercise_name, exercise_language)
values (null, "Classes", "Python");
insert into exercise (exercise_Id, exercise_name, exercise_language)
values (null, "Queries", "SQL");
insert into exercise (exercise_Id, exercise_name, exercise_language)
values (null, "Legos", "Javascript");
insert into instructor (instructor_Id, first_name, last_name, slack_handle,specialty, instructor_cohort_Id)
values (null, "Joe", "Shepherd","@joes", "dad jokes", 1);
insert into instructor (instructor_Id, first_name, last_name, slack_handle,specialty, instructor_cohort_Id)
values (null, "Steve", "Brownlee","@coach", "everything", 2);
insert into instructor (instructor_Id, first_name, last_name, slack_handle,specialty, instructor_cohort_Id)
values (null, "Jisie", "David","@jisie", "C#", 6);
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Misty", "DeRamus", "@mistyderamus", "1");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Jeff", "Hill", "@jeffH", "2");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Karla", "Gallegos", "@kgallegos", "1");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Danny", "Barker", "@danny", "6");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Caroline", "Brownlee", "@caroline", "2");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Ben", "Parker", "@benparker", "6");
insert into student (student_Id, first_name, last_name, slack_handle, student_cohort_Id)
values (null, "Sydney", "Noh", "@sydney", "1");
insert into student_exercise (exercise_Id, student_Id, student_exercise_Id)
values (5,7,null);
insert into student_exercise (exercise_Id, student_Id, student_exercise_Id)
values (2,3,null);