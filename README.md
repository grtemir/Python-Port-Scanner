# 🛡️ Python Network Recon Tool

A custom, lightweight port scanner and banner grabber tool built with Python.
This tool allows users to scan a target IP address for open ports, identify running service versions (Banner Grabbing), and log the results to a file automatically.

## 🚀 Features

* **Port Scanning:** Scans a user-defined range of ports using raw Sockets (TCP).
* **Banner Grabbing:** Automatically fetches service versions (e.g., Apache, OpenSSH) from open ports.
* **HTTP Awareness:** Sends specific payloads (`GET /`) to wake up HTTP servers (Port 80) for version detection.
* **Auto-Logging:** Saves all scan results, timestamps, and version details into `reports.txt`.
* **Flexible Interface:** Supports both command-line arguments and interactive mode for user input.
* **Smart Defaults:** Pre-configured to scan google.com ports 1-100 with sensible timeout settings.

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
    
    **Quick Start (with defaults):**
    Scan google.com ports 1-100 with 1 second timeout:
    ```bash
    python scanner.py
    ```
    
    **Custom Target and Port Range:**
    ```bash
    python scanner.py --target scanme.nmap.org --start-port 1 --end-port 1000 --timeout 2.0
    ```
    
    **Interactive Mode:**
    For the traditional interactive prompts:
    ```bash
    python scanner.py --interactive
    ```
    
    **Command-line Options:**
    - `--target` or `-t`: Target IP address or hostname (default: google.com)
    - `--timeout`: Connection timeout in seconds (default: 1.0)
    - `--start-port`: Starting port number (default: 1)
    - `--end-port`: Ending port number (default: 100)
    - `--interactive` or `-i`: Run in interactive mode
    - `--help` or `-h`: Show help message

## ⚠️ Disclaimer
This tool is created for **educational purposes only**. Use it only on networks/systems you own or have permission to scan (e.g., scanme.nmap.org). The author is not responsible for any misuse.
