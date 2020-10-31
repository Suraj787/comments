import frappe

def copy_comments_on_amend(doc,method=None):
    if doc.amended_from:
        comments = frappe.get_list("Comment",filters={"reference_name":doc.amended_from})
        for c in comments:
            comment = frappe.get_doc("Comment",c['name'])
            comment_copy = frappe.copy_doc(comment)
            comment_copy.reference_name = doc.name
            comment_copy.save()
    frappe.db.commit()