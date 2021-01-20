import React, { useState } from 'react';
import ReactDOM from 'react-dom';

import { ProductPrice } from './components/ProductPrice';
import { ShoppingCart } from './components/ShoppingCart';

document.addEventListener('DOMContentLoaded', (event) => {
  if (document.getElementById('product_price')) {
    const element = document.getElementById('product_price');
    const productId = element.dataset.productId;
    ReactDOM.render(<ProductPrice id={ productId } />, element);
  }

  if (document.getElementById('shopping_cart')) {
    ReactDOM.render(<ShoppingCart />, document.getElementById('shopping_cart'));
  }
});
