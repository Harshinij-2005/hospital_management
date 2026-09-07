import frappe


def execute(filters=None):
    columns = [
        {
            "label": "Name",
            "fieldname": "name",
            "fieldtype": "Data",
            "width": 150
        },
        {
            "label": "Description",
            "fieldname": "description",
            "fieldtype": "Data",
            "width": 300
        },
        {
            "label": "Amount",
            "fieldname": "amount",
            "fieldtype": "Currency",
            "width": 150
        }
    ]

    data = [
        {
            "name": "TEST-001",
            "description": "First test document",
            "amount": 1000
        },
        {
            "name": "TEST-002",
            "description": "Second test document",
            "amount": 2500
        },
        {
            "name": "TEST-003",
            "description": "Third test document",
            "amount": 5000
        }
    ]

    return columns, data