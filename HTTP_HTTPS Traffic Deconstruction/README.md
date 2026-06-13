# 🔐 HTTP/HTTPS Traffic Deconstruction

> **A hands-on cybersecurity lab for capturing, parsing, and analyzing web traffic**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![tcpdump](https://img.shields.io/badge/tcpdump-Packet%20Capture-003366?style=for-the-badge&logo=wireshark&logoColor=white)
![OpenSSL](https://img.shields.io/badge/OpenSSL-TLS%20Analysis-721412?style=for-the-badge&logo=openssl&logoColor=white)
![curl](https://img.shields.io/badge/curl-HTTP%20Client-073551?style=for-the-badge&logo=curl&logoColor=white)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- 📡 **Capture and analyze** HTTP/HTTPS traffic using command-line tools
- 🧩 **Parse HTTP headers** and identify request/response components
- 🚨 **Detect suspicious patterns** and anomalies in web traffic
- 🔒 **Analyze HTTPS metadata** and connection characteristics
- 🤖 **Create automated scripts** for traffic analysis
- 🛡️ **Apply traffic analysis techniques** for security monitoring

---

## 📋 Prerequisites

| Skill | Level |
|-------|-------|
| TCP/IP & Networking Concepts | Basic |
| Linux Command Line | Familiar |
| HTTP/HTTPS Protocols | Knowledgeable |
| Bash / Python Scripting | Basic |
| Text Processing (`grep`, `awk`, `sed`) | Basic |

---

## 🖥️ Lab Environment

> 💡 Al Nafi provides ready-to-use **Linux-based cloud machines** for this lab.
> Click **Start Lab** to access your pre-configured environment with all necessary tools installed.

---

## 🗂️ Lab Structure

```
http_analysis_lab/
├── 📄 index.html              # Test HTML file
├── 📦 http_traffic.pcap       # Captured HTTP traffic
├── 📝 http_requests.txt       # Extracted HTTP requests
├── 🐍 http_parser.py          # HTTP Parser Script
├── 📝 test_requests.txt       # Sample attack pattern data
├── 🐍 https_analyzer.py       # HTTPS Flow Analyzer
├── 📊 https_flows.pcap        # Captured HTTPS traffic
├── 🔧 analyze_cert.sh         # SSL Certificate Analyzer
├── ⏱️ timing_analysis.sh      # Connection Timing Script
└── 📁 traffic_logs/           # Monitoring output logs
```

---

# 🧪 Task 1: HTTP Traffic Capture and Analysis

---

## ⚙️ Step 1 — Set Up the Lab Environment

> 🏗️ *Create your working directory and spin up a test HTTP server.*

```bash
mkdir ~/http_analysis_lab && cd ~/http_analysis_lab

# ✍️ Create a simple test HTML file
cat > index.html << 'EOF'
<!DOCTYPE html>
<html>
<head><title>HTTP Analysis Lab</title></head>
<body><h1>Test Server</h1></body>
</html>
EOF

# 🚀 Start HTTP server on port 8080
python3 -m http.server 8080 &
SERVER_PID=$!
echo "Server started with PID: $SERVER_PID"
```

---

## 📡 Step 2 — Capture HTTP Traffic

> 🎯 *Start packet capture and generate test HTTP traffic including attack patterns.*

```bash
# 🟢 Start capturing on loopback interface
sudo tcpdump -i lo -w http_traffic.pcap port 8080 &
TCPDUMP_PID=$!

# ⏳ Wait for tcpdump to initialize
sleep 2

# 🌐 Generate various HTTP requests
curl -v http://localhost:8080/
curl -v -H "User-Agent: TestBot/1.0" http://localhost:8080/
curl -v -X POST -d "username=admin&password=test" http://localhost:8080/login
curl -v http://localhost:8080/../../etc/passwd
curl -v "http://localhost:8080/search?q=<script>alert('xss')</script>"

# 🔴 Stop capture
sleep 2
sudo kill $TCPDUMP_PID
```

> ⚠️ **Note:** The last two requests simulate **path traversal** and **XSS** attacks for detection practice.

---

## 🔍 Step 3 — Extract and Analyze HTTP Requests

> 🧠 *Convert captured traffic to a human-readable format and extract key information.*

```bash
# 📤 Extract HTTP requests from pcap file
tcpdump -r http_traffic.pcap -A -s 0 > http_requests.txt

# 📋 View HTTP methods used
grep -E "^(GET|POST|PUT|DELETE)" http_requests.txt

# 🕵️ Extract User-Agent headers
grep -i "user-agent:" http_requests.txt

# 📊 Count request types
grep -E "^(GET|POST)" http_requests.txt | awk '{print $1}' | sort | uniq -c
```

---

## 🐍 Step 4 — Create HTTP Parser Script

> 🛠️ *Build a Python script to parse and analyze HTTP traffic. Complete the `TODO` sections.*

```python
#!/usr/bin/env python3
"""
HTTP Traffic Parser and Analyzer
Students: Complete the TODO sections to implement full functionality
"""

import re
import sys
from collections import defaultdict

class HTTPParser:
    def __init__(self):
        self.suspicious_patterns = {
            'sql_injection': [r'union\s+select', r'drop\s+table', r"'.*or.*'"],
            'xss': [r'<script>', r'javascript:', r'onerror='],
            'path_traversal': [r'\.\./', r'%2e%2e'],
            'command_injection': [r';\s*(cat|ls|whoami)', r'\|.*\|']
        }
    
    def parse_request(self, request_text):
        """
        Parse HTTP request into components.
        Returns: Dictionary with method, path, version, and headers
        """
        # TODO: Split request into lines
        # TODO: Extract method, path, and HTTP version from first line
        # TODO: Parse headers from remaining lines
        # TODO: Return structured dictionary
        pass
    
    def detect_anomalies(self, parsed_request):
        """
        Detect suspicious patterns in HTTP request.
        Returns: List of detected anomalies
        """
        anomalies = []
        # TODO: Check path against suspicious patterns
        # TODO: Validate User-Agent header
        # TODO: Check for suspicious headers (X-Forwarded-For, etc.)
        # TODO: Detect unusual request characteristics
        return anomalies
    
    def generate_report(self, requests):
        """
        Generate analysis report for all requests.
        """
        # TODO: Parse all requests
        # TODO: Count methods, detect anomalies
        # TODO: Print formatted report with statistics
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 http_parser.py <input_file>")
        sys.exit(1)
    # TODO: Read input file
    # TODO: Split into individual requests
    # TODO: Create parser instance and generate report
    pass

if __name__ == "__main__":
    main()
```

```bash
# 🔑 Save as http_parser.py and make executable
chmod +x http_parser.py
```

---

## 🧪 Step 5 — Create Sample Data and Test

> 📝 *Create test data with various attack patterns and run your parser.*

```bash
# 📄 Create test request file with attack patterns
cat > test_requests.txt << 'EOF'
GET / HTTP/1.1
Host: localhost:8080
User-Agent: Mozilla/5.0

POST /login HTTP/1.1
Host: localhost:8080
User-Agent: AttackBot/1.0
Content-Length: 50

GET /admin' OR '1'='1 HTTP/1.1
Host: localhost:8080

GET /../../../etc/passwd HTTP/1.1
Host: localhost:8080
X-Forwarded-For: 10.0.0.1
EOF

# ▶️ Test your parser implementation
python3 http_parser.py test_requests.txt
```

> 🔎 **Attack patterns included:**
> - 🗄️ SQL Injection: `' OR '1'='1`
> - 📁 Path Traversal: `/../../../etc/passwd`
> - 🤖 Suspicious Bot Agent: `AttackBot/1.0`

---

# 🔒 Task 2: HTTPS Metadata Analysis

---

## 🔏 Step 1 — Analyze SSL/TLS Certificates

> 🏅 *Examine certificate issuer, subject, validity, and TLS version.*

```bash
cat > analyze_cert.sh << 'EOF'
#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <hostname>"
    exit 1
fi

HOSTNAME=$1

echo "🔐 Analyzing SSL certificate for: $HOSTNAME"
echo "========================================"

# 📜 Retrieve and display certificate information
echo | openssl s_client -connect $HOSTNAME:443 -servername $HOSTNAME 2>/dev/null | \
openssl x509 -noout -text | grep -E "(Issuer:|Subject:|Not After)"

# 🔑 Check TLS version and cipher
echo | openssl s_client -connect $HOSTNAME:443 -servername $HOSTNAME 2>&1 | \
grep -E "(Protocol|Cipher)"
EOF

chmod +x analyze_cert.sh
```

```bash
# 🌐 Test with various domains
./analyze_cert.sh www.google.com
./analyze_cert.sh github.com
```

---

## ⏱️ Step 2 — Analyze Connection Timing

> 📊 *Measure HTTPS connection characteristics including DNS, TCP, and TLS timing.*

```bash
cat > timing_analysis.sh << 'EOF'
#!/bin/bash

URL=$1

if [ -z "$URL" ]; then
    echo "Usage: $0 <url>"
    exit 1
fi

echo "⏱️  Connection Timing Analysis for: $URL"
echo "===================================="

curl -w "\n\
DNS Lookup:        %{time_namelookup}s\n\
TCP Connect:       %{time_connect}s\n\
TLS Handshake:     %{time_appconnect}s\n\
Server Processing: %{time_starttransfer}s\n\
Total Time:        %{time_total}s\n\
Download Size:     %{size_download} bytes\n\
HTTP Code:         %{http_code}\n" \
-o /dev/null -s "$URL"
EOF

chmod +x timing_analysis.sh
```

```bash
# ▶️ Test timing analysis
./timing_analysis.sh https://www.google.com
./timing_analysis.sh https://httpbin.org/delay/2
```

---

## 🐍 Step 3 — Create HTTPS Flow Analyzer

> 🔬 *Develop a comprehensive Python script for HTTPS analysis. Complete the `TODO` sections.*

```python
#!/usr/bin/env python3
"""
HTTPS Traffic Flow Analyzer
Students: Implement the TODO sections
"""

import subprocess
import json
import re
from urllib.parse import urlparse

class HTTPSAnalyzer:
    def __init__(self):
        self.suspicious_domains = ['bit.ly', 'tinyurl.com', 'pastebin.com']
    
    def check_certificate(self, hostname):
        """
        Retrieve and analyze SSL certificate.
        Returns: Dictionary with certificate details
        """
        # TODO: Use openssl to retrieve certificate
        # TODO: Parse issuer, subject, validity dates
        # TODO: Check for self-signed certificates
        # TODO: Return structured data
        pass
    
    def analyze_tls_handshake(self, hostname):
        """
        Analyze TLS handshake characteristics.
        Returns: Dictionary with TLS version, cipher, etc.
        """
        # TODO: Connect and capture handshake details
        # TODO: Extract TLS version and cipher suite
        # TODO: Check for weak ciphers
        pass
    
    def check_domain_reputation(self, domain):
        """
        Assess domain reputation and characteristics.
        Returns: Risk assessment dictionary
        """
        risk_score = 0
        flags = []
        # TODO: Check against suspicious domain list
        # TODO: Analyze domain length and structure
        # TODO: Check for IP addresses instead of domains
        # TODO: Calculate risk score
        return {'risk_score': risk_score, 'flags': flags}
    
    def measure_connection_timing(self, url):
        """
        Measure various connection timing metrics.
        Returns: Dictionary with timing measurements
        """
        # TODO: Use curl to measure timing
        # TODO: Calculate SSL handshake time
        # TODO: Identify timing anomalies
        pass
    
    def generate_report(self, urls):
        """
        Generate comprehensive analysis report.
        """
        # TODO: Analyze each URL
        # TODO: Compile statistics
        # TODO: Print formatted report
        pass

def main():
    analyzer = HTTPSAnalyzer()
    test_urls = [
        'https://www.google.com',
        'https://github.com',
        'https://httpbin.org/get'
    ]
    # TODO: Accept URLs from command line
    # TODO: Run analysis
    # TODO: Display results
    pass

if __name__ == "__main__":
    main()
```

> 💾 Save as `https_analyzer.py` and make it executable.

---

## 📦 Step 4 — Capture and Analyze HTTPS Flows

> 🌊 *Capture real HTTPS traffic and analyze flow patterns and packet sizes.*

```bash
# 🟢 Capture HTTPS traffic (port 443) for 30 seconds
sudo timeout 30 tcpdump -i any -w https_flows.pcap port 443 &

# 🌐 Generate HTTPS traffic during capture
sleep 2
curl -s https://www.google.com > /dev/null
curl -s https://github.com > /dev/null
curl -s https://httpbin.org/get > /dev/null

# ⏳ Wait for capture to complete
wait

# 🔍 Analyze captured flows
tcpdump -r https_flows.pcap -n | head -20
```

```bash
# 📊 Count unique HTTPS destinations
tcpdump -r https_flows.pcap -n 2>/dev/null | \
grep -E "\.443" | \
awk '{print $3, $5}' | \
sort | uniq -c | sort -rn

# 📐 Analyze packet sizes
tcpdump -r https_flows.pcap -n 2>/dev/null | \
grep -oP 'length \K[0-9]+' | \
awk '{sum+=$1; count++} END {print "Average packet size:", sum/count, "bytes"}'
```

---

# 🤖 Task 3: Automated Traffic Monitoring

---

## 🖥️ Step 1 — Create Real-Time Monitoring Script

> 🔄 *Build a bash script for continuous HTTP/HTTPS traffic monitoring. Complete the `TODO` sections.*

```bash
#!/bin/bash
# 📡 Real-time HTTP/HTTPS Traffic Monitor
# Students: Complete the TODO sections

INTERFACE="any"
DURATION=60
OUTPUT_DIR="./traffic_logs"

# TODO: Create output directory if it doesn't exist

monitor_http_traffic() {
    echo "👁️  Monitoring HTTP traffic..."
    # TODO: Capture HTTP traffic (port 80)
    # TODO: Extract and log suspicious patterns
    # TODO: Generate alerts for anomalies
}

monitor_https_traffic() {
    echo "🔒 Monitoring HTTPS traffic..."
    # TODO: Capture HTTPS metadata (port 443)
    # TODO: Log connection attempts
    # TODO: Track unusual destinations
}

analyze_patterns() {
    # TODO: Parse captured traffic
    # TODO: Identify attack patterns
    # TODO: Generate summary report
}

# TODO: Implement main monitoring loop
# TODO: Call monitoring functions
# TODO: Generate periodic reports
```

---

## 🚨 Step 2 — Create Alert System

> 🔔 *Implement an automated alert system for suspicious traffic patterns.*

```python
#!/usr/bin/env python3
"""
Traffic Alert System
Students: Implement alert logic
"""

class TrafficAlertSystem:
    def __init__(self):
        self.alert_threshold = {
            'sql_injection': 1,
            'xss': 1,
            'path_traversal': 1,
            'unusual_user_agent': 3
        }
    
    def check_alerts(self, analysis_results):
        """
        Check if alerts should be triggered.
        Returns: List of alerts to trigger
        """
        # TODO: Compare results against thresholds
        # TODO: Generate alert messages
        # TODO: Return list of alerts
        pass
    
    def send_alert(self, alert_message):
        """
        Send alert notification.
        """
        # TODO: Log alert to file
        # TODO: Print to console
        # TODO: (Optional) Send email/webhook notification
        pass

# TODO: Implement main function to process traffic and trigger alerts
```

---

# ✅ Expected Outcomes

After completing this lab, you should have:

| # | Outcome |
|---|---------|
| 🟢 1 | Captured and analyzed HTTP/HTTPS traffic using `tcpdump` and `curl` |
| 🟢 2 | Created functional parsers to extract and analyze HTTP headers |
| 🟢 3 | Implemented anomaly detection for common web attacks |
| 🟢 4 | Analyzed HTTPS metadata including certificates and timing |
| 🟢 5 | Developed automated monitoring scripts for traffic analysis |
| 🟢 6 | Gained practical experience in network security monitoring |

---

# 🛠️ Troubleshooting Tips

| ❌ Issue | ✅ Solution |
|---------|------------|
| 🚫 Permission denied when running `tcpdump` | Use `sudo` with tcpdump commands or add user to `pcap` group |
| 🐍 Python script not finding modules | Ensure Python 3 is installed and scripts use `#!/usr/bin/env python3` |
| 📭 No traffic captured in pcap file | Verify correct interface with `ip addr` and ensure traffic is generated during capture |
| 🔐 OpenSSL certificate retrieval fails | Check network connectivity and firewall rules; some hosts may block queries |
| ⚡ HTTP server port already in use | Use a different port or kill existing: `kill $(lsof -t -i:8080)` |

---

# 🎓 Conclusion

This lab provided hands-on experience with **HTTP/HTTPS traffic analysis** — a critical skill for cybersecurity professionals.

You learned to:
- 📡 Capture network traffic
- 🧩 Parse HTTP requests
- 🚨 Detect attack patterns
- 🔒 Analyze encrypted traffic metadata

> 💡 These techniques form the foundation for **network security monitoring**, **intrusion detection**, and **incident response**.

Continue practicing with real-world traffic captures and expand your scripts to handle more complex scenarios.

---

<div align="center">

![Security](https://img.shields.io/badge/Security-Monitoring-red?style=for-the-badge&logo=hackthebox&logoColor=white)
![Network](https://img.shields.io/badge/Network-Analysis-blue?style=for-the-badge&logo=cisco&logoColor=white)
![Lab](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Lab-green?style=for-the-badge&logo=academia&logoColor=white)

**Made with ❤️ for Cybersecurity Learners**

</div>
