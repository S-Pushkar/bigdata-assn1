#!/usr/bin/env python3

import sys
import json

for l in sys.stdin:
    line = l.strip().strip(',')
    if line == '' or line == '[' or line == ']':
        continue

    try:
        data = json.loads(line)
    except json.JSONDecodeError:
        continue

    city = data.get('city', '')
    categories = data.get('categories', [])
    sales_data = data.get('sales_data', {})

    if not sales_data:
        print(city, 0, 0, sep='\t')
        continue

    has_sales_data = False
    total_revenue = 0
    total_cogs = 0
    for category in categories:
        if category in sales_data:
            revenue = sales_data[category].get('revenue', 0)
            cogs = sales_data[category].get('cogs', 0)
            total_revenue += revenue
            total_cogs += cogs
            has_sales_data = True
    
    if not has_sales_data:
        print(city, 0, 0, sep='\t')
        continue

    if total_revenue - total_cogs > 0:
        print(city, 1, 0, sep='\t')
    else:
        print(city, 0, 1, sep='\t')
