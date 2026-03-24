from scapy.all import sniff, IP, TCP, UDP, ICMP
import sys
sys.stdout.reconfigure(encoding='utf-8')
from datetime import datetime

LOG_FILE = "packet_log.txt"

def log_packet(message: str):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {message}\n")

def process_packet(packet):
    if IP in packet:
        src_ip = packet[IP].src
        dst_ip = packet[IP].dst
        protocol = ""
        info = ""

        if TCP in packet:
            protocol = "TCP"
            src_port = packet[TCP].sport
            dst_port = packet[TCP].dport
            info = f"Port {src_port} → {dst_port}"

        elif UDP in packet:
            protocol = "UDP"
            src_port = packet[UDP].sport
            dst_port = packet[UDP].dport
            info = f"Port {src_port} → {dst_port}"

        elif ICMP in packet:
            protocol = "ICMP"
            info = f"Type {packet[ICMP].type}"

        else:
            protocol = "OTHER"
            info = ""

        message = f"{protocol} | {src_ip} → {dst_ip} | {info}"
        print(message)
        log_packet(message)

def start_sniffer(packet_count: int, filter_protocol: str):
    print(f"\n[*] Starting packet sniffer...")
    print(f"[*] Capturing {packet_count} packets")
    print(f"[*] Filter: {filter_protocol if filter_protocol else 'All protocols'}")
    print(f"[*] Logging to: {LOG_FILE}")
    print("-" * 50)

    sniff(
        filter=filter_protocol,
        prn=process_packet,
        count=packet_count,
        store=False
    )

    print("-" * 50)
    print(f"[*] Capture complete. Results saved to {LOG_FILE}")

if __name__ == "__main__":
    print("=== Network Packet Sniffer ===")
    print("Protocols: tcp, udp, icmp, or press Enter for all\n")

    count = input("How many packets to capture [default 20]: ").strip()
    count = int(count) if count.isdigit() else 20

    protocol = input("Filter by protocol (tcp/udp/icmp or Enter for all): ").strip().lower()

    start_sniffer(count, protocol)
