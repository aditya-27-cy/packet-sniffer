# Network Packet Sniffer

A Python-based command-line network packet sniffer that captures and logs 
live network traffic using the Scapy library.

## Features
- Captures live TCP, UDP, ICMP and other network packets
- Displays source IP, destination IP and port numbers in real time
- Filter packets by protocol (tcp/udp/icmp or all)
- Logs all captured packets to a timestamped text file (packet_log.txt)
- Choose how many packets to capture

## Tech Used
- Python 3
- `scapy` library
- `datetime` module (built-in)

## Requirements

Install Scapy:
   pip install scapy

## How to Run

Important: Must be run as Administrator on Windows

1. Clone the repository
   git clone https://github.com/aditya-27-cy/packet-sniffer

2. Navigate to the folder
   cd packet-sniffer

3. Run as Administrator in PowerShell
   python packet_sniffer.py

4. Enter number of packets to capture and protocol filter when prompted

## Sample Output

=== Network Packet Sniffer ===
Protocols: tcp, udp, icmp, or press Enter for all

How many packets to capture [default 20]: 20
Filter by protocol (tcp/udp/icmp or Enter for all):

[*] Starting packet sniffer...
[*] Capturing 20 packets
[*] Filter: All protocols
[*] Logging to: packet_log.txt
--------------------------------------------------
TCP | 23.209.224.40 → 192.168.31.35 | Port 443 → 64867
UDP | 192.168.1.5 → 8.8.8.8 | Port 52341 → 53
--------------------------------------------------
[*] Capture complete. Results saved to packet_log.txt

## Ethical Note
This tool is intended for educational purposes only. Only run this 
on your own machine and network. Do not use it to intercept traffic 
on networks you do not own or have permission to monitor. Unauthorized 
packet sniffing is illegal.

## Author
Aditya Ramesh Warrier — Dayananda Sagar University, B.Tech Cyber Security<img width="1125" height="645" alt="Screenshot (48)" src="https://github.com/user-attachments/assets/c019b8a3-c630-4d4c-8239-69f80d6c27c6" />
<img width="1920" height="1080" alt="Screenshot (47)" src="https://github.com/user-attachments/assets/bc2b2a3c-6f4a-462c-95c3-4bf3f9e56fe2" />
