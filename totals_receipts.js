// Total sales
const sales = [
  {item: "sticker", quantity: 5, price: 4},
  {item: "printable deck", quantity: 10, price: 17},
  {item: "SS Deck", quantity: 5, price: 33}
];

function calculateTotalSales(sales) {
  let total = 0;
  for (let i = 0; i < sales.length; i++) {
    total += sales[i].quantity*sales[i].price;
  }
  return total;
}

console.log ("Total Sales Amount:", calculateTotalSales(sales));

//Order receipt
const orders = [
  {item: "sticker", quantity: 2, price: 4},
  {item: "printable deck", quantity: 0, price: 17},
  {item: "SS Deck", quantity: 1, price: 33},
  {item: "shipping", quantity: 1, price: 5}
];

function generateReceipt(orders) {
  let grandTotal = 0;
  console.log("Receipt:");
  console.log("-------------------");
  for (let i = 0; i < orders.length; i++) {
    const itemTotal = orders[i].quantity * orders[i].price;
    grandTotal += itemTotal;
    console.log(`${orders[i].item} - Quantity: ${orders[i].quantity}, Price: $${orders[i].price}, Total: $${itemTotal}`);
  }
  console.log("-----------------");
  console.log(`Grand Total: $${grandTotal}`);
}
generateReceipt(orders);
