# Student Management System

A simple **Student Management System** built with **Python**.
This project allows users to manage student information directly from the terminal.

## Features

* Search for a student
* Add a new student
* Remove a student
* Update student information
* Show all students
* Automatically save student data in a JSON file
* Load existing data when the program starts
* Simple command-line interface

## Technologies Used

* **Python**
* **JSON**
* **OS module**

The project uses `students_data.json` to store student information and loads the data when needed.

## Project Structure

```text
Student-Management-System/
│
├── main.py
├── work.py
├── students_data.json
└── README.md
```

### `main.py`

This file contains the main menu and controls the overall program flow. It provides five options:

1. Search student
2. Add student
3. Remove student
4. Update student
5. Show all students

### `work.py`

This file contains the main student-management operations, including searching, adding, removing, updating, and displaying students.

### `students_data.json`

This file stores the student information in JSON format, including names, ID numbers, class, and age.

## How to Run

### 1. Clone the repository

```bash
git clone YOUR_REPOSITORY_URL
```

### 2. Open the project folder

```bash
cd Student-Management-System
```

### 3. Run the program

```bash
python main.py
```

## Example Menu

```text
===================================
||   STUDENT MANAGEMENT SYSTEM   ||
===================================

Choose what do you want:

  1. Search student
  2. Add student
  3. Remove student
  4. Update student
  5. Show all
```

## Data Storage

Student information is stored in `students_data.json`.
The program loads existing data and saves changes back to the JSON file.

## Purpose

This project was created to practice:

* Python functions
* Dictionaries
* Lists
* JSON file handling
* File handling
* Conditional statements
* Loops
* Modular programming
* Basic CRUD operations

## Future Improvements

Possible future features:

* Login system
* Better search options
* Student result management
* Attendance management
* GUI version
* Database support
* Export student data

## Author

**Nur Hamza**

---

⭐ If you find this project useful, consider giving the repository a **star**!
