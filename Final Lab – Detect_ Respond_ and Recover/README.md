 Final Lab – Detect, Respond, and Recover (SOC Security Operations)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- Deploy and configure security monitoring tools (:contentReference[oaicite:0]{index=0} and :contentReference[oaicite:1]{index=1})
- Develop Python scripts for automated log analysis and threat detection
- Simulate attack scenarios and identify security incidents
- Execute incident response procedures following industry best practices
- Document findings and create professional incident reports

---

## 📌 Prerequisites

Students should have:

- Basic Linux command-line operations
- Fundamental networking concepts (TCP/IP, ports, protocols)
- Basic Python programming (variables, loops, file I/O)
- Understanding of common cybersecurity threats

---

## 🖥️ Lab Environment

**Al Nafi Cloud Machine Setup**

This lab runs on a pre-configured Ubuntu 22.04 LTS environment with:

- 4GB RAM
- Internet connectivity
- sudo privileges
- Pre-installed security tools (Wazuh, Zeek, Python3)

---

# 🧩 Task 1: Install and Configure Security Monitoring Tools

---

## ⚙️ Step 1.1: System Preparation

```bash
sudo apt update && sudo apt upgrade -y

sudo apt install -y curl wget gnupg python3 python3-pip git libpcap-dev

pip3 install pandas requests

mkdir -p ~/soc-lab/{logs,scripts,reports,evidence}
cd ~/soc-lab
🛡️ Step 1.2: Install Wazuh Manager
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | gpg --no-default-keyring --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg --import
sudo chmod 644 /usr/share/keyrings/wazuh.gpg

echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | sudo tee /etc/apt/sources.list.d/wazuh.list

sudo apt update
sudo apt install -y wazuh-manager

sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager
sudo systemctl status wazuh-manager
🔐 Step 1.3: Configure Wazuh Monitoring
sudo cp /var/ossec/etc/ossec.conf /var/ossec/etc/ossec.conf.backup

sudo tee -a /var/ossec/etc/ossec.conf > /dev/null << 'EOF'
<ossec_config>
  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/auth.log</location>
  </localfile>

  <localfile>
    <log_format>syslog</log_format>
    <location>/var/log/syslog</location>
  </localfile>
</ossec_config>
EOF

sudo systemctl restart wazuh-manager
🚨 Step 1.4: Custom Detection Rules
sudo tee /var/ossec/etc/rules/local_rules.xml > /dev/null << 'EOF'
<group name="local,syslog,sshd,">

  <rule id="100001" level="10">
    <if_matched_sid>5716</if_matched_sid>
    <description>SSH Brute Force Attack Detected</description>
    <same_source_ip />
    <frequency>5</frequency>
    <timeframe>300</timeframe>
  </rule>

  <rule id="100002" level="12">
    <if_group>syscheck</if_group>
    <field name="file">/etc/passwd|/etc/shadow</field>
    <description>Critical system file modified</description>
  </rule>

</group>
EOF

sudo systemctl restart wazuh-manager
🌐 Step 1.5: Install Zeek Network Monitor
echo 'deb http://download.opensuse.org/repositories/security:/zeek/xUbuntu_22.04/ /' | sudo tee /etc/apt/sources.list.d/security:zeek.list

curl -fsSL https://download.opensuse.org/repositories/security:zeek/xUbuntu_22.04/Release.key | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/security_zeek.gpg > /dev/null

sudo apt update
sudo apt install -y zeek

echo 'export PATH=/opt/zeek/bin:$PATH' >> ~/.bashrc
source ~/.bashrc

sudo mkdir -p /opt/zeek/logs
sudo chmod 755 /opt/zeek/logs
🧠 Task 2: Develop Log Analysis Scripts
🐍 Step 2.1: Wazuh Log Analyzer
#!/usr/bin/env python3
"""
Wazuh Log Analyzer
"""

import json
from collections import defaultdict

class WazuhAnalyzer:
    def __init__(self):
        self.log_file = "/var/ossec/logs/alerts/alerts.json"
        self.alerts = []
        self.stats = defaultdict(int)

    def load_alerts(self):
        # Load and parse JSON alerts
        pass

    def analyze_severity(self):
        # Count severity levels
        pass

    def detect_brute_force(self):
        # Detect repeated login failures
        pass

    def generate_report(self):
        # Create report file
        pass

def main():
    analyzer = WazuhAnalyzer()
    # Execute workflow

if __name__ == "__main__":
    main()
🌐 Step 2.2: Zeek Traffic Analyzer
#!/usr/bin/env python3
"""
Zeek Analyzer
"""

class ZeekAnalyzer:
    def __init__(self):
        self.log_dir = "/opt/zeek/logs"

    def load_conn_log(self):
        # Parse conn.log
        pass

    def detect_port_scan(self):
        # Detect scanning activity
        pass

    def analyze_traffic_volume(self):
        # Detect large transfers
        pass

    def generate_report(self):
        # Save report
        pass

def main():
    analyzer = ZeekAnalyzer()

if __name__ == "__main__":
    main()
🚨 Step 2.3: Incident Response Script
#!/usr/bin/env python3

class IncidentResponder:
    def block_ip(self, ip):
        # iptables blocking
        pass

    def collect_evidence(self, data):
        # Save forensic data
        pass

    def create_incident_report(self, incident, details):
        # Generate report
        pass

def main():
    responder = IncidentResponder()

if __name__ == "__main__":
    main()
⚔️ Task 3: Simulate Attack Scenarios
🔓 SSH Brute Force Simulation
for i in {1..10}; do
    ssh test@localhost
done
🌐 Port Scan Simulation
for port in {20..100}; do
    echo >/dev/tcp/127.0.0.1/$port
done
📊 Task 4: Detect and Respond to Incidents
🔍 Analyze Logs
python3 ~/soc-lab/scripts/wazuh_analyzer.py
python3 ~/soc-lab/scripts/zeek_analyzer.py
🚫 Block Malicious IP
sudo iptables -A INPUT -s 192.168.1.100 -j DROP
🧾 Evidence Collection
netstat -tuln > ~/soc-lab/evidence/netstat.txt
ps aux > ~/soc-lab/evidence/processes.txt
cp /var/ossec/logs/alerts/alerts.json ~/soc-lab/evidence/
📦 Task 5: Recovery & Reporting
🧹 System Check
sudo /var/ossec/bin/rootcheck
sudo find /etc -type f -mtime -1
📄 Final Incident Report
# Incident Report

## Summary
- Incident detected via Wazuh + Zeek

## Response
- IP blocked
- Evidence collected
- Logs analyzed

## Recommendations
- Enable continuous monitoring
- Improve alert thresholds
📌 Expected Outcomes

Students will achieve:

Functional SOC monitoring system (Wazuh + Zeek)
Python-based threat detection scripts
Simulated attack detection capability
Incident response execution workflow
Forensic evidence collection
Professional incident reporting
🧠 Key Takeaways
Security monitoring requires layered tools
Automation improves detection speed
Logs are critical forensic evidence
Response actions must be fast and structured
Documentation is essential in cybersecurity operations
🚀 Next Steps
Integrate SIEM dashboards
Add machine learning anomaly detection
Build real-time alerting system
Extend Zeek scripts for advanced threats
Automate full SOC pipeline
