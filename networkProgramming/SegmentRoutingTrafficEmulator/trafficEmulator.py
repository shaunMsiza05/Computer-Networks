# Define routers and segments
routers = {
    'R1': {'sid': 101},
    'R2': {'sid': 102},
    'R3': {'sid': 103},
    'R4': {'sid': 104},
    'R5': {'sid': 105}
}

# Define links with RTTs and loss probabilities
links = {
    ('R1', 'R2'): {'rtt': 20, 'drop_prob': 0.05},
    ('R2', 'R5'): {'rtt': 30, 'drop_prob': 0.1},
    ('R1', 'R3'): {'rtt': 25, 'drop_prob': 0.03},
    ('R3', 'R4'): {'rtt': 20, 'drop_prob': 0.05},
    ('R4', 'R5'): {'rtt': 30, 'drop_prob': 0.02}
}

import random

def forward_packet(sid_stack):
    total_rtt = 0
    dropped = False

    for i in range(len(sid_stack) - 1):
        link = (sid_stack[i], sid_stack[i+1])
        params = links.get(link)

        if params:
            total_rtt += params['rtt']
            if random.random() < params['drop_prob']:
                dropped = True
                break  # Packet dropped on this link
        else:
            print(f"No link from {sid_stack[i]} to {sid_stack[i+1]}")
            dropped = True
            break

    return total_rtt, dropped

loss_count = 0
timeout_threshold = 2
max_rtt = 100  # Example maximum RTT to consider timeout

def monitor_and_trigger(primary_path, backup_path):
    global loss_count
    rtt, dropped = forward_packet(primary_path)

    if dropped or rtt > max_rtt:
        loss_count += 1
    else:
        loss_count = 0

    if loss_count >= timeout_threshold:
        print("💥 Rerouting traffic due to loss/timeout")
        rtt, dropped = forward_packet(backup_path)
        loss_count = 0  # Reset after reroute
        return rtt, dropped

    return rtt, dropped

primary = ['R1', 'R2', 'R5']
backup = ['R1', 'R3', 'R4', 'R5']

for cycle in range(1, 11):
    print(f"\nCycle {cycle}:")
    rtt, dropped = monitor_and_trigger(primary, backup)
    print(f"RTT: {rtt}, Dropped: {dropped}")

 
