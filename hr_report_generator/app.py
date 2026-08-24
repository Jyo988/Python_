
from jinja2 import Environment, FileSystemLoader
from prettytable import PrettyTable

from employee_system.employee import get_all_employees


def create_report(employee):

    environment = Environment(
        loader=FileSystemLoader("templates")
    )

    template = environment.get_template("employee_report.txt")

    report = template.render(employee=employee)

    return report


def create_table(employees):

    table = PrettyTable()

    table.field_names = [
        "ID",
        "Name",
        "Department",
        "Salary"
    ]

    for employee in employees:

        table.add_row([
            employee["id"],
            employee["name"],
            employee["department"],
            employee["salary"]
        ])

    return table


def main():

    employees = get_all_employees()

    print("HR EMPLOYEE REPORT")
    print("==================")
    print()

    for employee in employees:

        report = create_report(employee)

        print(report)
        print()

    print("EMPLOYEE TABLE")
    print("==============")

    table = create_table(employees)

    print(table)


main()
