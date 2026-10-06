# : Student Performance System :

A menu-driven, console-based student record management and analysis application built in pure Python using **nested dictionaries**, **modular functions**, and **structured control flow**. No classes, no external libraries.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Dependencies](https://img.shields.io/badge/Dependencies-None-brightgreen)
![Paradigm](https://img.shields.io/badge/Paradigm-Procedural-orange)
![Interface](https://img.shields.io/badge/Interface-CLI-lightgrey)

---

## Function Reference Card

| # | Function | Category | Parameters | Returns | Purpose |
|---|----------|----------|------------|---------|---------|
| 1 | `calculate_total(student)` | Calculation | `student` (dict) | `int` | Sum of Python, Java and SQL marks |
| 2 | `calculate_average(student)` | Calculation | `student` (dict) | `float` | Total divided by 3 subjects |
| 3 | `calculate_grade(average)` | Calculation | `average` (float) | `str` | Maps an average to A+, A, B, C or F |
| 4 | `display_students(students)` | Read | `students` (dict) | `None` | Prints every student record |
| 5 | `search_student(students, student_id)` | Read | `students`, `student_id` | `None` | Looks up one student by ID |
| 6 | `display_report(students, student_id)` | Read / Analysis | `students`, `student_id` | `None` | Prints total, average and grade for one student |
| 7 | `add_student(students)` | Create | `students` (dict) | `None` | Reads input and inserts a new record |
| 8 | `update_marks(students, student_id)` | Update | `students`, `student_id` | `None` | Changes a student's Python marks |
| 9 | `delete_student(students)` | Delete | `students` (dict) | `None` | Removes a record by ID |
| 10 | `find_topper(students)` | Analysis | `students` (dict) | `None` | Finds the student with the highest total |
| 11 | `menu()` | UI | none | `None` | Prints the main menu options |

---

## Table of Contents

- [Overview](#overview)
- [Key Features](#key-features)
- [Concepts Demonstrated](#concepts-demonstrated)
- [Project Structure](#project-structure)
- [Data Model](#data-model)
- [Getting Started](#getting-started)
- [Application Flow](#application-flow)
- [Detailed Function Documentation](#detailed-function-documentation)
- [Grading Scale](#grading-scale)
- [Sample Output](#sample-output)
- [Input Validation and Error Handling](#input-validation-and-error-handling)
- [Design Decisions](#design-decisions)
- [Known Limitations](#known-limitations)
- [Future Improvements](#future-improvements)
- [Lab Challenges](#lab-challenges)

---

## Overview

The Student Performance System manages academic records for a class. Each student has an ID, a name, and marks in three subjects: Python, Java and SQL. From these marks the program calculates totals, averages and letter grades, and identifies the class topper.

The project is based on the Python Dictionary Lab Exercise (Student Performance Analyzer) and extends the reference solution with input validation, duplicate ID protection, empty-data handling and a modern `match-case` dispatcher.

---

## Key Features

- Display all student records
- Search a student by ID
- Generate an individual report with total, average and grade
- Add new students with duplicate ID protection
- Update a student's marks
- Delete a student record
- Identify the class topper by highest total marks
- Graceful handling of invalid menu choices and non-numeric input
- Continuous menu loop that runs until the user exits

---

## Concepts Demonstrated

- Dictionaries and nested dictionaries (student ID mapped to a record dictionary)
- Dictionary methods: `items()`, key lookup with `[]`, `del`, assignment-based insertion
- Membership testing with the `in` operator
- Function decomposition with parameters and return values
- Conditional logic with `if`, `elif`, `else`
- Loops: `for` for traversal, `while True` for the application loop
- Structural pattern matching (`match-case`)
- Exception handling with `try / except ValueError`
- Higher-order function usage: `max()` with a `key` function and `lambda`
- CRUD operations (Create, Read, Update, Delete)

---

## Project Structure

```
Student-Performance-System/
|
|-- Project_Student.py        # Complete application source
|-- README.md                 # Project documentation
|-- images/                   # Output screenshots used in this README
    |-- 01-add-student.png
    |-- 02-display-students.png
    |-- 03-display-and-invalid-choice.png
    |-- 04-search-and-report.png
    |-- 05-topper-and-exit.png
```

---

## Data Model

Records are stored in a dictionary of dictionaries. The outer key is the unique student ID, and the value is a dictionary of that student's details.

```python
students = {
    101: {"name": "Tandrima", "python": 85, "java": 78, "sql": 90},
    102: {"name": "Prity",    "python": 92, "java": 88, "sql": 95},
    103: {"name": "Drubo",    "python": 70, "java": 75, "sql": 68},
}
```

- Outer dictionary: `student_id (int)` to `record (dict)`
- Inner dictionary: `name (str)`, `python (int)`, `java (int)`, `sql (int)`
- Why this structure: dictionary lookup by key is O(1) on average, so searching, updating and deleting by ID does not require scanning a list.

---

## Getting Started

### Prerequisites

- Python 3.10 or higher (required for `match-case`)
- No third-party packages

Check your version:

```bash
python --version
```

### Run the Application

```bash
git clone https://github.com/<your-username>/<your-repository>.git
cd <your-repository>
python Project_Student.py
```

### Menu Options

| Choice | Action |
|--------|--------|
| 1 | Display Students |
| 2 | Search Student |
| 3 | Student Report |
| 4 | Add Student |
| 5 | Update Marks |
| 6 | Delete Student |
| 7 | Find Topper |
| 8 | Exit |

---

## Application Flow

```
Start
  |
  v
Load in-memory students dictionary
  |
  v
+--> menu() prints options
|      |
|      v
|    Read choice (int)  --- ValueError --> "Please enter numbers only"
|      |
|      v
|    match choice
|      |-- 1 -> display_students
|      |-- 2 -> search_student
|      |-- 3 -> display_report
|      |-- 4 -> add_student
|      |-- 5 -> update_marks
|      |-- 6 -> delete_student
|      |-- 7 -> find_topper
|      |-- 8 -> print "Thank you!" and break
|      |-- _ -> "Invalid choice"
|      |
+------+  (loop repeats until option 8)
```

The main loop contains no business logic. It only reads the choice and routes it to the correct function, which keeps each feature independent and testable.

---

## Detailed Function Documentation

### Calculation Functions

#### `calculate_total(student)`

- Input: a single student record dictionary
- Output: integer sum of `python`, `java` and `sql`
- Why it exists: the total is needed by the report, the average and the topper search. Writing it once avoids repeating the same addition in three places (DRY principle).
- Example: Tandrima's record returns `85 + 78 + 90 = 253`

#### `calculate_average(student)`

- Input: a single student record dictionary
- Output: float, total divided by 3
- Why it exists: separates the averaging rule from the display code. It reuses `calculate_total`, so a change to how totals work automatically flows through.
- Example: Drubo's record returns `213 / 3 = 71.0`

#### `calculate_grade(average)`

- Input: a numeric average (not a student dictionary)
- Output: one of `"A+"`, `"A"`, `"B"`, `"C"`, `"F"`
- Why it takes an average instead of a student: it only needs a number, so it can be reused anywhere a grade must be derived from any average value
- Why `if / elif / else`: the thresholds are ordered ranges. The first matching condition wins, so checking from highest to lowest keeps the logic short and unambiguous.

### Read and Display Functions

#### `display_students(students)`

- Iterates over `students.items()` to unpack each ID and record together
- Prints ID, name and all three subject marks
- Guards against an empty dictionary with `if not students` and prints "No students available" instead of silently showing nothing
- Why `items()`: it gives key and value in one pass, which is cleaner and faster than looking up each key separately

#### `search_student(students, student_id)`

- Uses the `in` operator to test whether the ID exists as a key
- Prints "Student Found" with the name, or "Student not found"
- Why check first: accessing a missing key with `students[student_id]` would raise a `KeyError`. Testing membership first avoids that crash.

#### `display_report(students, student_id)`

- Validates the ID, then builds a complete report by calling `calculate_total`, `calculate_average` and `calculate_grade`
- Prints the average rounded to two decimal places with `round(average, 2)`
- Uses an early `return` when the ID is missing, so the rest of the function does not run on invalid data (guard clause pattern)
- Why it is separate from `search_student`: search confirms existence, while the report performs analysis. Each function has one job.

### Create, Update and Delete Functions

#### `add_student(students)`

- Prompts for ID, name and the three marks, then inserts a new nested dictionary
- Rejects an ID that already exists, printing "ID already exists", so existing records are never silently overwritten
- The dictionary is only modified after all inputs have been read successfully. If the user types invalid text partway through, a `ValueError` is raised before any write happens, so no half-created record is left behind.
- Why `students` is passed in: dictionaries are mutable, so the function updates the original object without needing a `return`

#### `update_marks(students, student_id)`

- Confirms the student exists, then replaces the stored Python marks with the new value
- Why it receives `student_id` as an argument: the main loop collects the ID so the function stays focused on the update itself
- Current scope: updates the Python subject only (see Future Improvements)

#### `delete_student(students)`

- Prompts for an ID and removes the record with the `del` statement
- Checks membership first and reports "Student not found" if the ID is absent
- Why `del`: it removes the key and its value in one step, with no leftover placeholder entries

### Analysis Function

#### `find_topper(students)`

- Returns early with a message if the dictionary is empty
- Uses `max(students, key=lambda sid: calculate_total(students[sid]))` to select the ID with the greatest total
- Prints the topper's ID, name and total
- Why `max()` with `key`: it expresses "find the largest by this rule" in one line. The common alternative, starting a `highest_total = 0` variable and looping, fails on an empty dictionary because `students[None]` raises an error. The `max()` version plus the empty check avoids that bug.
- Complexity: O(n), one pass over all students

### Interface Function

#### `menu()`

- Prints the numbered options
- Why it is its own function: the menu text is separated from the loop logic, so the layout can be changed without touching program flow

### Main Program Loop

- `while True` keeps the program running until the user selects option 8
- `match choice` dispatches to the right function. It reads more clearly than a long `if / elif` chain, and `case _` serves as the default branch for invalid options.
- `try / except ValueError` wraps the whole block so non-numeric input never crashes the program
- `break` on option 8 exits the loop cleanly with "Thank you!"

---

## Grading Scale

| Average | Grade |
|---------|-------|
| 90 and above | A+ |
| 80 to below 90 | A |
| 70 to below 80 | B |
| 60 to below 70 | C |
| Below 60 | F |

### Pre-loaded Data Results

| ID | Name | Python | Java | SQL | Total | Average | Grade |
|----|------|--------|------|-----|-------|---------|-------|
| 101 | Tandrima | 85 | 78 | 90 | 253 | 84.33 | A |
| 102 | Prity | 92 | 88 | 95 | 275 | 91.67 | A+ |
| 103 | Drubo | 70 | 75 | 68 | 213 | 71.00 | B |

Class topper: **Prity (ID 102)** with a total of 275.

---

## Sample Output

### 1. Adding a Student

Option 4 collects the ID, name and three marks, then confirms the insertion. The menu reappears and option 1 begins listing records.

[Add student]<img width="1633" height="1080" alt="1st" src="https://github.com/user-attachments/assets/e5f3d09f-a0d7-4e8f-97bd-d3fb90e0c5ce" />


### 2. Displaying All Students

Option 1 prints every record, including the newly added student (ID 1020).

[Display students]<img width="1613" height="1080" alt="2nd" src="https://github.com/user-attachments/assets/ba24c904-92a6-4dbf-8d6c-9b9b6e7788eb" />


### 3. Invalid Menu Choice

Entering `9` is not a valid option, so the `case _` branch prints "Invalid choice" and the menu is shown again.

[Display and invalid choice]<img width="1627" height="978" alt="4th" src="https://github.com/user-attachments/assets/06d2ea0f-258e-4193-afe0-a2d313b5ddb8" />


### 4. Searching and Generating a Report

Option 2 finds student 101 by ID. Option 3 produces the report for student 103, showing the total, average and grade.

[Search and report]<img width="1634" height="988" alt="5th" src="https://github.com/user-attachments/assets/db5c7306-23fd-4d98-a3e4-3554d6742703" />


### 5. Finding the Topper and Exiting

Option 7 identifies Prity (ID 102) with a total of 275. Option 8 prints "Thank you!" and ends the program.

[Topper and exit]<img width="1625" height="974" alt="7th" src="https://github.com/user-attachments/assets/66dccc23-dfe6-4396-86dc-ddf45fa784ab" />


---

## Input Validation and Error Handling

| Situation | How it is handled |
|-----------|-------------------|
| Non-numeric menu choice or ID | `ValueError` is caught and "Please enter numbers only" is printed |
| Menu number outside 1 to 8 | `case _` prints "Invalid choice" |
| Student ID not found | Membership check prints "Student not found" instead of raising `KeyError` |
| Duplicate ID on add | Rejected with "ID already exists" |
| Empty student dictionary | `display_students` and `find_topper` print "No students available" |
| Invalid marks input mid-way through adding | Exception occurs before the dictionary is modified, so no partial record is saved |

---

## Design Decisions

- **Nested dictionaries over lists:** direct key-based access makes lookup, update and delete fast and readable.
- **Small single-purpose functions:** each function does one thing, which makes the code easier to read, debug and extend.
- **Pass the dictionary as an argument:** avoids relying on global state and makes functions easier to test.
- **Calculation separated from display:** `calculate_*` functions return values and never print, so they can be reused by any future feature.
- **Guard clauses:** checking the failure case first and returning early keeps the main logic unindented and clear.
- **Procedural style:** following the lab requirements, no classes or OOP are used.

---

## Known Limitations

- Data is stored in memory only, so all additions, updates and deletions are lost when the program exits
- `update_marks` modifies Python marks only
- Marks are not validated against a range such as 0 to 100
- Names are not validated for empty input
- The student report shows total, average and grade but not the individual subject marks
- If two students tie for the highest total, only the first one found is reported as topper

---

## Future Improvements

- Persist data to a JSON or CSV file so records survive between runs
- Let the user choose which subject to update
- Validate that marks fall between 0 and 100
- Add a ranked leaderboard sorted by total marks
- Add class-level statistics such as subject-wise averages and grade distribution
- Report all students in the case of a tied topper
- Add unit tests for the calculation functions
- Replace the console interface with a Streamlit dashboard

---

## Lab Challenges

These extension exercises come from the original lab and can be built on top of this project:

- Find the student with the highest Python marks
- Find all students whose average is above 80
- Find the lowest-scoring student
- Count how many students received each grade
- Find the subject with the highest class average

---

## Requirements

- Python 3.10+
- Tested on CPython 3.14.7 (64-bit), Windows, run through Visual Studio Code terminal
