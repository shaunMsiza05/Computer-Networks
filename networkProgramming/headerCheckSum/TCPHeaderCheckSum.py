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
def build_pseudo_header(src_ip, dst_ip, protocol, tcp_length):
    """
    Constructs the pseudo header used in TCP checksum calculation.
    Includes source IP, destination IP, protocol number, and TCP length.
    """
    return struct.pack('!4s4sBBH', src_ip, dst_ip, 0, protocol, tcp_length)

# ----------------------------------------
# Step 1: Define IP addresses and protocol
# ----------------------------------------
src_ip = b'\xC0\xA8\x00\x01'  # 192.168.0.1
dst_ip = b'\xC0\xA8\x00\xC7'  # 192.168.0.199