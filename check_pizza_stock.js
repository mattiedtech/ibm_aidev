const products = [
  {product: "Pepperoni", stock: 6},
  {product: "Pineapple", stock: 0},
  {product: "Mozzarella", stock: 25},
  {product: "Dough", stock: 40},
  {product: "Sauce", stock: 100}
];

function checkStockLevels(products) {
  for (let i = 0; i < products.length; i++) {
    if (products[i].stock > 0) {
      console.log(`${products[i].product} is In Stock.`);
    } else {
      console.log(`${products[i].product} is Out of Stock.`)
    }
  }
}

checkStockLevels(products);
