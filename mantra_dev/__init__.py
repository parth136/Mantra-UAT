__version__ = "0.0.1"
import erpnext.stock.doctype.stock_reservation_entry.stock_reservation_entry
# import mantra_dev.backend_code.stock_reservation_entry
import mantra_dev.backend_code.stock_reservation_entry.stock_reservation_entry

import erpnext.accounts.doctype.purchase_invoice.purchase_invoice
import mantra_dev.purchase_invoice

import erpnext.stock.doctype.purchase_receipt.purchase_receipt
import mantra_dev.purchase_receipt

erpnext.stock.doctype.stock_reservation_entry.stock_reservation_entry.create_stock_reservation_entries_for_so_items = mantra_dev.backend_code.stock_reservation_entry.stock_reservation_entry.create_stock_reservation_entries_for_so_items

erpnext.accounts.doctype.purchase_invoice.purchase_invoice.PurchaseInvoice.po_required = mantra_dev.purchase_invoice.PurchaseInvoice.po_required

erpnext.accounts.doctype.purchase_invoice.purchase_invoice.PurchaseInvoice.pr_required = mantra_dev.purchase_invoice.PurchaseInvoice.pr_required

erpnext.stock.doctype.purchase_receipt.purchase_receipt.PurchaseReceipt.po_required = mantra_dev.purchase_invoice.PurchaseInvoice.po_required