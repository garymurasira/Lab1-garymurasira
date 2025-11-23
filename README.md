Grade Calculator & Organizer

Overview
There are two parts in this project:
Grade Calculator (Python)  
   - Gathers data on assignments (Formative and Summative).  
   - Validates user input.  
   - Compute weighted totals, GPA (scale of 5.0) and pass/fail.  
   - Recommends re-submission in case of failed assignments.  
   - Exports results to grades.csv.

Organizer (Bash)  
   - Divide Archives CSV files by renaming them with a time.  
   - Pushes them to an archive folder.  
   - Records everything that was done and the contents of the files in organizer.log.

Features
Name of assignment, category, grade and weight input validation.
Pass / Fail Logic: This is based on categories.
  - Should attain [?]50% of weight in both FA and SA.
  - No FA or SA assignments - automatic fail.
GPA calculation on a 5.0 scale.
Resubmission list of assignments below 50 grades.
CSV export with assignment information.
Archiving and logging of CSV files Bash script.

How to Run

Grade Calculator (Python)
Make sure you have the Python 3.
Run the program:
   ```bash
   python grade_calculator.py

Organizer (Bash)- Ensure you have Bash available (Linux/macOS or Git Bash on Windows).
- Run the script:
./organizer.sh
- All .csv files in the current directory will be archived with timestamps.
- Check organizer.log for details of actions and file contents.

Project Structure├── grade_calculator.py   # Python program for GPA and pass/fail
├── organizer.sh          # Bash script for archiving CSVs
├── grades.csv            # Output file (overwritten each run)
├── archive/              # Directory where timestamped CSVs are stored
└── organizer.log         # Log file with archive actions and file contents
Example Output---RESULTS---
Total Formative: 44.10 / 60.0
Total Summative: 32.50 / 40.0
----------------
Total Grade: 76.60 / 100
GPA: 3.8300
Status: PASS
Resubmission: None
