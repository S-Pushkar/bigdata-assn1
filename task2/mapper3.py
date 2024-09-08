#!/usr/bin/env python3

import sys

for l in sys.stdin:
    line = l.strip()
    line_array = line.split(',')
    if len(line_array) == 2:
        print(line)
    elif len(line_array) == 7:
        timestamp = int(line_array[0])
        request_id = line_array[1]
        client_id = line_array[2]
        endpoint = line_array[3]
        no_of_servers_down = int(float(line_array[4]))
        status_code = int(line_array[5])
        cost = int(line_array[6])
        print(f"{request_id},{client_id},{status_code},{cost}")
