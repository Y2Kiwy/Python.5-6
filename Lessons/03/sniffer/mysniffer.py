from scapy.packet import Packet        # Import the base Packet class
from scapy.layers.inet import IP, TCP  # Import the IP and TCP layers
from scapy.sendrecv import sniff       # Import the sniff function

# Initialize a global variable to count the number of TCP packets processed
iPkt: int = 0

# Define a function to process each captured packet
def process_packet(pkt: Packet):
    # Use the global variable iPkt within the function
    global iPkt
    
    # Increment the packet count by 1
    iPkt += 1
    
    # Print a message showing the number of TCP packets read
    print(f"I've read a packet on your PC: {iPkt}")

    # Check if the packet contains an IP layer; return if it doesn't
    if not pkt.haslayer(IP):
        return

    # Check if the packet contains a TCP layer
    if pkt[IP].proto == 6:
        # Extract TCP source and destination ports and store them in a string
        tcp_layer: str = f"TCP_SPORT: {pkt[TCP].sport} - TCP_DPORT: {pkt[TCP].dport}"

        # Print the TCP source and destination ports
        print(tcp_layer)

        # Check if the packet is HTTP
        if pkt[IP].sport == 80 or pkt[IP].dport == 80:
            print("It's an HTTP packet\n")
        
        # Check if the packet is HTTPS (TLS)
        elif pkt[IP].sport == 443 or pkt[IP].dport == 443:
            print("It's an HTTPS (TLS) packet\n")

        else:
            print()

    else:
        # Extract IP source and destination addresses and protocol information, then store them in a string
        ip_layer: str = f"IP_SRC: {pkt[IP].src} - IP_DST: {pkt[IP].dst} - PROTO: {pkt[IP].proto} - IP_LEN: {pkt[IP].len}\n"

        # Print the IP source, destination, protocol, and length information
        print(ip_layer)

# Start sniffing TCP packets on the "eth0" interface and call process_packet for each captured packet
sniff(iface="eth0", filter="tcp", prn=process_packet)
