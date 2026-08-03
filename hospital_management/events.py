import frappe

def appointment_created(doc, method):
    frappe.msgprint("Appointment Created Successfully")