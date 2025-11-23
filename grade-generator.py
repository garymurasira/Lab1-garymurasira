"""
Grade Calculator Program
------------------------
This script lets a user enter assignments (Formative or Summative),
records grades and weights, calculates GPA, and decides pass/fail status.
It also prints a summary and saves results to a CSV file.

Inputs: assignment name, category (FA/SA), grade (0-100), weight (>0)
Outputs: GPA (5.0 scale), pass/fail status, resubmission list, CSV export
"""

import csv   # need this for saving results later


class Assignment:
    """
    Represents a single assignment with name, category, grade, and weight.
    Category is normalized to uppercase (FA/SA).
    """
    def __init__(self, name, category, grade, weight):
        # basic info for each assignment
        self.name = name
        self.category = category.upper()   # force FA/SA uppercase
        self.grade = float(grade)          # keep numeric
        self.weight = float(weight)

    def weighted_score(self):
        """Return grade scaled by assignment weight."""
        # quick calc: grade scaled by weight
        return (self.grade / 100) * self.weight


class GradeCalculator:
    """
    Collects assignments, validates input, computes GPA and pass/fail,
    and handles reporting/export.
    """
    def __init__(self):
        self.assignments = []

    def collect_input(self):
        """Loop until user stops adding assignments."""
        # keep asking until user says stop
        while True:
            name = self.get_valid_name()
            category = self.get_valid_category()
            grade = self.get_valid_grade()
            weight = self.get_valid_weight()

            # add assignment in the list
            self.assignments.append(Assignment(name, category, grade, weight))

            cont = input("Add another assignment? (y/n): ").lower()
            if cont != 'y':   # anything other than 'y' ends loop
                break

    def get_valid_name(self):
        """Prompt until a non-empty name is entered."""
        while True:
            name = input("Assignment Name: ").strip()
            if name:   # non-empty string check
                return name
            print("Assignment name cannot be empty.")

    def get_valid_category(self):
        """Prompt until category is FA or SA."""
        while True:
            category = input("Category (FA/SA): ").upper()
            if category in ["FA", "SA"]:
                return category
            print("Invalid category. Please enter FA or SA.")

    def get_valid_grade(self):
        """Prompt until grade is a number between 0 and 100."""
        while True:
            try:
                grade = float(input("Grade (0-100): "))
                if 0 <= grade <= 100:
                    return grade
                print("Grade must be between 0 and 100.")
            except ValueError:
                print("Please enter a valid number.")
            

    def get_valid_weight(self):
        """Prompt until weight is a positive number."""
        while True:
            try:
                weight = float(input("Weight (positive number): "))
                if weight > 0:
                    return weight
                print("Weight must be positive.")
            except ValueError:
                print("Please enter a valid number.")
            

    def calculate_results(self):
        """
        Compute totals, GPA, pass/fail status, and resubmission list.
        Pass rule: must achieve >=50% of weight in both FA and SA.
        """
        # initializing totals (FA = formative, SA = summative)
        total_fa = total_sa = fa_weight = sa_weight = 0

        for a in self.assignments:
            weighted = a.weighted_score()
            if a.category == "FA":
                total_fa += weighted
                fa_weight += a.weight
            else:
                total_sa += weighted
                sa_weight += a.weight

        total_grade = total_fa + total_sa
        gpa = (total_grade / 100) * 5.0   # convert to 5.0 GPA scale

        
        fa_pass = total_fa >= (fa_weight * 0.5) if fa_weight > 0 else False
        sa_pass = total_sa >= (sa_weight * 0.5) if sa_weight > 0 else False

        status = "PASS" if fa_pass and sa_pass else "FAIL"

        # collect names of failed assignments
        failed_assignments = [a.name for a in self.assignments if a.grade < 50]
        resubmission = ", ".join(failed_assignments) if failed_assignments else "None"

        # return everything in a dict (easy to print/export)
        return {
            "total_fa": total_fa,
            "fa_weight": fa_weight,
            "total_sa": total_sa,
            "sa_weight": sa_weight,
            "total_grade": total_grade,
            "gpa": gpa,
            "status": status,
            "resubmission": resubmission
        }

    def print_summary(self, results):
        """Print results in a readable format."""
        # quick report to console
        print("\n---RESULTS---")
        print(f"Total Formative: {results['total_fa']:.2f} / {results['fa_weight']}")
        print(f"Total Summative: {results['total_sa']:.2f} / {results['sa_weight']}")
        print("----------------")
        print(f"Total Grade: {results['total_grade']:.2f} / 100")
        print(f"GPA: {results['gpa']:.4f}")
        print(f"Status: {results['status']}")
        print(f"Resubmission: {results['resubmission']}")

    def export_to_csv(self):
        """Save assignments to grades.csv (overwrite each run)."""
        # add assignments to CSV file (overwrite each run)
        print("\nExporting results to grades.csv...")

        try:
            with open("grades.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["Assignment", "Category", "Grade", "Weight"])
                for a in self.assignments:
                    writer.writerow([a.name, a.category, a.grade, a.weight])
            print("\nData saved to grades.csv")
        except Exception as e:
            print(f"Error saving file: {e}")

def main():
    """Main entry point: run calculator workflow."""
    print("Welcome to the Grade Generator Calculator\n")
    calculator = GradeCalculator()
    calculator.collect_input()
    results = calculator.calculate_results()
    calculator.print_summary(results)
    calculator.export_to_csv()
    # end of program → file saved, summary printed


if __name__ == "__main__":
    main()
