
from tabulate import tabulate

from rich.console import Console
from rich.table import Table

from employee_system.employee import get_all_employees


def show_tabulate(employees):

    print("EMPLOYEE TABLE - TABULATE")
    print("=========================")

    table = tabulate(
        employees,
        headers="keys",
        tablefmt="grid"
    )

    print(table)


def show_rich(employees):

    print()
    print("EMPLOYEE TABLE - RICH")
    print("=====================")

    table = Table(title="Employee Details")

    table.add_column("ID")
    table.add_column("Name")
    table.add_column("Department")
    table.add_column("Salary")

    for employee in employees:

        table.add_row(
            employee["id"],
            employee["name"],
            employee["department"],
            str(employee["salary"])
        )

    console = Console()

    console.print(table)


def main():

    employees = get_all_employees()

    show_tabulate(employees)

    show_rich(employees)


main()
