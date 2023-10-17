from scapy.all import *
ip_packet = IP(src="10.0.1.26", dst="52.66.244.58")
tcp_packet = TCP(sport=25555,dport=80, flags=0)
packet = ip_packet/tcp_packet
num_packets = 10
for _ in range(num_packets):
    send(packet)