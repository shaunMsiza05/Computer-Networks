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
# Step 1: Create a mock IPv4 header
# ----------------------------------------
# This is a simplified 20-byte IPv4 header (no options)
# Checksum field is initially set to zero
ipv4_header = bytearray([
    0x45, 0x00,             # Version + IHL, Type of Service
    0x00, 0x54,             # Total Length
    0x00, 0x00,             # Identification
    0x40, 0x00,             # Flags + Fragment Offset
    0x40, 0x01,             # TTL, Protocol (ICMP = 1)
    0x00, 0x00,             # Header Checksum (initially zero)
    0xC0, 0xA8, 0x00, 0x01, # Source IP: 192.168.0.1
    0xC0, 0xA8, 0x00, 0xC7  # Destination IP: 192.168.0.199
])

# ----------------------------------------
# Step 2: Calculate checksum for the header
# ----------------------------------------
ipv4_checksum = checksum(ipv4_header)

# ----------------------------------------
# Step 3: Insert checksum into header
# ----------------------------------------
ipv4_header[10] = (ipv4_checksum >> 8) & 0xFF
ipv4_header[11] = ipv4_checksum & 0xFF

print(f"✅ Valid IPv4 Header Checksum: 0x{ipv4_checksum:04X}")

# ----------------------------------------
# Step 4: Simulate corruption by flipping a bit
# ----------------------------------------
corrupted_header = bytearray(ipv4_header)
corrupted_header[0] ^= 0x01  # Flip one bit in the first byte (Version/IHL)

# ----------------------------------------
# Step 5: Recalculate checksum on corrupted header
# ----------------------------------------
corrupted_checksum = checksum(corrupted_header)

# ----------------------------------------
# Step 6: Check if corrupted checksum is valid
# ----------------------------------------
is_valid = corrupted_checksum == 0x0000 or corrupted_checksum == 0xFFFF
print(f"❌ Corrupted IPv4 Checksum: 0x{corrupted_checksum:04X}")
print(f"Checksum Valid After Corruption: {is_valid}")
