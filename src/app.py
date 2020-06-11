from flask import Flask, jsonify, request, render_template
from databaseLogic import create_invoice
# do this in VS live share
#harmonize excel sheets
#4 sheets
# DONE
app = Flask(__name__)

@app.route('/')
def home():
    return "hello"

@app.route('/<int:invoice_id>')
def getInvoiceObj(invoice_id):
    name = create_invoice(invoice_id)["name"]
    return jsonify(create_invoice(invoice_id)), 200
    # return render_template('main.html', name=name)

app.run(port=5000)
# SERVER SIDE CODE (pyhton)
# pull data from an excel sheet in the repository
# code that makes an invoice object --> jsonify it
# this will be @app.route //not class _____ server 
# only one route to make inovices (invoice/#)
# based on the #, we will spit out that invoice
# i don't see a need for a POST at this point

# JS (react, fetch)
# htttp/// _____/invoice/
# GET data
# display as REACT table (flask template)

