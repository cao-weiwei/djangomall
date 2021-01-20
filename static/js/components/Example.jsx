import React, { useState } from 'react';
// 导出 Example
export const Example = function () {
  // 定义两个 state 变量， count 和 name
  const [count, setCount] = useState(0);
  const [name, setName] = useState();

  return (
    <div>
      <p>
        <i className="fas fa-shopping-cart"></i>
        {count}, {name}
      </p>
      <input
        type="radio"
        name="product"
        value="product1"
        onClick={(e) => setName(e.target.value)}
      />
      <input type="radio" name="product" onClick={() => setName('product2')} />
      <button className="btn btn-success" onClick={() => setCount(count + 1)}>
        Add to Cart
      </button>
    </div>
  );
};