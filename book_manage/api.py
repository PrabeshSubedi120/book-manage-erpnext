import frappe
from frappe.utils import nowdate

@frappe.whitelist()
def check_overdue_users(book_name):
    overdue_users = frappe.db.sql("""
        SELECT bs.user
        FROM `tabBook Submission` bs
        JOIN `tabBook` b ON bs.book = b.name
        WHERE b.name = %s
        AND b.submission_deadline < %s
        AND bs.status != 'Submitted'
    """, (book_name, nowdate()), as_dict=1)

    if overdue_users:
        return "Overdue Users: " + ", ".join([u.user for u in overdue_users])
    else:
        return "No overdue users found."
