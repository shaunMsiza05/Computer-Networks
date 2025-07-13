from socket import *
import time

# Setup
serverAddress = ('localhost', 12000)
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.settimeout(1)  # 1-second timeout for each ping

# Statistics
pingStatistics = {
    'packetsSent': 0,
    'packetsReceived': 0,
    'RTTs': []
}

# Main loop for sending 10 pings
for sequence_Number in range(1, 11):
    send_time = time.time()
    message = f"Ping {sequence_Number} {send_time}"
    pingStatistics['packetsSent'] += 1

    try:
        clientSocket.sendto(message.encode(), serverAddress)
        # if not data is returned, recvfrom will throw a timeout exception
        response, addr = clientSocket.recvfrom(1024)
        receive_time = time.time()
        rtt = receive_time - send_time

        pingStatistics['packetsReceived'] += 1
        pingStatistics['RTTs'].append(rtt)

        print(f"Reply from {addr}: {response.decode()} RTT: {rtt:.4f} seconds")

    except timeout:
        print(f"Request timed out (seq #{sequence_Number})")

# Socket cleanup
clientSocket.close()

# Final stats
packetsLost = pingStatistics['packetsSent'] - pingStatistics['packetsReceived']
lossRate = (packetsLost / pingStatistics['packetsSent']) * 100
rtts = pingStatistics['RTTs']
minRTT = min(rtts) if rtts else 0
maxRTT = max(rtts) if rtts else 0
avgRTT = sum(rtts) / len(rtts) if rtts else 0

print(f"\nPackets: Sent = {pingStatistics['packetsSent']}, "
      f"Received = {pingStatistics['packetsReceived']}, "
      f"Lost = {packetsLost} ({lossRate:.0f}% loss)")
print(f"RTT stats: Min = {minRTT:.4f}s, Max = {maxRTT:.4f}s, Avg = {avgRTT:.4f}s")
