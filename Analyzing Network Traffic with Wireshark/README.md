# 🦈 Analyzing Network Traffic with Wireshark 

![Wireshark](https://img.shields.io/badge/Wireshark-Network%20Analysis-1679A7?style=for-the-badge&logo=wireshark&logoColor=white)
![TShark](https://img.shields.io/badge/TShark-CLI%20Capture-blue?style=for-the-badge&logo=wireshark&logoColor=white)
![DNS](https://img.shields.io/badge/DNS-Traffic%20Analysis-orange?style=for-the-badge&logo=cloudflare&logoColor=white)
![TLS](https://img.shields.io/badge/TLS%2FSSL-Security%20Audit-green?style=for-the-badge&logo=letsencrypt&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🔧 Install and configure **Wireshark** on a Linux system
- 📡 Capture **live network traffic** using Wireshark
- 🔍 Analyze **DNS traffic** to identify potential security threats
- 🌐 Examine **HTTP communications** for suspicious activities
- 🔒 Investigate **TLS/SSL traffic** for anomalies and security issues
- 🎯 Apply **packet filtering techniques** to isolate specific traffic types
- 🚨 Identify common **network attack patterns** and malicious activities
- 📊 Generate comprehensive **network traffic analysis reports**

---

## ✅ Prerequisites

| Requirement | Description |
|---|---|
| 🌐 Networking | Basic understanding of TCP/IP, DNS, HTTP, HTTPS |
| 🖥️ Linux CLI | Familiarity with Linux command line interface |
| 🛡️ Security | Knowledge of basic cybersecurity principles |
| 📦 Protocols | Understanding of network protocols and packet structure |
| 💻 Terminal | Basic familiarity with terminal operations in Linux |

---

## 🧪 Lab Environment

> 💡 **Al Nafi** provides Linux-based cloud machines for this lab.  
> Click **Start Lab** to access your pre-configured environment.  
> No need to build your own VM or install additional software.

**🛠️ Your cloud machine includes:**

| Component | Details |
|---|---|
| 🐧 OS | Ubuntu 22.04 LTS |
| 📡 Network | Interface configured for packet capture |
| 🌐 Connectivity | Internet access for generating traffic |
| 🔑 Permissions | All permissions for network monitoring pre-configured |

---

# 📋 Task 1 — Installing and Configuring Wireshark

![Install](https://img.shields.io/badge/Wireshark-Install%20%26%20Configure-1679A7?style=flat-square&logo=wireshark&logoColor=white)
![Permissions](https://img.shields.io/badge/Non--Root-Capture%20Setup-green?style=flat-square)

---

## 📦 Subtask 1.1 — Update System and Install Wireshark

🔄 **Update package repositories:**

```bash
sudo apt update
```

📥 **Install Wireshark and related tools:**

```bash
sudo apt install -y wireshark tshark curl wget dnsutils
```

👤 **Add current user to the wireshark group:**

```bash
sudo usermod -a -G wireshark $USER
```

🔁 **Reload group membership:**

```bash
newgrp wireshark
```

---

## ⚙️ Subtask 1.2 — Configure Wireshark for Non-Root Capture

🔧 **Reconfigure wireshark-common to allow non-superuser packet capture:**

```bash
sudo dpkg-reconfigure wireshark-common
```

> 📝 When prompted, select **Yes** to allow non-superusers to capture packets.

🔑 **Set capabilities for dumpcap:**

```bash
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
```

✅ **Verify the configuration:**

```bash
getcap /usr/bin/dumpcap
```

---

## 🔍 Subtask 1.3 — Verify Installation and Network Interfaces

📋 **List available network interfaces:**

```bash
ip link show
```

🔎 **Check interfaces available to Wireshark:**

```bash
tshark -D
```

> 📝 Make note of your primary network interface — usually `eth0` or `ens3`.

---

# 📋 Task 2 — Capturing Network Traffic

![Capture](https://img.shields.io/badge/Live-Packet%20Capture-blue?style=flat-square)
![Filter](https://img.shields.io/badge/BPF-Capture%20Filters-orange?style=flat-square)

---

## 📡 Subtask 2.1 — Start Basic Packet Capture

🖥️ **Start Wireshark GUI** *(if using a desktop environment)*:

```bash
wireshark &
```

🔄 **Alternative — Start command-line capture with tshark:**

```bash
sudo tshark -i eth0 -w /tmp/network_capture.pcap
```

> 💡 If using the GUI, select your network interface and click **Start**.

---

## 🌐 Subtask 2.2 — Generate Network Traffic for Analysis

🖥️ **Open a new terminal and generate various types of traffic:**

🔍 **Generate DNS traffic:**

```bash
nslookup google.com
nslookup facebook.com
nslookup malicious-domain-example.com
```

🌐 **Generate HTTP traffic:**

```bash
curl -v http://httpbin.org/get
curl -v http://httpbin.org/user-agent
```

🔒 **Generate HTTPS/TLS traffic:**

```bash
curl -v https://httpbin.org/get
curl -v https://www.google.com
```

⚠️ **Generate suspicious-looking DNS queries:**

```bash
nslookup suspicious.example.com
nslookup malware.test.com
```

---

## 🎯 Subtask 2.3 — Capture Traffic with Specific Filters

📦 **Capture only DNS traffic:**

```bash
sudo tshark -i eth0 -f "port 53" -w /tmp/dns_traffic.pcap -c 50
```

🌐 **Capture only HTTP traffic:**

```bash
sudo tshark -i eth0 -f "port 80" -w /tmp/http_traffic.pcap -c 50
```

🔒 **Capture only HTTPS traffic:**

```bash
sudo tshark -i eth0 -f "port 443" -w /tmp/https_traffic.pcap -c 50
```

> **📁 Capture Files Summary:**

| File | Filter | Protocol |
|---|---|---|
| `dns_traffic.pcap` | `port 53` | 🔍 DNS |
| `http_traffic.pcap` | `port 80` | 🌐 HTTP |
| `https_traffic.pcap` | `port 443` | 🔒 HTTPS/TLS |

---

# 📋 Task 3 — Analyzing DNS Traffic for Anomalies

![DNS](https://img.shields.io/badge/DNS-Query%20Analysis-orange?style=flat-square)
![Tunneling](https://img.shields.io/badge/DNS-Tunneling%20Detection-red?style=flat-square)

---

## 🔎 Subtask 3.1 — Load and Filter DNS Traffic

📂 **Open the DNS capture file in Wireshark:**

```bash
wireshark /tmp/dns_traffic.pcap &
```

🎯 **In Wireshark, apply the following display filter:**

```
dns
```

---

## 📊 Subtask 3.2 — Identify DNS Query Patterns

✏️ **Create a DNS analysis script:**

```bash
cat > /tmp/analyze_dns.sh << 'EOF'
#!/bin/bash

echo "=== DNS Traffic Analysis ==="
echo "Analyzing DNS queries from capture file..."

# Extract DNS queries using tshark
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name \
  -Y "dns.flags.response == 0" > /tmp/dns_queries.txt

echo "Top DNS queries:"
sort /tmp/dns_queries.txt | uniq -c | sort -nr | head -10

echo -e "\n=== Potential Suspicious Domains ==="
grep -E "(malware|suspicious|phishing|botnet|trojan)" \
  /tmp/dns_queries.txt || echo "No obviously suspicious domains found"

echo -e "\n=== Unusual TLD Analysis ==="
grep -o '\.[a-z]*$' /tmp/dns_queries.txt | sort | uniq -c | sort -nr

echo -e "\n=== DNS Response Analysis ==="
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.resp.name -e dns.a \
  -Y "dns.flags.response == 1 and dns.a" | head -10
EOF

chmod +x /tmp/analyze_dns.sh
/tmp/analyze_dns.sh
```

---

## 🕵️ Subtask 3.3 — Detect DNS Tunneling Attempts

✏️ **Create a DNS tunneling detection script:**

```bash
cat > /tmp/detect_dns_tunneling.sh << 'EOF'
#!/bin/bash

echo "=== DNS Tunneling Detection ==="

# Analyze query lengths (DNS tunneling often uses long subdomain names)
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name \
  -Y "dns.flags.response == 0" | \
while read query; do
    if [ ${#query} -gt 50 ]; then
        echo "Suspicious long DNS query: $query (Length: ${#query})"
    fi
done

echo -e "\n=== Query Type Analysis ==="
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.type \
  -Y "dns.flags.response == 0" | sort | uniq -c | sort -nr

echo -e "\n=== Subdomain Analysis ==="
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name \
  -Y "dns.flags.response == 0" | \
grep -o '\.' | wc -l | awk '{print "Average dots per query: " $1/NR}'
EOF

chmod +x /tmp/detect_dns_tunneling.sh
/tmp/detect_dns_tunneling.sh
```

> **🚨 DNS Tunneling Indicators:**

| Indicator | Description | Risk |
|---|---|---|
| 📏 Long queries | Subdomain name > 50 characters | 🔴 High |
| 🔢 Unusual query types | TXT, NULL, CNAME records in bulk | 🟠 Medium |
| 📊 High subdomain count | Excessive dots per query | 🟠 Medium |
| ⚠️ Suspicious keywords | `malware`, `botnet`, `phishing` in domain | 🔴 High |

---

# 📋 Task 4 — Analyzing HTTP Traffic for Anomalies

![HTTP](https://img.shields.io/badge/HTTP-Request%20Analysis-blue?style=flat-square)
![SQLi](https://img.shields.io/badge/SQLi%20%2F%20XSS-Attack%20Detection-red?style=flat-square)

---

## 🌐 Subtask 4.1 — Extract and Analyze HTTP Requests

📡 **Generate HTTP traffic with various user agents and capture it:**

```bash
# Generate traffic with different user agents
curl -H "User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36" \
  http://httpbin.org/user-agent
curl -H "User-Agent: SuspiciousBot/1.0" http://httpbin.org/user-agent
curl -H "User-Agent: " http://httpbin.org/user-agent

# Capture this traffic
sudo tshark -i eth0 -f "port 80" -w /tmp/http_analysis.pcap -c 30 &
TSHARK_PID=$!

# Generate traffic
sleep 2
curl -v http://httpbin.org/get
curl -v http://httpbin.org/post -d "data=test"
curl -v http://httpbin.org/cookies/set/session/abc123

# Stop capture
sleep 5
kill $TSHARK_PID
```

---

## 📊 Subtask 4.2 — Analyze HTTP Headers and Methods

✏️ **Create an HTTP analysis script:**

```bash
cat > /tmp/analyze_http.sh << 'EOF'
#!/bin/bash

echo "=== HTTP Traffic Analysis ==="

echo "HTTP Methods Used:"
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.request.method | sort | uniq -c

echo -e "\n=== User Agents ==="
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.user_agent | sort | uniq -c

echo -e "\n=== Requested URLs ==="
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.host -e http.request.uri | head -10

echo -e "\n=== HTTP Response Codes ==="
tshark -r /tmp/http_analysis.pcap -Y "http.response" \
  -T fields -e http.response.code | sort | uniq -c

echo -e "\n=== Potential Security Issues ==="
echo "Checking for suspicious user agents..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.user_agent | \
  grep -iE "(bot|crawler|scanner|exploit)" || \
  echo "No obviously suspicious user agents found"

echo -e "\nChecking for authentication headers..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.authorization | \
  grep -v "^$" || echo "No authorization headers found"
EOF

chmod +x /tmp/analyze_http.sh
/tmp/analyze_http.sh
```

---

## 🚨 Subtask 4.3 — Detect HTTP Anomalies

✏️ **Create an HTTP anomaly detection script:**

```bash
cat > /tmp/detect_http_anomalies.sh << 'EOF'
#!/bin/bash

echo "=== HTTP Anomaly Detection ==="

echo "Checking for SQL Injection attempts..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.request.uri | \
  grep -iE "(union|select|insert|delete|drop|'|;|--)" || \
  echo "No SQL injection patterns detected"

echo -e "\nChecking for XSS attempts..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.request.uri | \
  grep -iE "(<script|javascript:|onload=|onerror=)" || \
  echo "No XSS patterns detected"

echo -e "\nChecking for directory traversal..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.request.uri | \
  grep -E "(\.\.\/|\.\.\\)" || echo "No directory traversal patterns detected"

echo -e "\nChecking for unusual HTTP methods..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.request.method | \
  grep -vE "^(GET|POST|HEAD|PUT|DELETE|OPTIONS)$" || \
  echo "Only standard HTTP methods found"

echo -e "\nAnalyzing request sizes..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" \
  -T fields -e http.content_length | \
  awk '{if($1>10000) print "Large request detected: " $1 " bytes"}'
EOF

chmod +x /tmp/detect_http_anomalies.sh
/tmp/detect_http_anomalies.sh
```

> **🔍 HTTP Attack Pattern Checklist:**

| Attack Type | Pattern Detected | Tool |
|---|---|---|
| 💉 SQL Injection | `UNION`, `SELECT`, `DROP`, `'`, `--` | `grep -iE` |
| 📜 XSS | `<script`, `javascript:`, `onerror=` | `grep -iE` |
| 📁 Directory Traversal | `../`, `..\` | `grep -E` |
| 🤖 Suspicious Bots | `bot`, `scanner`, `exploit` in User-Agent | `grep -iE` |
| 📦 Oversized Requests | `content_length > 10000` | `awk` |

---

# 📋 Task 5 — Analyzing TLS Traffic for Security Issues

![TLS](https://img.shields.io/badge/TLS-Handshake%20Analysis-green?style=flat-square&logo=letsencrypt&logoColor=white)
![Cipher](https://img.shields.io/badge/Cipher-Suite%20Audit-purple?style=flat-square)
![PFS](https://img.shields.io/badge/Perfect%20Forward-Secrecy%20Check-blue?style=flat-square)

---

## 🔒 Subtask 5.1 — Capture and Examine TLS Handshakes

📡 **Generate TLS traffic and capture it:**

```bash
# Capture TLS traffic
sudo tshark -i eth0 -f "port 443" -w /tmp/tls_traffic.pcap -c 50 &
TSHARK_PID=$!

# Generate TLS traffic
sleep 2
curl -v https://www.google.com
curl -v https://httpbin.org/get
curl -v https://badssl.com/
curl -k -v https://self-signed.badssl.com/

# Stop capture
sleep 5
kill $TSHARK_PID
```

---

## 🔍 Subtask 5.2 — Analyze TLS Handshake Process

✏️ **Create a TLS analysis script:**

```bash
cat > /tmp/analyze_tls.sh << 'EOF'
#!/bin/bash

echo "=== TLS Traffic Analysis ==="

echo "TLS Versions Used:"
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 1" \
  -T fields -e tls.handshake.version | sort | uniq -c

echo -e "\n=== Server Names (SNI) ==="
tshark -r /tmp/tls_traffic.pcap \
  -Y "tls.handshake.extensions_server_name" \
  -T fields -e tls.handshake.extensions_server_name | sort | uniq

echo -e "\n=== Cipher Suites ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" \
  -T fields -e tls.handshake.ciphersuite | head -10

echo -e "\n=== Certificate Analysis ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 11" \
  -T fields -e x509sat.printableString | head -5

echo -e "\n=== TLS Alerts ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.alert_message" \
  -T fields -e tls.alert_message.level -e tls.alert_message.desc
EOF

chmod +x /tmp/analyze_tls.sh
/tmp/analyze_tls.sh
```

---

## ⚠️ Subtask 5.3 — Detect TLS Security Issues

✏️ **Create a TLS security detection script:**

```bash
cat > /tmp/detect_tls_issues.sh << 'EOF'
#!/bin/bash

echo "=== TLS Security Issue Detection ==="

echo "Checking for weak TLS versions..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 1" \
  -T fields -e tls.handshake.version | \
while read version; do
    case $version in
        "0x0300") echo "🔴 WARNING: SSL 3.0 detected (insecure)" ;;
        "0x0301") echo "🟠 WARNING: TLS 1.0 detected (deprecated)" ;;
        "0x0302") echo "🟡 WARNING: TLS 1.1 detected (deprecated)" ;;
        "0x0303") echo "🟢 INFO: TLS 1.2 detected (acceptable)" ;;
        "0x0304") echo "✅ GOOD: TLS 1.3 detected (recommended)" ;;
    esac
done

echo -e "\nChecking for certificate validation issues..."
tshark -r /tmp/tls_traffic.pcap \
  -Y "tls.alert_message.desc == 42" \
  -T fields -e frame.time || echo "No bad certificate alerts found"

echo -e "\nAnalyzing cipher suite security..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" \
  -T fields -e tls.handshake.ciphersuite | \
while read cipher; do
    if [[ $cipher == *"RC4"* ]] || [[ $cipher == *"DES"* ]]; then
        echo "WARNING: Weak cipher detected: $cipher"
    fi
done

echo -e "\nChecking for perfect forward secrecy..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" \
  -T fields -e tls.handshake.ciphersuite | \
  grep -E "(DHE|ECDHE)" && \
  echo "✅ Perfect Forward Secrecy supported" || \
  echo "⚠️ No PFS detected"
EOF

chmod +x /tmp/detect_tls_issues.sh
/tmp/detect_tls_issues.sh
```

> **🔒 TLS Version Security Rating:**

| Version | Hex | Status |
|---|---|---|
| SSL 3.0 | `0x0300` | 🔴 Insecure — disable immediately |
| TLS 1.0 | `0x0301` | 🟠 Deprecated — upgrade required |
| TLS 1.1 | `0x0302` | 🟡 Deprecated — upgrade required |
| TLS 1.2 | `0x0303` | 🟢 Acceptable — monitor cipher suites |
| TLS 1.3 | `0x0304` | ✅ Recommended — best choice |

---

# 📋 Task 6 — Advanced Traffic Analysis and Reporting

![Report](https://img.shields.io/badge/Comprehensive-Analysis%20Report-darkblue?style=flat-square)
![Stats](https://img.shields.io/badge/Traffic-Statistics-blue?style=flat-square)
![Export](https://img.shields.io/badge/CSV-Export%20Results-green?style=flat-square)

---

## 📝 Subtask 6.1 — Create Comprehensive Network Analysis

✏️ **Create a comprehensive analysis script:**

```bash
cat > /tmp/comprehensive_analysis.sh << 'EOF'
#!/bin/bash

REPORT_FILE="/tmp/network_analysis_report.txt"

echo "=== COMPREHENSIVE NETWORK TRAFFIC ANALYSIS REPORT ===" > $REPORT_FILE
echo "Generated on: $(date)" >> $REPORT_FILE
echo "Analyst: $(whoami)" >> $REPORT_FILE
echo "=========================================" >> $REPORT_FILE

echo -e "\n1. TRAFFIC SUMMARY" >> $REPORT_FILE
echo "Total packets captured:" >> $REPORT_FILE
ls -la /tmp/*.pcap | wc -l >> $REPORT_FILE

echo -e "\n2. PROTOCOL DISTRIBUTION" >> $REPORT_FILE
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)" >> $REPORT_FILE
        tshark -r "$file" -q -z io,phs | head -20 >> $REPORT_FILE
        echo "" >> $REPORT_FILE
    fi
done

echo -e "\n3. SECURITY FINDINGS" >> $REPORT_FILE
echo "DNS Analysis Results:" >> $REPORT_FILE
/tmp/analyze_dns.sh >> $REPORT_FILE 2>/dev/null

echo -e "\nHTTP Analysis Results:" >> $REPORT_FILE
/tmp/analyze_http.sh >> $REPORT_FILE 2>/dev/null

echo -e "\nTLS Analysis Results:" >> $REPORT_FILE
/tmp/analyze_tls.sh >> $REPORT_FILE 2>/dev/null

echo -e "\n4. RECOMMENDATIONS" >> $REPORT_FILE
echo "- Monitor DNS queries for unusual patterns" >> $REPORT_FILE
echo "- Implement HTTP security headers" >> $REPORT_FILE
echo "- Ensure TLS 1.2 or higher is used" >> $REPORT_FILE
echo "- Regular security monitoring recommended" >> $REPORT_FILE

echo "Report generated: $REPORT_FILE"
cat $REPORT_FILE
EOF

chmod +x /tmp/comprehensive_analysis.sh
/tmp/comprehensive_analysis.sh
```

---

## 📈 Subtask 6.2 — Create Traffic Visualization

✏️ **Create a traffic statistics script:**

```bash
cat > /tmp/traffic_stats.sh << 'EOF'
#!/bin/bash

echo "=== NETWORK TRAFFIC STATISTICS ==="

echo "Top 10 Destination IPs:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        tshark -r "$file" -T fields -e ip.dst | sort | uniq -c | sort -nr | head -10
    fi
done

echo -e "\nTop 10 Source IPs:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        tshark -r "$file" -T fields -e ip.src | sort | uniq -c | sort -nr | head -10
    fi
done

echo -e "\nProtocol Usage:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)"
        tshark -r "$file" -T fields -e _ws.col.Protocol | sort | uniq -c | sort -nr | head -10
        echo ""
    fi
done

echo -e "\nTraffic Timeline:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)"
        tshark -r "$file" -T fields -e frame.time | head -5
        echo "..."
        tshark -r "$file" -T fields -e frame.time | tail -5
        echo ""
    fi
done
EOF

chmod +x /tmp/traffic_stats.sh
/tmp/traffic_stats.sh
```

---

## 💾 Subtask 6.3 — Export Analysis Results

✏️ **Create an export script:**

```bash
cat > /tmp/export_results.sh << 'EOF'
#!/bin/bash

EXPORT_DIR="/tmp/wireshark_analysis_export"
mkdir -p $EXPORT_DIR

echo "Exporting analysis results to $EXPORT_DIR"

# Copy all capture files
cp /tmp/*.pcap $EXPORT_DIR/ 2>/dev/null

# Export DNS queries
tshark -r /tmp/dns_traffic.pcap \
  -T fields -e frame.time -e dns.qry.name -e dns.qry.type \
  > $EXPORT_DIR/dns_queries.csv 2>/dev/null

# Export HTTP requests
tshark -r /tmp/http_analysis.pcap \
  -T fields -e frame.time -e http.host -e http.request.method -e http.request.uri \
  > $EXPORT_DIR/http_requests.csv 2>/dev/null

# Export TLS connections
tshark -r /tmp/tls_traffic.pcap \
  -T fields -e frame.time -e ip.dst -e tls.handshake.extensions_server_name \
  > $EXPORT_DIR/tls_connections.csv 2>/dev/null

# Copy analysis scripts
cp /tmp/analyze_*.sh $EXPORT_DIR/
cp /tmp/detect_*.sh $EXPORT_DIR/
cp /tmp/comprehensive_analysis.sh $EXPORT_DIR/

# Create summary
echo "Analysis completed on: $(date)" > $EXPORT_DIR/summary.txt
echo "Files analyzed: $(ls /tmp/*.pcap 2>/dev/null | wc -l)" >> $EXPORT_DIR/summary.txt
echo "Total packets: $(tshark -r /tmp/*.pcap -T fields -e frame.number 2>/dev/null | wc -l)" >> $EXPORT_DIR/summary.txt

echo "Export completed. Files available in: $EXPORT_DIR"
ls -la $EXPORT_DIR
EOF

chmod +x /tmp/export_results.sh
/tmp/export_results.sh
```

> **📁 Exported Files Summary:**

| File | Contents |
|---|---|
| `dns_queries.csv` | Timestamp, query name, query type |
| `http_requests.csv` | Timestamp, host, method, URI |
| `tls_connections.csv` | Timestamp, destination IP, SNI |
| `summary.txt` | Analysis metadata and packet counts |
| `*.sh` | All analysis and detection scripts |

---

# 🔧 Troubleshooting Common Issues

<details>
<summary>🔴 Permission Denied for Packet Capture</summary>

Add user to wireshark group:

```bash
sudo usermod -a -G wireshark $USER
```

Set proper capabilities:

```bash
sudo setcap cap_net_raw,cap_net_admin=eip /usr/bin/dumpcap
```

Restart session or reload group:

```bash
newgrp wireshark
```

</details>

<details>
<summary>🔴 No Network Interface Available</summary>

Check available interfaces:

```bash
ip link show
```

Ensure the interface is up:

```bash
sudo ip link set eth0 up
```

Check for wireless monitor mode support:

```bash
iwconfig 2>/dev/null
```

</details>

<details>
<summary>🔴 Capture Files Not Generated or Empty</summary>

Check available disk space:

```bash
df -h /tmp
```

Verify network activity:

```bash
ping -c 5 google.com
```

Use verbose mode for debugging:

```bash
sudo tshark -i eth0 -v -c 10
```

</details>

<details>
<summary>🔴 Analysis Scripts Not Working</summary>

Check if capture files exist:

```bash
ls -la /tmp/*.pcap
```

Verify tshark installation:

```bash
which tshark
```

Run scripts with debug output:

```bash
bash -x /tmp/analyze_dns.sh
```

</details>

---

# ✅ Expected Outcomes

After completing this lab, students should have:

- ✅ **Wireshark installed and configured** for non-root packet capture
- ✅ **Live traffic captured** across DNS, HTTP, and HTTPS protocols
- ✅ **DNS analysis script** identifying suspicious domains and tunneling indicators
- ✅ **HTTP analysis script** detecting SQLi, XSS, traversal, and suspicious bots
- ✅ **TLS analysis script** auditing versions, cipher suites, and PFS support
- ✅ **Comprehensive report** combining all findings with recommendations
- ✅ **CSV exports** of DNS, HTTP, and TLS connection data

---

# 🎓 Conclusion

In this lab, you successfully performed comprehensive **network traffic analysis** using Wireshark and TShark. Here's a summary of key accomplishments:

| Area | Achievement |
|---|---|
| 📡 Capture | Live packet capture via GUI and CLI with protocol filters |
| 🔍 DNS Analysis | Query pattern extraction, suspicious domain detection, tunneling detection |
| 🌐 HTTP Analysis | Method/user-agent audit, SQLi/XSS/traversal detection |
| 🔒 TLS Analysis | Version audit, cipher suite check, PFS detection, alert monitoring |
| 📊 Reporting | Comprehensive report generation with protocol distribution |
| 💾 Export | CSV exports of DNS, HTTP, and TLS data for further investigation |

---

## 💡 Key Takeaways

| # | Takeaway |
|---|---|
| 🕵️ | **Packet-level evidence** is essential for security incident investigation |
| 🤖 | **Automated scripts** make large-scale traffic analysis efficient |
| 🔒 | **TLS 1.2+ and PFS** are minimum requirements for secure communications |
| 🔍 | **DNS anomalies** like long queries often indicate tunneling or exfiltration |
| 🌐 | **HTTP headers and URIs** reveal attack patterns before they succeed |
| 📋 | **Regular traffic analysis** supports proactive threat detection |

---

## 🚀 Next Steps

![Zeek](https://img.shields.io/badge/Next-Zeek%20Network%20Monitor-blue?style=flat-square)
![SIEM](https://img.shields.io/badge/Next-SIEM%20Integration-orange?style=flat-square)
![Suricata](https://img.shields.io/badge/Next-Suricata%20IDS-red?style=flat-square)
![Threat](https://img.shields.io/badge/Next-Threat%20Hunting-purple?style=flat-square)

- 🔵 Explore **Zeek (formerly Bro)** for advanced network monitoring and logging
- 🟠 Integrate captures into a **SIEM** like Elastic Stack or Splunk
- 🔴 Study **Suricata IDS** for automated rule-based threat detection
- 🟣 Practice **threat hunting** using network forensic techniques

---

<div align="center">

![Made with](https://img.shields.io/badge/Made%20with-❤️%20for%20Security-blueviolet?style=for-the-badge)
![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Lab%20Guide-0077B5?style=for-the-badge)

</div>
