url = 'http://localhost:8080'
db = 'odoo15_divya'
username = 'admin'
password = 'admin'
file_name_with_path = '/home/konsultoo/Downloads/sales_order_sale.order.csv'

import csv
from xmlrpc import client
import logging
from datetime import datetime
import math

common = client.ServerProxy('{}/xmlrpc/2/common'.format(url))
common.version()
uid = common.authenticate(db, username, password, {})
models = client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# with open(file_name_with_path) as csvfile:
#     reader = csv.DictReader(csvfile)
#     print('CSV FILE  :  ', type(reader))

# dict_from_csv = {}

with open(file_name_with_path, mode='r') as inp:
    reader = csv.reader(inp)
    # dict_from_csv = {rows[0]: columns[0] for rows, columns in reader}
    for row in reader:

        if row[0] != 'Order Reference':
            company_ids = models.execute_kw(db, uid, password, 'res.company', 'search_read', [[
                ['name', '=', row[4]],
            ]])
            print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<')
            if not company_ids:
                company_vals = {
                    'name': row[4]
                }
                company_id = models.execute_kw(db, uid, password, 'res.company', 'create', [company_vals])

            # print ("\n\nCompany IDDDDDDDd", company_ids[0]['id'])
            partner_ids = models.execute_kw(db, uid, password, 'res.partner', 'search_read', [[
                ['name', '=', row[2]], ['company_id', '=', company_ids[0]['id']],
            ]], {'fields': ['name']})
            print(">>>>>>>>>>>>>>>>>>>>>>>>", partner_ids)
            if not partner_ids:
                customer_vals = {
                    'name': row[2],
                    'customer_rank': 1,
                    'company_id': company_ids[0]['id']
                }
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'create', [customer_vals])

            # user_ids = models.execute_kw(db, uid, password, 'res.users', 'search_read', [[
            #     ['name', '=', row[3]], ['company_id', '=', company_ids[0]['id']]]], {'fields': ['name']})
            # print('?????????????????????????????????????')
            # if not user_ids:
            #     salesperson_vals = {
            #         'name': row[3],
            #         'login': row[3] + "@gmail.com",
            #         'company_id': company_ids[0]['id']
            #     }
            #     user_id = models.execute_kw(db, uid, password, 'res.users', 'create', [salesperson_vals])

            if partner_ids and company_ids:
                partner_id = models.execute_kw(db, uid, password, 'res.partner', 'search', [[
                    ['id', '=', partner_ids[0].get('id')]
                ]])
                company_id = models.execute_kw(db, uid, password, 'res.company', 'search', [[
                    ['id', '=', company_ids[0].get('id')]
                ]])
                # user_id = models.execute_kw(db, uid, password, 'res.users', 'search', [[
                #     ['id', '=', user_ids[0].get('id')]
                # ]])
                print("partner id, user ids and company ids are already exists")

                so_vals = {
                    'name': row[0],
                    'partner_id': partner_id[0],
                    'date_order': row[1],
                    # 'user_id': user_ids[0],
                    'company_id': company_id[0],
                    'create_date': row[7],
                }
                so_id = models.execute_kw(db, uid, password, 'sale.order', 'create', [so_vals])
                print('so created>>>>>>>>>>>>>>>>>', so_id)
