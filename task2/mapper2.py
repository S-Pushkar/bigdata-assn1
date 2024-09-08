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
    line_array = line.split(',')
    if len(line_array) == 2:
        print(line)
    elif len(line_array) == 5:
        timestamp = int(line_array[0])
        client_id = line_array[1]
        request_id = line_array[2]
        endpoint = line_array[3]
        no_of_servers_down = int(line_array[4])
        if not endpoint in endpoints:
            continue
        has_current_client_been_added = False
        if no_of_servers_down == 3:
            str_timestamp = str(timestamp).zfill(9)
            has_current_client_been_added = True
            print(f"{str_timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        endpoint_state = [i for i in servers[endpoint]]
        is_current_client_in_endpoint_state = False
        for server in servers.keys():
            servers_tmp = [i for i in servers[server]]
            for client in servers_tmp:
                if timestamp - client['timestamp'] > 0 and client in servers[server]:
                    servers[server].remove(client)
                if client['client_id'] == client_id:
                    is_current_client_in_endpoint_state = True
        for client in endpoint_state:
            client_timestamp = client['timestamp']
            if client['client_id'] == client_id:
                is_current_client_in_endpoint_state = True
            if timestamp - client_timestamp > 0 and client in servers[endpoint]:
                servers[endpoint].remove(client)
                if len(servers[endpoint]) + no_of_servers_down < 3 and not has_current_client_been_added and not is_current_client_in_endpoint_state:
                    servers[endpoint].append({'request_id': request_id, 'client_id': client_id, 'timestamp': timestamp})
                    has_current_client_been_added = True
                    str_timestamp = str(timestamp).zfill(9)
                    print(f"{str_timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
        if not has_current_client_been_added:
            if len(servers[endpoint]) + no_of_servers_down < 3 and not is_current_client_in_endpoint_state:
                servers[endpoint].append({'request_id': request_id, 'client_id': client_id, 'timestamp': timestamp})
                timestamp = str(timestamp).zfill(9)
                print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
            else:
                timestamp = str(timestamp).zfill(9)
                print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
