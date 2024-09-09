from scapy.packet import Packet        # Import the base Packet class
from scapy.layers.inet import IP, TCP  # Import the IP and TCP layers
from scapy.sendrecv import sniff       # Import the sniff function

class PacketSniffer:
    def __init__(self):
        # Initialize packet counter
        self.packet_count = 0
        
    def process_packet(self, pkt: Packet):
        """Process each captured packet."""
        self.packet_count += 1
        print(f"I've read a packet on your PC: {self.packet_count}")

        # Check if the packet contains an IP layer
        if not pkt.haslayer(IP):
            return

        # Check if the packet contains a TCP layer
        if pkt.haslayer(TCP):
            # Extract TCP source and destination ports
            tcp_info = f"TCP_SPORT: {pkt[TCP].sport} - TCP_DPORT: {pkt[TCP].dport}"
            print(tcp_info)

            # Check if the packet is HTTP or HTTPS (TLS)
            if pkt[TCP].sport == 80 or pkt[TCP].dport == 80:
                direction = "response" if pkt[TCP].sport == 80 else "request"
                print(f"It's an HTTP {direction}\n")
            elif pkt[TCP].sport == 443 or pkt[TCP].dport == 443:
                print("It's an HTTPS (TLS) packet\n")
        else:
            # Extract IP information if no TCP layer is found
            ip_info = f"IP_SRC: {pkt[IP].src} - IP_DST: {pkt[IP].dst} - PROTO: {pkt[IP].proto} - IP_LEN: {pkt[IP].len}"
            print(ip_info)

    def start_sniffing(self, iface="eth0", filter="tcp"):
        """Start sniffing TCP packets on the specified interface."""
        sniff(iface=iface, filter=filter, prn=self.process_packet)

# Create an instance of PacketSniffer and start sniffing
sniffer = PacketSniffer()
sniffer.start_sniffing()
