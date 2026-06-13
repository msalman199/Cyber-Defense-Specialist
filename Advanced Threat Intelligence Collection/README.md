# 🛡️ Advanced Threat Intelligence Collection

<div align="center">

![Threat Intelligence](https://img.shields.io/badge/Threat-Intelligence-red?style=for-the-badge&logo=securityscorecard&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.10-blue?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu%2022.04-orange?style=for-the-badge&logo=ubuntu&logoColor=white)
![JSON](https://img.shields.io/badge/JSON-Data-black?style=for-the-badge&logo=json&logoColor=white)
![Cybersecurity](https://img.shields.io/badge/Cyber-Security-green?style=for-the-badge&logo=hackaday&logoColor=white)

</div>

---

# 📖 Overview

This lab focuses on building a complete **Threat Intelligence Collection and Analysis Pipeline** using Python.

Students will learn how to:

- 🌐 Collect threat intelligence from multiple sources
- 🔍 Validate IPs, Domains, and Hashes
- 📊 Normalize and standardize threat indicators
- ⚠️ Calculate risk scores automatically
- 📑 Generate intelligence reports
- 🚀 Build a complete threat intelligence automation workflow

---

# 🎯 Objectives

By the end of this lab, students will be able to:

✅ Collect threat intelligence data from multiple sources using Python

✅ Normalize and standardize threat indicators

✅ Validate:

- IP Addresses
- Domain Names
- File Hashes

✅ Calculate threat risk scores

✅ Generate automated reports

✅ Build an end-to-end Threat Intelligence Pipeline

---

# 📚 Prerequisites

Before starting this lab, ensure you have:

- Python Programming Basics
- Linux Command Line Fundamentals
- Cybersecurity Concepts
- JSON Knowledge
- Understanding of Threat Indicators

---

# 🖥️ Lab Environment

Al Nafi Cloud Machine provides:

| Component | Version |
|------------|------------|
| Ubuntu | 22.04 LTS |
| Python | 3.10 |
| Requests Library | Installed |
| Pandas | Installed |
| JSON Tools | Installed |
| Sample Threat Feeds | Available |

---

# 🏗️ Task 1: Environment Setup and Configuration

---

## 📁 Step 1: Create Project Structure

```bash
mkdir -p ~/threat_intel/{scripts,data,reports,config,logs}
cd ~/threat_intel

python3 --version
```

Expected Output:

```text
Python 3.10.x
```

---

## ⚙️ Step 2: Create Configuration File

Create:

```bash
config/sources.json
```

```json
{
    "data_sources": {
        "local_feeds": [
            "malware_domains.txt",
            "suspicious_ips.txt"
        ],
        "api_endpoints": {
            "virustotal": "https://www.virustotal.com/api/v3/",
            "abuseipdb": "https://api.abuseipdb.com/api/v2/"
        }
    },
    "thresholds": {
        "high_risk": 80,
        "medium_risk": 60,
        "low_risk": 40
    }
}
```

---

## 🧪 Step 3: Create Sample Threat Data

### Malicious Domains

```bash
cat > data/malware_domains.txt << 'EOF'
malicious-site.com
phishing-example.net
suspicious-domain.org
threat-actor.info
EOF
```

### Suspicious IPs

```bash
cat > data/suspicious_ips.txt << 'EOF'
192.168.1.100
203.0.113.10
198.51.100.20
EOF
```

---

# 🚀 Task 2: Implement Threat Intelligence Collector

---

## 🛠️ Step 1: Create Threat Collector

Create:

```text
scripts/threat_collector.py
```

### Features to Implement

| Feature | Description |
|----------|------------|
| Configuration Loader | Reads JSON settings |
| Logging System | File & Console Logging |
| IP Validation | IPv4 & IPv6 Support |
| Domain Validation | RFC-Compliant Checks |
| Hash Validation | MD5 / SHA1 / SHA256 |
| Indicator Collection | Reads Local Feeds |
| Indicator Enrichment | Adds Metadata |
| Risk Scoring | Calculates Threat Score |
| JSON Export | Saves Collected Data |

---

### Required Functions

```python
load_config()
setup_logging()
validate_ip()
validate_domain()
validate_hash()
collect_from_file()
enrich_indicator()
calculate_risk_score()
save_collected_data()
run_collection()
```

---

## 🔐 Threat Indicator Validation

### IP Validation

```python
ipaddress.ip_address(ip_string)
```

Supports:

- IPv4
- IPv6

---

### Domain Validation

Requirements:

- Must contain at least one dot
- Valid hostname format
- No illegal characters

Example:

```text
example.com
security.org
```

---

### Hash Validation

| Hash Type | Length |
|------------|------------|
| MD5 | 32 |
| SHA1 | 40 |
| SHA256 | 64 |

Example:

```text
d41d8cd98f00b204e9800998ecf8427e
```

---

## 🧮 Risk Score Formula

Example scoring model:

| Factor | Points |
|----------|----------|
| Base Confidence | +50 |
| Recent Activity | +20 |
| Malware Indicator | +20 |
| Known Threat Feed | +10 |

Maximum:

```text
100
```

---

## ▶️ Step 2: Test Collection

Make executable:

```bash
chmod +x scripts/threat_collector.py
```

Run:

```bash
python3 scripts/threat_collector.py
```

---

## 🔍 Step 3: Verify Output

```bash
ls -lh data/
```

View JSON:

```bash
python3 -m json.tool data/collected_*.json | head -30
```

---

# 🔄 Task 3: Implement Data Normalization

---

## 🧹 Step 1: Create Data Normalizer

Create:

```text
scripts/data_normalizer.py
```

---

### Required Functions

```python
load_raw_data()
normalize_confidence()
normalize_severity()
normalize_tags()
deduplicate_indicators()
normalize_dataset()
save_normalized_data()
generate_statistics()
```

---

## 📊 Severity Mapping

| Risk Score | Severity |
|------------|-----------|
| 80+ | HIGH |
| 60-79 | MEDIUM |
| 40-59 | LOW |
| <40 | INFO |

---

## 🏷️ Tag Normalization

Example:

| Input | Output |
|---------|---------|
| C2 | command_control |
| malware | malware |
| PHISHING | phishing |

---

## 🧠 Deduplication Logic

Keep:

✅ Highest confidence indicator

Merge:

✅ Tags

Remove:

✅ Duplicate entries

Track:

✅ Duplicate Count

---

## ▶️ Step 2: Run Normalization

```bash
python3 scripts/data_normalizer.py
```

Compare:

```bash
echo "Raw indicators:"
python3 -c "import json; print(len(json.load(open('data/collected_*.json'))))"

echo "Normalized indicators:"
python3 -c "import json; print(len(json.load(open('data/normalized_*.json'))))"
```

---

# 📑 Task 4: Generate Threat Intelligence Reports

---

## 📝 Step 1: Create Report Generator

Create:

```text
scripts/report_generator.py
```

---

### Functions to Complete

```python
load_data()
generate_executive_summary()
generate_severity_breakdown()
generate_indicator_type_analysis()
generate_top_threats()
generate_html_report()
generate_text_report()
generate_json_report()
```

---

## 📈 Executive Summary

Include:

- Total Indicators
- High Risk Indicators
- Top Threat Categories
- Risk Distribution

---

## 🔥 Top Threat Analysis

Example:

| Indicator | Type | Risk |
|------------|------|------|
| malicious-site.com | Domain | 95 |
| 203.0.113.10 | IP | 90 |
| SHA256 Hash | Hash | 88 |

---

## 🌐 HTML Reporting

Generate:

```html
reports/threat_report.html
```

Include:

- Dashboard Styling
- Severity Charts
- Statistics
- Top Threats

---

## 📄 Text Reporting

Generate:

```text
reports/threat_report.txt
```

---

## 📦 JSON Reporting

Generate:

```json
reports/threat_report.json
```

---

## ▶️ Step 2: Generate Reports

```bash
python3 scripts/report_generator.py
```

View Reports:

```bash
ls -lh reports/
```

Display Text Report:

```bash
cat reports/threat_report_*.txt
```

---

# ⚡ Step 3: Create Automated Pipeline

Create:

```bash
scripts/run_pipeline.sh
```

```bash
#!/bin/bash

echo "Starting Threat Intelligence Pipeline"
echo "======================================"

echo "[1/3] Collecting threat intelligence..."
python3 scripts/threat_collector.py

echo "[2/3] Normalizing data..."
python3 scripts/data_normalizer.py

echo "[3/3] Generating reports..."
python3 scripts/report_generator.py

echo "Pipeline completed successfully!"
echo "Check reports/ directory for output"
```

Make executable:

```bash
chmod +x scripts/run_pipeline.sh
```

Run:

```bash
./scripts/run_pipeline.sh
```

---

# 📂 Project Structure

```text
threat_intel/
│
├── config/
│   └── sources.json
│
├── data/
│   ├── malware_domains.txt
│   ├── suspicious_ips.txt
│   ├── collected_*.json
│   └── normalized_*.json
│
├── logs/
│   └── collection.log
│
├── reports/
│   ├── threat_report.html
│   ├── threat_report.txt
│   └── threat_report.json
│
├── scripts/
│   ├── threat_collector.py
│   ├── data_normalizer.py
│   ├── report_generator.py
│   └── run_pipeline.sh
│
└── README.md
```

---

# 🎯 Expected Outcomes

After completing this lab you will have:

✅ Threat Intelligence Collector

✅ Threat Indicator Validator

✅ Data Normalization Engine

✅ Risk Scoring Framework

✅ Multi-format Report Generator

✅ End-to-End Automation Pipeline

---

# 📦 Key Deliverables

| File | Purpose |
|--------|----------|
| threat_collector.py | Collect Threat Indicators |
| data_normalizer.py | Normalize & Deduplicate Data |
| report_generator.py | Generate Reports |
| run_pipeline.sh | Complete Automation Workflow |

---

# 🛠️ Troubleshooting

## ❌ Import Errors

Install missing modules:

```bash
pip3 install requests pandas
```

Verify:

```bash
python3 -c "import requests,pandas"
```

---

## ❌ File Not Found

Check directory:

```bash
pwd
```

Verify files:

```bash
ls -la data/
```

---

## ❌ JSON Errors

Validate:

```bash
python3 -m json.tool file.json
```

---

## ❌ Empty Reports

Check logs:

```bash
cat logs/collection.log
```

Verify data collection completed successfully.

---

# 🏆 Skills Developed

Throughout this lab you practiced:

🔍 Threat Intelligence Collection

🌐 IOC Validation

📊 Data Normalization

⚠️ Risk Assessment

📑 Automated Reporting

🚀 Security Automation

📈 Threat Intelligence Operations

---

# 🎓 Conclusion

In this lab, you built a complete Threat Intelligence Collection and Analysis Pipeline from the ground up.

You implemented:

- Threat Data Collection
- Indicator Validation
- Data Normalization
- Risk Scoring
- Report Generation
- Automation Pipeline

These capabilities mirror real-world Security Operations Center (SOC) workflows and provide a strong foundation for building enterprise-grade Threat Intelligence Platforms.

---

<div align="center">

### 🛡️ Threat Intelligence • Automation • SOC Operations • Cyber Defense

⭐ If you found this lab useful, consider starring the repository!

</div>
