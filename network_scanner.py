import scapy.all as scapy
import socket
import ipaddress
import threading
from queue import Queue

result_queue = Queue()

def scan(ip, result_queue):
    arp = scapy.ARP(pdst=str(ip))
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp
    result = scapy.srp(packet, timeout=1, verbose=False)[0]

    for sent, received in result:
        try:
            hostname = socket.gethostbyaddr(received.psrc)[0]
        except socket.herror:
            hostname = "Unknown"
        result_queue.put({
            "ip": received.psrc,
            "mac": received.hwsrc,
            "hostname": hostname
        })

def print_result():
    print(f"{'IP':<20}{'MAC Address':<20}{'Hostname'}")
    print("-" * 60)
    while not result_queue.empty():
        r = result_queue.get()
        print(f"{r['ip']:<20}{r['mac']:<20}{r['hostname']}")

def main():
    cidr = input("Enter the CIDR range (e.g. 192.168.1.0/24): ")
    network = ipaddress.ip_network(cidr, strict=False)

    threads = []
    for ip in network.hosts():
        t = threading.Thread(target=scan, args=(ip, result_queue))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print_result()

if __name__ == "__main__":
    main()
