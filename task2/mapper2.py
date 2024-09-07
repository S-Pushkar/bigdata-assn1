#!/usr/bin/env python3

import sys

servers = {
    "user/profile": [],
    "user/settings": [],
    "order/history": [],
    "order/checkout": [],
    "product/details": [],
    "product/search": [],
    "cart/add": [],
    "cart/remove": [],
    "payment/submit": [],
    "support/ticket": []
}

endpoints = set(servers.keys())

for l in sys.stdin:
    line = l.strip()
    line_array = line.split(' ')
    if len(line_array) == 2:
        request_id = line_array[0]
        prediction = line_array[1]
        print(f"{request_id} {prediction}")
    elif len(line_array) == 5:
        timestamp = int(line_array[0])
        request_id = line_array[1]
        client_id = line_array[2]
        endpoint = line_array[3]
        no_of_servers_down = int(float(line_array[4]))
        if not endpoint in endpoints:
            continue
        endpoint_state = [i for i in servers[endpoint]]
        has_current_client_been_added = False
        for client in endpoint_state:
            client_timestamp = int(client['timestamp'])
            if timestamp - client_timestamp > 1:
                servers[endpoint].remove(client)
                if len(servers[endpoint]) + no_of_servers_down < 3 and not has_current_client_been_added:
                    servers[endpoint].append({'request_id': request_id, 'client_id': client_id, 'timestamp': timestamp})
                    has_current_client_been_added = True
                    str_timestamp = str(timestamp).zfill(9)
                    print(f"{str_timestamp} {request_id} {client_id} {endpoint} {no_of_servers_down} 200")
        if not has_current_client_been_added:
            if len(servers[endpoint]) + no_of_servers_down < 3:
                servers[endpoint].append({'request_id': request_id, 'client_id': client_id, 'timestamp': timestamp})
                timestamp = str(timestamp).zfill(9)
                print(f"{timestamp} {request_id} {client_id} {endpoint} {no_of_servers_down} 200")
            else:
                timestamp = str(timestamp).zfill(9)
                print(f"{timestamp} {request_id} {client_id} {endpoint} {no_of_servers_down} 500")
