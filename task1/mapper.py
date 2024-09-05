import sys
import json

for l in sys.stdin:
    line = l.strip()
    if line == '' or line[0] == '[' or line[0] == ']':
        continue
    data = json.loads(line)
    city = ''
    if 'city' in data:
        city = data['city']
    categories = data['categories']
    category_output = {}
    for category in categories:
        category_output[category] = 0

    if 'sales_data' in data:
        for category in categories:
            if category in data['sales_data']:
                revenue = -1
                if 'revenue' in data['sales_data'][category]:
                    revenue = data['sales_data'][category]['revenue']
                if 'cogs' in data['sales_data'][category]:
                    revenue -= data['sales_data'][category]['cogs']
                category_output[category] = revenue

    for category in category_output:
        print(city, 1 if category_output[category] > 0 else 0, 1 if category_output[category] <= 0 else 0, sep='\t')
