from odoo import http
from odoo.http import request


class SchoolData(http.Controller):
    @http.route('/',type='http', auth='public', website=True)
    def get_products(self, **kw):
        products = request.env['product.template'].search([])
        context = {
            'products':products
        }
        return request.render('js.products_list',context)

    @http.route('/search-data/',  type='json', website=True, auth='public')
    def filter_product(self, **kw):
        products = request.env['product.template'].search([('name','ilike',kw.get('name'))])
        product_data = []
        for rec in products:
            product_data.append({
                'id':rec.id,
                'name':rec.name,
                'description_sale':rec.description_sale,
                'list_price':rec.list_price,
                'qty_available':rec.qty_available,
            }) 
        return {
            'status':200,
            'products':product_data,
            }