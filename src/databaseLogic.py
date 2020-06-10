from openpyxl import Workbook
from openpyxl import load_workbook 


wb=load_workbook('./db/shopdata.xlsx')

def getCustomerID(invoiceID):
    invoice_ws = wb["invoice"]
    for row in invoice_ws['A']:
        if row.value == invoiceID:
            customerID = invoice_ws.cell(row=row.row, column=row.column+1).value 
    return customerID

def getCustomerName(customerID):
    customer_ws = wb['customer']    
    for row in customer_ws['A']:
        if row.value == customerID:
            customerFName = customer_ws.cell(row=row.row, column=row.column+1).value
            customerLName = customer_ws.cell(row=row.row, column=row.column+2).value
    return f"{customerFName} {customerLName}"


def create_invoice(invoiceID):
    customerID =getCustomerID(invoiceID) 
    full_name =getCustomerName(customerID)
    return {
        'name':full_name,
        
        }
    