from __future__ import unicode_literals
import frappe
from frappe import _

def execute(filters=None):
    columns, data = get_columns(), get_data(filters)
    return columns, data

def get_columns():
    return [
        {"label": _("Sales Order No"), "fieldname": "sales_order_no", "fieldtype": "Link", "options": "Sales Order", "width": 150},
        {"label": _("Customer Name"), "fieldname": "customer_name", "fieldtype": "Data", "width": 200},
        {"label": _("Customer PO No"), "fieldname": "customer_po_no", "fieldtype": "Data", "width": 150},
        {"label": _("Item Code"), "fieldname": "item_code", "fieldtype": "Link", "options": "Item", "width": 150},
        {"label": _("Item Name"), "fieldname": "item_name", "fieldtype": "Data", "width": 200},
        {"label": _("Status"), "fieldname": "status", "fieldtype": "Data", "width": 150},
        {"label": _("Qty"), "fieldname": "qty", "fieldtype": "Float", "width": 100},
        {"label": _("Delivered Qty"), "fieldname": "delivered_qty", "fieldtype": "Float", "width": 100},
        {"label": _("Qty to Deliver"), "fieldname": "qty_to_deliver", "fieldtype": "Float", "width": 100}
    ]

def get_data(filters):
    conditions = ""
    if filters.get("from_date") and filters.get("to_date"):
        conditions = "so.transaction_date BETWEEN '{0}' AND '{1}'".format(filters.get("from_date"), filters.get("to_date"))
    
    data = frappe.db.sql("""
        SELECT
            so.name AS sales_order_no,
            so.customer_name AS customer_name,
            so.po_no AS customer_po_no,
            soi.item_code AS item_code,
            soi.item_name AS item_name,
            so.status AS status,
            soi.qty AS qty,
            soi.delivered_qty AS delivered_qty,
            soi.qty - soi.delivered_qty AS qty_to_deliver
        FROM
            `tabSales Order` AS so
        JOIN
            `tabSales Order Item` AS soi ON soi.parent = so.name
        WHERE
            (so.status = 'To Deliver' OR so.status = 'To Deliver and Bill')
            AND {conditions}
        ORDER BY
            so.transaction_date DESC
    """.format(conditions=conditions), as_dict=True)

    return data
