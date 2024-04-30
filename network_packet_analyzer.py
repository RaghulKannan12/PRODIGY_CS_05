from scapy.all import sniff

def packet_callback(packet):
    if packet.haslayer("IP"):
        src_ip = packet["IP"].src
        dst_ip = packet["IP"].dst
        protocol = packet["IP"].proto
        payload_data = packet.payload
        print(f"Source IP: {src_ip}, Destination IP: {dst_ip}, Protocol: {protocol}, Payload Data: {payload_data}")

def main():
    print("Packet Sniffer started...")
    sniff(prn=packet_callback, store=False)

if __name__ == "__main__":
    main()
