import React from "react";
import "./App.css";

function App() {
  let [invoice, setInvoice] = React.useState(1);
  let [invoiceResp, setInvoiceResp] = React.useState({name: null, items: []});
  // let [items, setItems] = React.useState()

const getInvoice = async () =>{
  let x = await fetch('http://127.0.0.1:5000/'+invoice)
  let res = await x.json();

  setInvoiceResp(res)

  // console.log(items);
  
}
  const handleInvoiceChange = (e) => {
    setInvoice(e.target.value);
  };

  return (
    <div className="App">
      <header className="App-header">
        <p> Invoice App</p>
        <label>
          Enter invoice number here:
          <input type="number" onChange={handleInvoiceChange} />
        </label>
        <button onClick={getInvoice}>Find Invoice</button>

        <p>Customer name: {invoiceResp.name}</p>
        {/* <p>Items: {items}</p> */}
        { invoiceResp.items && invoiceResp.items.map((item, idx) => <div key={idx}>
          <li>
          Name:{item['name']},
          qty: {item['qty']},
          price each: ${item['price']}
          </li>
        </div>)}
        
        <p>ID: {invoiceResp.invoiceID}</p>

      </header>
    </div>
  );
}

export default App;
