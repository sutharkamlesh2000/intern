/** @odoo-module **/

import publicWidget from '@web/legacy/js/public/public_widget';
import { jsonrpc } from "@web/core/network/rpc_service";

publicWidget.registry.ProductListWidget = publicWidget.Widget.extend({

    selector: ".product-list-container",

    events: {
        // 'click #search-product-btn':'onSeachBtn',
        'change input[name="product_search"]': '_onChangeSearch',
    },

    // onSeachBtn :function(){
    //     var val = document.querySelector('#product-search')
    //     console.log('Inside btn',val)
    // },

    _onChangeSearch: function () {
        var val = document.querySelector('#product-search').value
        console.log(val, "vallll")
        jsonrpc('/search-data/', {
            name: val,
        }).then((response) => {
            console.log('response\t\t',response.products)
            document.querySelectorAll(".product-item").innerHTML = ' ';
            
            response.forEach((product) => {
                console.log(product.name,"\t\t product name")
            });


            // response.forEach((product) => {
                // var productHTML = `<div class="product-item" style="border: 1px solid #ddd; margin-bottom: 20px; padding: 15px; border-radius: 8px; box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);">
                //                 <div class="product-info" style="display: flex; justify-content: space-between; align-items: center;">
                //                     <div class="product-image" style="flex-shrink: 0; width: 120px; height: 120px; background-color: #f4f4f4; display: flex; align-items: center; justify-content: center;">
                //                         <img t-if="product.image_1920" t-att-src="${product.image_1920}" style="max-width: 100%; max-height: 100%; object-fit: cover;" alt="Product Image"/>
                //                     </div>
                                    
                //                     <div class="product-details" style="flex-grow: 1; margin-left: 20px;">
                //                         <h3 style="margin: 0; color: #007bff; font-size: 20px;"><t t-esc="${product.name}"/></h3>
                //                         <p style="margin: 5px 0; color: #666; font-size: 14px;"><strong>Description:</strong> <t t-esc="${product.description_sale}"/></p>
                //                         <p style="margin: 5px 0; color: #333; font-size: 16px;"><strong>Price:</strong> <t t-esc="${product.list_price}"/> USD</p>
                //                         <p style="margin: 5px 0; color: #333; font-size: 14px;"><strong>Available Stock:</strong> <t t-esc="${product.qty_available}"/></p>
                //                     </div>
                
                //                     <div class="product-action" style="text-align: center;">
                //                         <button style="padding: 10px 15px; background-color: #28a745; color: white; border: none; border-radius: 5px; cursor: pointer; font-size: 16px;">
                //                             <t t-esc="'Add to cart'"></t>
                //                         </button>
                //                     </div>
                //                 </div>
                // </div>` ;

            // });

        });
    },
})