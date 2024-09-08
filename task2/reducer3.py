#!/usr/bin/env python3

import sys

prediction = 0

clients = {}

for l in sys.stdin:
    line = l.strip()
    line_array = line.split(' ')
    if len(line_array) == 2:
        prediction = int(line_array[1])
    elif len(line_array) == 4:
        request_id = line_array[0]
        client_id = line_array[1]
        status_code = int(line_array[2])
        cost = int(line_array[3])
        if client_id not in clients:
            clients[client_id] = {"total_cost": 0, "total_requests": 0, "number_of_correct_predictions": 0}
        clients[client_id]["total_cost"] += cost
        clients[client_id]["total_requests"] += 1
        if status_code == prediction:
            clients[client_id]["number_of_correct_predictions"] += 1

for client_id in sorted(clients.keys()):
    print(f"{client_id} {clients[client_id]['number_of_correct_predictions']}/{clients[client_id]['total_requests']} {clients[client_id]['total_cost']}")
