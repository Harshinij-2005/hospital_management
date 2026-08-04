from frappe.query_builder import DocType
import frappe

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

def custom_logic(doc, method):
    frappe.msgprint("Hook executed!")