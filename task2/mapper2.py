#!/usr/bin/env python3

import sys

servers = {
    "user/profile": -1,
    "user/settings": -1,
    "order/history": -1,
    "order/checkout": -1,
    "product/details": -1,
    "product/search": -1,
    "cart/add": -1,
    "cart/remove": -1,
    "payment/submit": -1,
    "support/ticket": -1
}

previous_timestamp = ''

clients_in_current_timestamp = set()

endpoints = set(servers.keys())

for l in sys.stdin:
    line = l.strip()
    line_array = line.split(',')
    if len(line_array) == 2:
        print(line)
    elif len(line_array) == 5:
        timestamp = line_array[0]
        client_id = line_array[2]
        request_id = line_array[1]
        endpoint = line_array[3]
        no_of_servers_down = int(line_array[4])
        if timestamp == previous_timestamp:
            if client_id not in clients_in_current_timestamp:
                if no_of_servers_down == 3:
                    servers[endpoint] = 0
                    clients_in_current_timestamp.add(client_id)
                    print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
                elif servers[endpoint] == -1:
                    servers[endpoint] = 2 - no_of_servers_down
                    clients_in_current_timestamp.add(client_id)
                    print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
                elif servers[endpoint] > 0:
                    servers[endpoint] -= 1
                    clients_in_current_timestamp.add(client_id)
                    print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
                else:
                    clients_in_current_timestamp.add(client_id)
                    print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        else:
            previous_timestamp = timestamp
            for server in servers.keys():
                servers[server] = -1
            clients_in_current_timestamp.clear()
            if no_of_servers_down == 3:
                servers[endpoint] = 0
                clients_in_current_timestamp.add(client_id)
                print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
                continue
            servers[endpoint] = 2 - no_of_servers_down
            clients_in_current_timestamp.add(client_id)
            print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
        # if timestamp == previous_timestamp and client_id in clients_in_current_timestamp:
        #     continue
        # # if no_of_servers_down == 3:
        # #     print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        # else:
        #     if timestamp == previous_timestamp:
        #         if client_id not in clients_in_current_timestamp:
        #             if no_of_servers_down == 3:
        #                 servers[endpoint] = 0
        #                 clients_in_current_timestamp.add(client_id)
        #                 print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        #             if servers[endpoint] == -1:
        #                 servers[endpoint] = 2 - no_of_servers_down
        #                 clients_in_current_timestamp.add(client_id)
        #                 print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
        #             elif servers[endpoint] > 0:
        #                 servers[endpoint] -= 1
        #                 clients_in_current_timestamp.add(client_id)
        #                 print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
        #             else:
        #                 clients_in_current_timestamp.add(client_id)
        #                 print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        #     else:
        #         previous_timestamp = timestamp
        #         for server in servers.keys():
        #             servers[server] = -1
        #         # previous_timestamp = timestamp
        #         clients_in_current_timestamp.clear()
        #         if no_of_servers_down == 3:
        #             servers[endpoint] = 0
        #             clients_in_current_timestamp.add(client_id)
        #             print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},500")
        #             continue
        #         servers[endpoint] = 2 - no_of_servers_down
        #         clients_in_current_timestamp.add(client_id)
        #         print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down},200")
