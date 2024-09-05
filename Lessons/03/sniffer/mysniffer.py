from scapy.packet import Packet   # Import the base Packet class
from scapy.layers.inet import IP  # Import the IP layer
from scapy.sendrecv import sniff  # Import the sniff function

# Initialize a global variable to count the number of TCP packets read
iPkt: int = 0

# Define a function to process each captured packet
def process_packet(pkt: 'Packet'):
    # Use the global variable iPkt within the function
    global iPkt
    
    # Increment the packet count by 1
    iPkt += 1
    
    # Print a message showing the number of TCP packets read
    print(f"I've read a TCP packet on your PC: {iPkt} {type(pkt)}")

    # Check if the packet contains an IP layer, return if it doesn't
    if not pkt.haslayer(IP):
        return
    
    # Extract the source and destination IP addresses and the protocol, then store them in a string
    ip_layer = "IP_SRC: " + pkt[IP].src + " IP_DST: " + pkt[IP].dst + " PROTO: " + str(pkt[IP].proto)
    
    # Print the IP source, destination, and protocol information
    print(ip_layer)

# Start sniffing TCP packets on the "eth0" interface and call process_packet on each captured packet
sniff(iface="eth0", filter="tcp", prn=process_packet)
