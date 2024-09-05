#!/usr/bin/env python3

import sys
import json

cities = {}

for l in sys.stdin:
    line = l.strip()
    city, profit, loss = line.split('\t')
    if city not in cities:
        cities[city] = {}
        cities[city]['city'] = city
        cities[city]['profit_stores'] = 0
        cities[city]['loss_stores'] = 0
    cities[city]['profit_stores'] += int(profit)
    cities[city]['loss_stores'] += int(loss)

for city in cities:
    output = json.dumps(cities[city])
    print(output)
