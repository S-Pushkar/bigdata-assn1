#!/usr/bin/env python3

import sys

for l in sys.stdin:
    line = l.strip()
    line_arr = line.split(' ')
    if len(line_arr) == 2:
        request_id = line_arr[0]
        prediction = line_arr[1]
        print(f"{request_id},{prediction}")
    elif len(line_arr) == 5 or len(line_arr) == 4:
        request_id = line_arr[0]
        client_id = line_arr[1]
        endpoint = line_arr[2]
        timestamp = line_arr[3]
        no_of_servers_down = 0
        if len(line_arr) == 5:
            no_of_servers_down = int(float(line_arr[4]))
        print(f"{timestamp},{client_id},{request_id},{endpoint},{no_of_servers_down}")
