import React, { useRef } from 'react';

export const ShoppingCartForm = function ({ priceTotal }) {
  const shippingAddressEl = useRef(null);

  const submit = (e) => {
    const addressId = document.querySelector('input[name="shipping_address"]:checked').value;
    shippingAddressEl.current.value = addressId;
  };

  return (
    <form action="/orders/" method="post" className="col-sm-3" onSubmit={ (e) => submit(e) }>
      <input type="hidden" name="shipping_address" value="0" ref={ shippingAddressEl } />
      <input type="hidden" name="csrfmiddlewaretoken" value={ window.csrf } />
      <dl className="dlist-align">
        <dt>{ gettext('Total price') }</dt>
        <dd className="text-right">{ priceTotal }</dd>
      </dl>
      <dl className="dlist-align">
        <dt>Other Fees</dt>
        <dd className="text-right"></dd>
      </dl>
      <dl className="dlist-align h4">
        <dt>{ gettext('Total') }</dt>
        <dd className="text-right"><strong>{ priceTotal }</strong></dd>
      </dl>
      <textarea className="form-control mb-3"></textarea>
      <button className="btn btn-success btn-large" type="submit">Submit</button>
    </form>
  );
};
