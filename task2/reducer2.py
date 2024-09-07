#!/usr/bin/env python3

import sys

costs = {
    "user/profile": 100,
    "user/settings": 200,
    "order/history": 300,
    "order/checkout": 400,
    "product/details": 500,
    "product/search": 600,
    "cart/add": 700,
    "cart/remove": 800,
    "payment/submit": 900,
    "support/ticket": 1000
}

for l in sys.stdin:
    line = l.strip()
    line_array = line.split(' ')
    if len(line_array) == 2:
        print(line)
    elif len(line_array) == 6:
        timestamp = line_array[0]
        request_id = line_array[1]
        client_id = line_array[2]
        endpoint = line_array[3]
        no_of_servers_down = int(line_array[4])
        status = int(line_array[5])
        cost = costs[endpoint] if status == 200 else 0
        print(f"{timestamp} {request_id} {client_id} {endpoint} {no_of_servers_down} {status} {cost}")
