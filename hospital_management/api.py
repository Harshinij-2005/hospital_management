import frappe
from frappe.query_builder import DocType
from frappe.utils import now


@frappe.whitelist()
def test_document_database_querybuilder():

    Appointment = DocType("Appointment")
    Patient = DocType("Patient Data")

    records = (
        frappe.qb.from_(Appointment)
        .join(Patient)
        .on(Appointment.patient == Patient.name)
        .select(
            Appointment.name,
            Appointment.patient,
            Patient.first_name,
            Patient.last_name,
            Appointment.status
        )
        .limit(5)
        .run(as_dict=True)
    )

    if records:
        # Document API
        doc = frappe.get_doc("Appointment", records[0]["name"])
        doc.status = "Completed"
        doc.save()

        # Database API
        for row in records:
            frappe.db.set_value(
                "Appointment",
                row["name"],
                "department",
                "General"
            )

    return records


@frappe.whitelist()
def get_recent_todos():
    # Securely fetch the latest 5 ToDo records
    todos = frappe.get_list(
        "ToDo",
        fields=["name", "description", "owner"],
        order_by="creation desc",
        limit=5
    )

    result = []

    for todo in todos:
        owner_email = frappe.db.get_value(
            "User",
            todo["owner"],
            "email"
        )

        result.append({
            "name": todo["name"],
            "description": todo["description"],
            "owner_email": owner_email
        })

    return {
        "timestamp": now(),
        "records": result
    }


def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")
    