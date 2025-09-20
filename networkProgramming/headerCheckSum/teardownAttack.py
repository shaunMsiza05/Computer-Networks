# Fragment offset is in units of 8 bytes
class Fragment:
    def __init__(self, offset_units, data, more_fragments):
        self.offset = offset_units * 8  # Convert to byte offset
        self.data = data
        self.more_fragments = more_fragments

def reassemble_fragments(fragments):
    buffer = {}
    for frag in fragments:
        for i in range(len(frag.data)):
            pos = frag.offset + i
            if pos in buffer:
                print(f"⚠️ Overlap detected at byte offset {pos}")
            buffer[pos] = frag.data[i]
    message = ''.join(buffer[i] for i in sorted(buffer))
    print(f"\n✅ Reassembled message: {message}")

# Simulated fragments with actual overlap
fragment1 = Fragment(offset_units=0, data="ABCDEFGH", more_fragments=True)  # Bytes 0–7
fragment2 = Fragment(offset_units=1, data="12345678", more_fragments=False) # Bytes 8–15
fragment3 = Fragment(offset_units=0, data="XXXX", more_fragments=True)      # Bytes 0–3 (overlaps)

reassemble_fragments([fragment1, fragment2, fragment3])
