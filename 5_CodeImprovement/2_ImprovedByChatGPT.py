# Makertalk 20231013
# 7 Python Code Smells
# https://www.youtube.com/watch?v=LrtnLEkOwFE&list=PLC0nd42SBTaNuP4iB4L6SJlMaHE71FG6N&index=24
# https://github.com/ArjanCodes/2021-code-smells/blob/main/before.py

# Findings ChatGPT
# Improvements made:
#
#     Removed unnecessary try-except blocks.
#     Improved code readability by simplifying and reorganizing the code.
#     Used list comprehensions for finding employees by role.
#     Renamed some methods and variables for better clarity.
#     Added type hints for function arguments and return values.
#     Modified the way holidays are paid out to be more informative.
#     Added the calculate_payment method for HourlyEmployee to calculate payment based on hourly rate and hours worked.
#
# This code should be more maintainable and easier to understand.

from dataclasses import dataclass
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5

@dataclass
class Employee:
    name: str
    role: str
    vacation_days: int = 25

    def take_a_holiday(self, payout: bool = False) -> None:
        if payout:
            if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
                raise ValueError(f"You don't have enough holidays left for a payout. Remaining holidays: {self.vacation_days}.")
            self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
            print(f"Paying out {FIXED_VACATION_DAYS_PAYOUT} holidays. Holidays left: {self.vacation_days}")
        else:
            if self.vacation_days < 1:
                raise ValueError("You don't have any holidays left. Now back to work, you!")
            self.vacation_days -= 1
            print(f"Have fun on your holiday, {self.name}. Don't forget to check your emails!")

@dataclass
class HourlyEmployee(Employee):
    hourly_rate: float = 50
    hours_worked: int = 10

    def calculate_payment(self) -> float:
        return self.hourly_rate * self.hours_worked

@dataclass
class SalariedEmployee(Employee):
    monthly_salary: float = 5000

class Company:
    def __init__(self):
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        self.employees.append(employee)

    def find_employees_by_role(self, target_role: str) -> List[Employee]:
        return [employee for employee in self.employees if employee.role == target_role]

    def pay_employee(self, employee: Employee) -> None:
        if isinstance(employee, SalariedEmployee):
            print(f"Paying {employee.name} a monthly salary of ${employee.monthly_salary}.")
        elif isinstance(employee, HourlyEmployee):
            payment = employee.calculate_payment()
            print(f"Paying {employee.name} ${payment} for {employee.hours_worked} hours.")

def main() -> None:
    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role="manager"))
    company.add_employee(HourlyEmployee(name="Brenda", role="president"))
    company.add_employee(HourlyEmployee(name="Tim", role="intern"))

    print("Managers:")
    for manager in company.find_employees_by_role("manager"):
        print(manager.name)

    print("Presidents:")
    for president in company.find_employees_by_role("president"):
        print(president.name)

    print("Interns:")
    for intern in company.find_employees_by_role("intern"):
        print(intern.name)

    company.pay_employee(company.employees[0])
    company.employees[0].take_a_holiday(False)

if __name__ == "__main__":
    main()
