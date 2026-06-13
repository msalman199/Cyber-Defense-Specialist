# 🚨 Incident Triage with Python Automation

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Incident%20Response-red?style=for-the-badge&logo=hackthebox&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![SOC](https://img.shields.io/badge/SOC-Automation-critical?style=for-the-badge)
![SIEM](https://img.shields.io/badge/SIEM-Alert%20Triage-success?style=for-the-badge)
![Threat Intelligence](https://img.shields.io/badge/Threat-Intelligence-orange?style=for-the-badge)
![Incident Response](https://img.shields.io/badge/Incident-Response-darkred?style=for-the-badge)

### 🛡️ Alert Triage • 🔍 Threat Intelligence • ⚡ Automated Response

</div>

---

# 📖 Overview

Modern Security Operations Centers (SOCs) generate thousands of alerts daily. Manual investigation of every alert is inefficient and leads to alert fatigue.

This lab focuses on building an automated incident triage platform using Python capable of:

✅ Processing SIEM alerts

✅ Filtering false positives

✅ Calculating priority scores

✅ Enriching alerts with threat intelligence

✅ Generating incident tickets

✅ Automating response workflows

✅ Producing triage reports

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- 🚨 Automate security alert triage
- 🔍 Identify false positives using rule-based filtering
- 📊 Calculate incident priority scores
- 🛡️ Enrich alerts with threat intelligence
- 🎫 Generate automated incident tickets
- ⚡ Build response automation workflows
- 📄 Create incident reports and recommendations

---

# 🧰 Prerequisites

Before starting this lab:

- Basic Python programming
- Understanding of alerts and incidents
- Familiarity with JSON
- Linux command-line basics
- Knowledge of cybersecurity concepts

---

# 🏗️ Lab Environment

Al Nafi Cloud Machines provide:

- Ubuntu Linux
- Python 3.8+
- JSON Libraries
- Datetime Module
- Regular Expressions
- Development Tools

---

# 📂 Project Structure

```text
incident_triage_lab/
│
├── data/
│   └── sample_alerts.json
│
├── rules/
│   └── triage_rules.json
│
├── reports/
│
└── scripts/
    ├── incident_triage.py
    ├── alert_enrichment.py
    ├── automated_response.py
    └── complete_workflow.py
```

---

# 🚀 Task 1: Setup Environment

## 📁 Create Directory Structure

```bash
mkdir -p ~/incident_triage_lab/{data,scripts,reports,rules}

cd ~/incident_triage_lab
```

---

# 📄 Sample Alert Data

## File: `data/sample_alerts.json`

```json
[
  {
    "alert_id":"ALT-001",
    "severity":"HIGH",
    "alert_type":"Suspicious DNS Query",
    "event_count":15,
    "user":"john.doe",
    "asset":"WORKSTATION-01"
  },
  {
    "alert_id":"ALT-002",
    "severity":"MEDIUM",
    "alert_type":"Failed Login Attempt",
    "event_count":3,
    "user":"admin",
    "asset":"SERVER-01"
  },
  {
    "alert_id":"ALT-003",
    "severity":"LOW",
    "alert_type":"Port Scan",
    "event_count":100,
    "user":"vuln_scanner",
    "asset":"SCANNER-01"
  }
]
```

---

# 📄 Triage Rules

## File: `rules/triage_rules.json`

```json
{
  "whitelist": {
    "users": [
      "vuln_scanner",
      "backup_service"
    ]
  },

  "severity_weights": {
    "CRITICAL": 10,
    "HIGH": 7,
    "MEDIUM": 4,
    "LOW": 1
  },

  "alert_type_weights": {
    "Malware Detection": 10,
    "Data Exfiltration": 8,
    "Suspicious DNS Query": 6,
    "Failed Login Attempt": 5,
    "Port Scan": 2
  }
}
```

---

# 🛡️ Task 2: Build Core Triage Engine

## 📂 File: `scripts/incident_triage.py`

```python
#!/usr/bin/env python3

import json
import datetime


class IncidentTriageEngine:

    def __init__(self, rules_file):

        self.rules = self.load_rules(rules_file)

        self.processed_alerts = []
        self.false_positives = []
        self.high_priority_alerts = []

    def load_rules(self, rules_file):

        try:
            with open(rules_file) as f:
                return json.load(f)

        except FileNotFoundError:
            return {}

    def load_alerts(self, alerts_file):

        with open(alerts_file) as f:
            return json.load(f)

    def is_whitelisted(self, alert):

        whitelist = self.rules.get("whitelist", {})

        return (
            alert.get("user")
            in whitelist.get("users", [])
        )

    def calculate_priority_score(self, alert):

        score = 0

        score += self.rules["severity_weights"].get(
            alert["severity"],
            0
        )

        score += self.rules["alert_type_weights"].get(
            alert["alert_type"],
            0
        )

        if alert["event_count"] > 10:
            score += 2

        return score

    def triage_alert(self, alert):

        result = alert.copy()

        result["triage_timestamp"] = (
            datetime.datetime.now().isoformat()
        )

        if self.is_whitelisted(alert):

            result["triage_status"] = (
                "FALSE_POSITIVE"
            )

            result["priority_level"] = "LOW"

            return result

        score = self.calculate_priority_score(
            alert
        )

        result["priority_score"] = score

        result["triage_status"] = (
            "LEGITIMATE"
        )

        if score >= 15:
            level = "CRITICAL"
        elif score >= 10:
            level = "HIGH"
        elif score >= 5:
            level = "MEDIUM"
        else:
            level = "LOW"

        result["priority_level"] = level

        return result

    def process_alerts(self, alerts):

        for alert in alerts:

            triaged = self.triage_alert(alert)

            self.processed_alerts.append(
                triaged
            )

            if (
                triaged["triage_status"]
                == "FALSE_POSITIVE"
            ):
                self.false_positives.append(
                    triaged
                )

            if triaged["priority_level"] in [
                "CRITICAL",
                "HIGH"
            ]:
                self.high_priority_alerts.append(
                    triaged
                )

    def generate_summary_report(self):

        report = f"""
Total Alerts: {len(self.processed_alerts)}
False Positives: {len(self.false_positives)}
High Priority: {len(self.high_priority_alerts)}
"""

        return report

    def save_results(self, output_dir):

        with open(
            f"{output_dir}/processed_alerts.json",
            "w"
        ) as f:
            json.dump(
                self.processed_alerts,
                f,
                indent=4
            )


def main():

    engine = IncidentTriageEngine(
        "rules/triage_rules.json"
    )

    alerts = engine.load_alerts(
        "data/sample_alerts.json"
    )

    engine.process_alerts(alerts)

    print(
        engine.generate_summary_report()
    )

    engine.save_results("reports")


if __name__ == "__main__":
    main()
```

---

# ▶️ Run Triage Engine

```bash
chmod +x scripts/incident_triage.py
```

```bash
python3 scripts/incident_triage.py
```

---

# 🔍 Task 3: Alert Enrichment

## 📂 File: `scripts/alert_enrichment.py`

```python
#!/usr/bin/env python3

class AlertEnricher:

    def __init__(self):

        self.threat_intel = {
            "malicious_ips": [
                "203.0.113.10",
                "198.51.100.55"
            ]
        }

    def check_ip_reputation(self, ip):

        if ip in self.threat_intel[
            "malicious_ips"
        ]:

            return {
                "is_malicious": True,
                "threat_level": "HIGH"
            }

        return {
            "is_malicious": False,
            "threat_level": "LOW"
        }

    def enrich_alert(self, alert):

        enriched = alert.copy()

        enriched["source_ip_reputation"] = (
            self.check_ip_reputation(
                alert["source_ip"]
            )
        )

        return enriched


if __name__ == "__main__":

    print("Alert Enrichment Module")
```

---

# ⚡ Task 4: Automated Response System

## 📂 File: `scripts/automated_response.py`

```python
#!/usr/bin/env python3

import json


class AutomatedResponder:

    def __init__(self):

        self.response_log = []

    def generate_response_actions(
        self,
        alert
    ):

        priority = alert[
            "priority_level"
        ]

        if priority == "CRITICAL":

            return [
                "Isolate Host",
                "Notify SOC",
                "Create Ticket"
            ]

        elif priority == "HIGH":

            return [
                "Notify Analyst",
                "Create Ticket",
                "Collect Forensics"
            ]

        elif priority == "MEDIUM":

            return [
                "Create Ticket",
                "Queue Investigation"
            ]

        return ["Log Event"]

    def create_incident_ticket(
        self,
        alert
    ):

        return {
            "ticket_id":
            f"TKT-{alert['alert_id']}",

            "title":
            alert["alert_type"],

            "priority":
            alert["priority_level"]
        }

    def process_high_priority_alerts(
        self,
        alerts
    ):

        for alert in alerts:

            ticket = (
                self.create_incident_ticket(
                    alert
                )
            )

            actions = (
                self.generate_response_actions(
                    alert
                )
            )

            self.response_log.append(
                {
                    "ticket": ticket,
                    "actions": actions
                }
            )

    def save_response_log(
        self,
        output_file
    ):

        with open(output_file, "w") as f:

            json.dump(
                self.response_log,
                f,
                indent=4
            )


if __name__ == "__main__":

    print(
        "Automated Response System"
    )
```

---

# 🔗 Task 5: Complete Workflow

## 📂 File: `scripts/complete_workflow.py`

```python
#!/usr/bin/env python3

from incident_triage import (
    IncidentTriageEngine
)

from automated_response import (
    AutomatedResponder
)


def run_complete_workflow():

    print(
        "=== Complete Incident Triage Workflow ==="
    )

    engine = IncidentTriageEngine(
        "rules/triage_rules.json"
    )

    alerts = engine.load_alerts(
        "data/sample_alerts.json"
    )

    engine.process_alerts(alerts)

    responder = AutomatedResponder()

    responder.process_high_priority_alerts(
        engine.high_priority_alerts
    )

    responder.save_response_log(
        "reports/response_log.json"
    )

    print(
        engine.generate_summary_report()
    )


if __name__ == "__main__":
    run_complete_workflow()
```

---

# ▶️ Run Complete Workflow

```bash
python3 scripts/complete_workflow.py
```

---

# 📊 Expected Results

| Metric | Value |
|----------|----------|
| Alerts Processed | 5 |
| False Positives | 2 |
| High Priority Alerts | 2 |
| Tickets Created | 2 |
| Response Actions | 6 |

---

# 🛠️ Troubleshooting

## JSON Validation

```bash
python3 -m json.tool data/sample_alerts.json
```

---

## Verify Working Directory

```bash
pwd
```

Expected:

```text
/home/user/incident_triage_lab
```

---

## Check Files

```bash
find . -type f
```

---

## Permission Issues

```bash
chmod +x scripts/*.py
```

---

# 🎓 Learning Outcomes

After completing this lab, you will have:

✅ Built a Rule-Based Triage Engine

✅ Implemented False Positive Detection

✅ Created Priority Scoring Logic

✅ Enriched Alerts with Threat Intelligence

✅ Automated Incident Response Actions

✅ Generated Incident Tickets

✅ Built a Complete SOC Automation Workflow

---

# 🏁 Conclusion

This lab demonstrated practical Security Operations Center (SOC) automation using Python. You developed an end-to-end incident triage workflow that processes alerts, filters false positives, enriches threat data, prioritizes incidents, and automates response actions.

These capabilities are essential for modern SOC teams handling large alert volumes and seeking to improve incident response efficiency.

> 🚀 Next enhancements: SIEM integration, Machine Learning-based anomaly detection, User Behavior Analytics (UBA), Automated Forensics Collection, and Security Dashboards.

---

<div align="center">

### 🚨 Detect • Prioritize • Respond • Automate

⭐ Happy Hunting & Stay Secure! ⭐

</div>
