import hashlib

# Simulated routing table: defines which IPs are internal
INTERNAL_IPS = {"192.168.1.1", "192.168.1.2", "192.168.1.3"}

def is_internal(src_ip, dst_ip):
    """
    Determine if both source and destination IPs are internal.
    """
    return src_ip in INTERNAL_IPS and dst_ip in INTERNAL_IPS

def compute_checksum(payload):
    """
    Compute a SHA-256 checksum of the payload.
    """
    return hashlib.sha256(payload.encode()).hexdigest()

def route_packet(src_ip, dst_ip, payload):
    """
    Simulate routing a packet with optional checksum logic.
    """
    print(f"\nRouting packet from {src_ip} to {dst_ip}")
    if is_internal(src_ip, dst_ip):
        checksum = compute_checksum(payload)
        print("✅ Internal traffic detected.")
        print(f"Payload: {payload}")
        print(f"Checksum applied: {checksum}")
        # Simulate verification
        verified = checksum == compute_checksum(payload)
        print(f"Checksum verification: {'Passed' if verified else 'Failed'}")
    else:
        print("🌐 External traffic detected.")
        print(f"Payload: {payload}")
        print("No checksum applied.")

# Example usage
route_packet("192.168.1.1", "192.168.1.2", "Sensitive internal data")
route_packet("192.168.1.1", "8.8.8.8", "Outbound DNS query")
