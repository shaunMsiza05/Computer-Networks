import random
import time

class ReliableIP:
    def __init__(self):
        self.sent_packets = {}
        self.received_packets = {}

    def send_packet(self, src, dst, payload, seq_num):
        """
        Simulate sending a packet with reliability features.
        """
        print(f"\n📤 Sending packet #{seq_num} from {src} to {dst}")
        packet = {
            "src": src,
            "dst": dst,
            "seq": seq_num,
            "payload": payload
        }

        # Simulate unreliable delivery (10% chance of loss)
        if random.random() < 0.9:
            self.sent_packets[seq_num] = packet
            print(f"✅ Packet #{seq_num} delivered.")
            self.receive_packet(packet)
        else:
            print(f"❌ Packet #{seq_num} lost in transit.")
            self.retransmit_packet(src, dst, payload, seq_num)

    def retransmit_packet(self, src, dst, payload, seq_num):
        """
        Retry sending the packet after a delay.
        """
        print(f"🔁 Retransmitting packet #{seq_num}...")
        time.sleep(1)
        self.send_packet(src, dst, payload, seq_num)

    def receive_packet(self, packet):
        """
        Simulate receiving and acknowledging a packet.
        """
        seq = packet["seq"]
        print(f"📥 Received packet #{seq} at {packet['dst']}")
        self.received_packets[seq] = packet["payload"]
        self.send_ack(packet["src"], seq)

    def send_ack(self, dst, seq_num):
        """
        Simulate sending an acknowledgment.
        """
        print(f"📨 ACK sent to {dst} for packet #{seq_num}")

# Example usage
ip = ReliableIP()
ip.send_packet("192.168.1.10", "192.168.1.20", "Hello, world!", seq_num=1)
ip.send_packet("192.168.1.10", "192.168.1.20", "This is reliable IP!", seq_num=2)
