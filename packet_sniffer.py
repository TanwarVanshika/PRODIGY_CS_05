from scapy.all import sniff, IP

def packet_callback(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        payload = bytes(packet[IP].payload)

        print(f"Source IP : {ip_src}")
        print(f"Destination IP : {ip_dst}")
        print(f"Protocol : {protocol}")
        print(f"Payload : {payload}")
        print("-" * 50)

#Capture Packets
sniff(prn=packet_callback, store=0, count=7, timeout=10)
 
