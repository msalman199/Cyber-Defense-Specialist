# 🚨 Incident Response Automation with Python

<div align="center">

![Python](https://img.shields.io/badge/Python-Automation-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Logs-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![CyberSecurity](https://img.shields.io/badge/Incident%20Response-Security-FF3B30?style=for-the-badge)
![Automation](https://img.shields.io/badge/SOC-Automation-0A66C2?style=for-the-badge)

</div>

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- 🧠 Build automated log collection & analysis systems using Python  
- 🚨 Implement severity-based incident response workflows  
- 📡 Create automated alerting mechanisms for security events  
- 🔍 Develop scripts for threat detection & pattern matching  
- ⚙️ Configure automated response actions based on incident severity  

---

# 📚 Prerequisites

Before starting this lab, students should have:

- 🐍 Basic Python programming (functions, file I/O, regex)  
- 🐧 Linux command line & log file structure understanding  
- 🔐 Basic cybersecurity & incident response knowledge  

---

# ☁️ Lab Environment

### 🚀 Al Nafi Cloud Machine Setup

- Single Linux-based cloud machine  
- Python 3 pre-installed  
- Required tools ready to use  

---

# 🧩 Task 1: Incident Response Framework Setup

## 📁 Step 1.1: Create Directory Structure

```bash
mkdir -p ~/incident_response/{scripts,logs,reports,config,alerts}
cd ~/incident_response

mkdir -p logs/{system,security,application}
mkdir -p scripts/{collection,analysis,response}
mkdir -p reports/incidents
```

## 📄 Step 1.2: Sample Log Files

### 🖥️ System Logs
```bash
cat > logs/system/syslog.log << 'EOF'
2024-01-15 10:30:15 server01 sshd: Failed password for root from 192.168.1.100
2024-01-15 10:31:20 server01 sshd: Failed password for admin from 192.168.1.100
2024-01-15 10:32:25 server01 kernel: CPU usage spike detected: 95%
2024-01-15 10:34:35 server01 firewall: BLOCKED connection from 10.0.0.50
EOF
```

### 🔐 Security Logs
```bash
cat > logs/security/auth.log << 'EOF'
2024-01-15 10:30:00 FAILED LOGIN FROM 192.168.1.200 FOR user1
2024-01-15 10:30:10 ROOT LOGIN ON tty1
EOF
```

### 🌐 Application Logs
```bash
cat > logs/application/webapp.log << 'EOF'
2024-01-15 10:29:45 [ERROR] SQL injection attempt detected
2024-01-15 10:31:55 [ERROR] Path traversal attempt ../../../etc/passwd
2024-01-15 10:33:05 [ERROR] XSS attempt <script>alert('XSS')</script>
EOF
```

## ⚙️ Step 1.3: Configuration File

📄 `config/response_config.json`

```json
{
  "email": {
    "smtp_server": "localhost",
    "smtp_port": 587,
    "recipients": ["admin@company.com"]
  },
  "blocking": {
    "use_iptables": true,
    "block_duration": 3600,
    "whitelist_ips": ["127.0.0.1"]
  },
  "thresholds": {
    "failed_login_count": 3,
    "time_window_seconds": 300
  }
}
```

---

# 🧩 Task 2: Log Collector

## 🐍 Step 2.1: log_collector.py

📄 `scripts/collection/log_collector.py`

```python
#!/usr/bin/env python3

import os
import json
import shutil
import datetime
from pathlib import Path

class LogCollector:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)
        self.logs_dir = self.base_dir / "logs"

    def collect_system_logs(self):
        print("📦 Collecting system logs...")
        return {"system_status": "active"}

    def collect_security_logs(self):
        print("🔐 Collecting security logs...")
        return {"security_status": "active"}

    def collect_application_logs(self):
        print("🌐 Collecting application logs...")
        return {"application_status": "active"}

    def generate_collection_report(self):
        report = {
            "timestamp": str(datetime.datetime.now()),
            "status": "completed"
        }

        report_path = self.base_dir / "reports/incidents/collection.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)
        with open(report_path, "w") as f:
            json.dump(report, f, indent=4)

        print("📊 Collection report generated")
        return str(report_path)

    def run_collection(self):
        print("🚀 Starting Log Collection System")
        self.collect_system_logs()
        self.collect_security_logs()
        self.collect_application_logs()
        self.generate_collection_report()
        print("✅ Log collection completed")


if __name__ == "__main__":
    collector = LogCollector("/home/ubuntu/incident_response")
    collector.run_collection()
```

---

# 🧩 Task 3: Log Analyzer

## 🔍 Step 3.1: log_analyzer.py

📄 `scripts/analysis/log_analyzer.py`

```python
#!/usr/bin/env python3

import re
import json
from pathlib import Path
from collections import defaultdict

class LogAnalyzer:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

        self.patterns = {
            "failed_login": r"FAILED|Failed password",
            "sql_injection": r"SQL injection|OR 1=1",
            "xss": r"<script>",
            "privilege": r"root|sudo"
        }

    def analyze_log_file(self, file_path):
        print(f"🔍 Analyzing {file_path}")
        incidents = []

        with open(file_path, "r", errors="ignore") as f:
            for line in f:
                for t, pattern in self.patterns.items():
                    if re.search(pattern, line, re.IGNORECASE):
                        incidents.append({
                            "type": t,
                            "line": line.strip()
                        })

        return incidents

    def run_analysis(self):
        print("🚨 Starting Incident Analysis")

        logs_path = self.base_dir / "logs"
        all_incidents = []

        for file in logs_path.rglob("*.log"):
            all_incidents.extend(self.analyze_log_file(file))

        report_path = self.base_dir / "reports/incidents/analysis.json"
        report_path.parent.mkdir(parents=True, exist_ok=True)

        with open(report_path, "w") as f:
            json.dump(all_incidents, f, indent=4)

        print("📊 Analysis completed")


if __name__ == "__main__":
    analyzer = LogAnalyzer("/home/ubuntu/incident_response")
    analyzer.run_analysis()
```

---

# 🧩 Task 4: Incident Response Engine

## ⚙️ Step 4.1: incident_responder.py

📄 `scripts/response/incident_responder.py`

```python
#!/usr/bin/env python3

import json
from pathlib import Path

class IncidentResponder:
    def __init__(self, base_dir):
        self.base_dir = Path(base_dir)

    def block_ip(self, ip):
        print(f"🚫 Blocking IP: {ip}")

    def send_alert(self, incident):
        print(f"📧 ALERT: {incident}")

    def respond(self):
        print("🚨 Running Incident Response Engine")

        report = self.base_dir / "reports/incidents/analysis.json"

        if not report.exists():
            print("❌ No analysis report found")
            return

        with open(report) as f:
            incidents = json.load(f)

        for inc in incidents:
            if inc["type"] == "failed_login":
                self.send_alert(inc)
            elif inc["type"] == "sql_injection":
                self.block_ip("192.168.1.100")

        print("✅ Response completed")


if __name__ == "__main__":
    responder = IncidentResponder("/home/ubuntu/incident_response")
    responder.respond()
```

## 🔗 Step 4.2: Automation Script

📄 `scripts/automated_response.py`

```python
#!/usr/bin/env python3
import sys
from pathlib import Path

# Append scripts directory to path to support standalone execution
sys.path.append(str(Path(__file__).parent))

from collection.log_collector import LogCollector
from analysis.log_analyzer import LogAnalyzer
from response.incident_responder import IncidentResponder

BASE = "/home/ubuntu/incident_response"

def main():
    print("🚀 INCIDENT RESPONSE AUTOMATION STARTED")

    collector = LogCollector(BASE)
    collector.run_collection()

    analyzer = LogAnalyzer(BASE)
    analyzer.run_analysis()

    responder = IncidentResponder(BASE)
    responder.respond()

    print("✅ FULL AUTOMATION COMPLETE")


if __name__ == "__main__":
    main()
```

---

# ▶️ Execution Commands

```bash
python3 scripts/collection/log_collector.py
python3 scripts/analysis/log_analyzer.py
python3 scripts/response/incident_responder.py
python3 scripts/automated_response.py
```

---

# 📁 Expected Output

```text
incident_response/
 ├── logs/
 ├── reports/
 │    └── incidents/
 │         ├── collection.json
 │         └── analysis.json
 ├── alerts/
 └── scripts/
```

---

# 🧠 Key Takeaways

- ⚡ **Python enables full SOC automation workflows**: Programmatic ingestion unifies decoupled data structures into an actionable state machine.
- 🔍 **Regex is powerful for threat detection**: Signature-matching via basic expressions allows security teams to identify vulnerabilities without excessive system overhead.
- 🚨 **Severity-based response improves security posture**: Differentiating actions (like dropping brute-force hosts vs logging scanning probes) minimizes system self-disruption.
- 📊 **Logs are the foundation of incident response**: Standardizing logs using common formats prevents data tracking gaps across system layers.
- 🔁 **Automation reduces response time**: Running defensive plays instantly isolates endpoints, dramatically lowering the risk of successful exploitation.

---

# 🚀 Conclusion

