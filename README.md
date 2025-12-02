# 🛡️ Python Network Recon Tool

A custom, lightweight port scanner and banner grabber tool built with Python.
This tool allows users to scan a target IP address for open ports, identify running service versions (Banner Grabbing), and log the results to a file automatically.

## 🚀 Features

* **Port Scanning:** Scans a user-defined range of ports using raw Sockets (TCP).
* **Banner Grabbing:** Automatically fetches service versions (e.g., Apache, OpenSSH) from open ports.
* **HTTP Awareness:** Sends specific payloads (`GET /`) to wake up HTTP servers (Port 80) for version detection.
* **Auto-Logging:** Saves all scan results, timestamps, and version details into `reports.txt`.
* **User Friendly:** Target IP, Port Range, and Timeout settings are taken dynamically from the user.

## 🛠️ Installation & Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/grtemir/Python-Port-Scanner.git](https://github.com/grtemir/Python-Port-Scanner.git)
    ```

2.  **Navigate to the directory:**
    ```bash
    cd Python-Port-Scanner
    ```

3.  **Run the tool:**
    ```bash
    python scanner.py
    ```

## ⚠️ Disclaimer
This tool is created for **educational purposes only**. Use it only on networks/systems you own or have permission to scan (e.g., scanme.nmap.org). The author is not responsible for any misuse.
