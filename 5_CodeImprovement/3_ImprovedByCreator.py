# Your updated Employee management system code looks much better. You've incorporated several improvements and best
# practices, including using an abstract base class (`Employee`), custom exceptions, and an enum for roles. Here's a
# summary of the changes:
#
# 1. You've defined an `ABC` (Abstract Base Class) for `Employee` with an abstract `pay` method, enforcing subclasses
# to implement it.
#
# 2. You've created a custom exception `VacationDaysShortageError` for handling vacation day shortages,
# providing informative error messages.
#
# 3. Roles are now defined as an `Enum`, which improves code readability and maintainability.
#
# 4. The `take_a_holiday` and `payout_a_holiday` methods now raise exceptions when necessary, providing clear error
# messages.
#
# 5. You've incorporated the `pay` method in each employee subclass to calculate and print the payment details.
#
# 6. The `Company` class now includes a `find_employees` method that allows you to find employees by their role.
#
# Overall, this code is well-structured, more maintainable, and follows good coding practices. Well done!


"""
Very advanced Employee management system.
"""

from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import Enum, auto
from typing import List

FIXED_VACATION_DAYS_PAYOUT = 5  # The fixed nr of vacation days that can be paid out.


class VacationDaysShortageError(Exception):
    """Custom error that is raised when not enough vacation days are available."""

    def __init__(self, requested_days: int, remaining_days: int, message: str) -> None:
        self.requested_days = requested_days
        self.remaining_days = remaining_days
        self.message = message
        super().__init__(message)


class Role(Enum):
    """Employee roles"""

    PRESIDENT = auto()
    VICEPRESIDENT = auto()
    MANAGER = auto()
    LEAD = auto()
    WORKER = auto()
    INTERN = auto()


@dataclass
class Employee(ABC):
    """Basic representation of an employee at the company."""

    name: str
    role: Role
    vacation_days: int = 25

    @abstractmethod
    def pay(self) -> None:
        """Method to call when paying an employee"""

    def take_a_holiday(self) -> None:
        """Let the employee take a holiday (lazy bastard)"""
        if self.vacation_days < 1:
            raise VacationDaysShortageError(
                requested_days=1,
                remaining_days=self.vacation_days,
                message="You don't have any holidays left. Now back to work, you!",
            )
        self.vacation_days -= 1
        print("Have fun on your holiday. Don't forget to check your emails!")

    def payout_a_holiday(self) -> None:
        """Let the employee get paid for unused holidays."""
        # check that there are enough vacation days left for a payout
        if self.vacation_days < FIXED_VACATION_DAYS_PAYOUT:
            raise VacationDaysShortageError(
                requested_days=FIXED_VACATION_DAYS_PAYOUT,
                remaining_days=self.vacation_days,
                message="You don't have enough holidays left over for a payout",
            )
        self.vacation_days -= FIXED_VACATION_DAYS_PAYOUT
        print(f"Paying out a holiday. Holidays left: {self.vacation_days}")


@dataclass
class HourlyEmployee(Employee):
    """Employee that's paid based on number of worked hours."""

    hourly_rate: float = 50
    hours_worked: int = 10

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a hourly rate of \
            ${self.hourly_rate} for {self.hours_worked} hours."
        )


@dataclass
class SalariedEmployee(Employee):
    """Employee that's paid based on a fixed monthly salary."""

    monthly_salary: float = 5000

    def pay(self) -> None:
        print(
            f"Paying employee {self.name} a monthly salary of ${self.monthly_salary}."
        )


class Company:
    """Represents a company with employees."""

    def __init__(self) -> None:
        self.employees: List[Employee] = []

    def add_employee(self, employee: Employee) -> None:
        """Add an employee to the list of employees."""
        self.employees.append(employee)

    def find_employees(self, role: Role) -> List[Employee]:
        """Find all employees with a particular role in the employee list"""
        return [employee for employee in self.employees if employee.role is role]


def main() -> None:
    """Main function."""

    company = Company()

    company.add_employee(SalariedEmployee(name="Louis", role=Role.MANAGER))
    company.add_employee(HourlyEmployee(name="Brenda", role=Role.PRESIDENT))
    company.add_employee(HourlyEmployee(name="Tim", role=Role.INTERN))

    print(company.find_employees(role=Role.VICEPRESIDENT))
    print(company.find_employees(role=Role.MANAGER))
    print(company.find_employees(role=Role.INTERN))
    company.employees[0].pay()
    company.employees[0].take_a_holiday()


if __name__ == "__main__":
    main()
