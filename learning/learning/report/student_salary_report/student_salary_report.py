import frappe

def execute(filters=None):
    columns = [
        {
            "label": "Employee ID",
            "fieldname": "employee_id",
            "fieldtype": "Int",
            "width": 120
        },
        {
            "label": "Employee Name",
            "fieldname": "employee_name",
            "fieldtype": "Data",
            "width": 180
        },
        {
            "label": "Salary",
            "fieldname": "salary",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = [
        {
            "employee_id": 1,
            "employee_name": "Harshini",
            "salary": 45000
        },
        {
            "employee_id": 2,
            "employee_name": "Divya",
            "salary": 50000
        },
        {
            "employee_id": 3,
            "employee_name": "Priya",
            "salary": 40000
        }
    ]

    return columns, data
