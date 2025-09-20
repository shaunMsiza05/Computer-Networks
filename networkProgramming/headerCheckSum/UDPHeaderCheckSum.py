import struct

# ----------------------------------------
# Function: Calculate one's complement checksum
# ----------------------------------------
def checksum(data):
    """
    Calculates the one's complement checksum for the given byte data.
    Pads with zero if the length is odd.
    """
    if len(data) % 2 != 0:
        data += b'\x00'  # Pad to even length

    total = 0
    for i in range(0, len(data), 2):
        word = (data[i] << 8) + data[i + 1]  # Combine two bytes
        total += word
        total = (total & 0xFFFF) + (total >> 16)  # Wrap around carry

    return ~total & 0xFFFF  # One's complement

# ----------------------------------------
# Function: Build the pseudo header
# ----------------------------------------
def build_pseudo_header(src_ip, dst_ip, protocol, udp_length):
    """
    Constructs the pseudo header used in UDP checksum calculation.
    Includes source IP, destination IP, protocol number, and UDP length.
    """
    return struct.pack('!4s4sBBH', src_ip, dst_ip, 0, protocol, udp_length)

# ----------------------------------------
# Step 1: Define IP addresses and protocol
# ----------------------------------------
src_ip = b'\xC0\xA8\x00\x01'  # 192.168.0.1
dst_ip = b'\xC0\xA8\x00\xC7'  # 192.168.0.199
protocol = 17  # UDP protocol number

# ----------------------------------------
# Step 2: Create UDP header and payload
# ----------------------------------------
udp_header = bytearray([
    0x1F, 0x90,  # Source port 8080
    0x00, 0x35,  # Destination port 53
    0x00, 0x15,  # Length (21 bytes: header + payload)
    0x00, 0x00   # Checksum (initially zero)
])

udp_payload = b'DNS query here!'  # Example UDP payload
udp_segment = udp_header + udp_payload
udp_length = len(udp_segment)

# ----------------------------------------
# Step 3: Build pseudo header and calculate checksum
# ----------------------------------------
pseudo_header = build_pseudo_header(src_ip, dst_ip, protocol, udp_length)
full_data = pseudo