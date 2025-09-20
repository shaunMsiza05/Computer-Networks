def calculate_checksum(header_bytes):
    """
    Calculate the IPv4 header checksum using one's complement addition.
    """
    if len(header_bytes) % 2 != 0:
        header_bytes += b'\x00'  # pad if odd length

    total = 0
    for i in range(0, len(header_bytes), 2):
        word = (header_bytes[i] << 8) + header_bytes[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)  # wrap around carry

    checksum = ~total & 0xFFFF
    return checksum

def verify_checksum(header_bytes):
    """
    Verify the checksum of an IPv4 header.
    """
    if len(header_bytes) % 2 != 0:
        header_bytes += b'\x00'

    total = 0
    for i in range(0, len(header_bytes), 2):
        word = (header_bytes[i] << 8) + header_bytes[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)

    return total == 0xFFFF

# 🧱 Example: 20-byte IPv4 header (checksum field set to 0 for calculation)
# This is just a mock header for illustration
mock_header = bytearray([
    0x45, 0x00, 0x00, 0x54,  # Version, IHL, TOS, Total Length
    0x00, 0x00, 0x40, 0x00,  # ID, Flags, Fragment Offset
    0x40, 0x01, 0x00, 0x00,  # TTL, Protocol, Checksum (initially 0)
    0xC0, 0xA8, 0x00, 0x01,  # Source IP: 192.168.0.1
    0xC0, 0xA8, 0x00, 0xC7   # Destination IP: 192.168.0.199
])

# Calculate checksum
checksum = calculate_checksum(mock_header)
print(f"Calculated Checksum: 0x{checksum:04X}")

# Insert checksum into header
mock_header[10] = (checksum >> 8) & 0xFF
mock_header[11] = checksum & 0xFF

# Verify checksum
is_valid = verify_checksum(mock_header)
print(f"Checksum Valid: {is_valid}")
def calculate_checksum(header_bytes):
    """
    Calculate the IPv4 header checksum using one's complement addition.
    """
    if len(header_bytes) % 2 != 0:
        header_bytes += b'\x00'  # pad if odd length

    total = 0
    for i in range(0, len(header_bytes), 2):
        word = (header_bytes[i] << 8) + header_bytes[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)  # wrap around carry

    checksum = ~total & 0xFFFF
    return checksum

def verify_checksum(header_bytes):
    """
    Verify the checksum of an IPv4 header.
    """
    if len(header_bytes) % 2 != 0:
        header_bytes += b'\x00'

    total = 0
    for i in range(0, len(header_bytes), 2):
        word = (header_bytes[i] << 8) + header_bytes[i + 1]
        total += word
        total = (total & 0xFFFF) + (total >> 16)

    return total == 0xFFFF

# 🧱 Example: 20-byte IPv4 header (checksum field set to 0 for calculation)
# This is just a mock header for illustration
mock_header = bytearray([
    0x45, 0x00, 0x00, 0x54,  # Version, IHL, TOS, Total Length
    0x00, 0x00, 0x40, 0x00,  # ID, Flags, Fragment Offset
    0x40, 0x01, 0x00, 0x00,  # TTL, Protocol, Checksum (initially 0)
    0xC0, 0xA8, 0x00, 0x01,  # Source IP: 192.168.0.1
    0xC0, 0xA8, 0x00, 0xC7   # Destination IP: 192.168.0.199
])

# Calculate checksum
checksum = calculate_checksum(mock_header)
print(f"Calculated Checksum: 0x{checksum:04X}")

# Insert checksum into header
mock_header[10] = (checksum >> 8) & 0xFF
mock_header[11] = checksum & 0xFF

# Verify checksum
is_valid = verify_checksum(mock_header)
print(f"Checksum Valid: {is_valid}")
