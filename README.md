# 🔍 Network Scanner – Python Project

## 📖 Overview

This project is a **Python-based network scanner** that identifies active devices connected to a **local network** using **ARP (Address Resolution Protocol)**.  
It displays the **IP address**, **MAC address**, and **hostname** of each discovered device in a neat table format.

---

## 🎯 Objectives

- Detect all live hosts on a local network (e.g., your Wi-Fi).
- Display each device's IP, MAC address, and hostname.
- Practice ethical network reconnaissance techniques using Python.
- Learn multithreading and packet-level communication with Scapy.

---

## 🛠️ Technologies Used

| Library       | Purpose                               |
|---------------|----------------------------------------|
| `scapy`       | Sends ARP requests to find devices     |
| `socket`      | Resolves IPs to hostnames              |
| `ipaddress`   | Parses CIDR notation and IP ranges     |
| `threading`   | Runs parallel scans for faster results |
| `queue`       | Collects results from all threads      |

---

## 🚀 How It Works

1. You input your local network’s CIDR range (e.g., `192.168.1.0/24`).
2. The script generates a list of all IPs in that range.
3. Each IP is scanned using an ARP request to check if it’s alive.
4. If the IP responds, its MAC address and hostname are collected.
5. Results are shown in a clean table format.

---

## 📦 Requirements

- Python 3.x
- Admin/root privileges (for sending ARP packets)
- Required Python packages:
  
```bash
pip install scapy
