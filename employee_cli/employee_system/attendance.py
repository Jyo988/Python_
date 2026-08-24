
attendance_records = {}


def mark_attendance(employee_id, present):

    if employee_id not in attendance_records:

        attendance_records[employee_id] = []

    attendance_records[employee_id].append(present)


def get_attendance(employee_id):

    return attendance_records.get(employee_id, [])


def calculate_attendance_percentage(employee_id):

    records = get_attendance(employee_id)

    if len(records) == 0:
        return 0

    present_days = sum(records)

    percentage = (present_days / len(records)) * 100

    return percentage
