# 🛡️ Identifying Malicious Attachments & URLs

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Threat%20Detection-red?style=for-the-badge&logo=hackthebox&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=ubuntu&logoColor=white)
![Malware](https://img.shields.io/badge/Malware-Analysis-critical?style=for-the-badge)
![URL](https://img.shields.io/badge/URL-Security-success?style=for-the-badge)
![Threat Detection](https://img.shields.io/badge/Threat-Detection-darkred?style=for-the-badge)

### 🔍 Attachment Analysis • 🌐 URL Inspection • 🚨 Threat Detection

</div>

---

# 📖 Overview

Email remains one of the most common attack vectors used by cybercriminals. Malicious attachments and phishing URLs are frequently used to distribute malware, steal credentials, and compromise systems.

In this lab, students will build a complete email security analysis platform capable of:

✅ Scanning file attachments

✅ Detecting suspicious file properties

✅ Calculating file hashes

✅ Analyzing URLs for phishing indicators

✅ Applying risk scoring methodologies

✅ Generating comprehensive security reports

✅ Performing integrated email security analysis

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- 🛡️ Analyze email attachments for malicious characteristics
- 🌐 Detect phishing and malware distribution URLs
- 🔑 Calculate MD5 and SHA256 file hashes
- 📊 Apply risk scoring methodologies
- 📄 Generate automated security reports
- 🚨 Identify suspicious file extensions and patterns
- 🔍 Perform integrated email security analysis

---

# 🧰 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming knowledge
- Linux command-line experience
- Understanding of file systems and file types
- Basic cybersecurity concepts (malware, phishing)

---

# 🏗️ Lab Environment

Al Nafi Cloud Machine provides:

- Ubuntu Linux
- Python 3.x
- Internet Connectivity
- Security Analysis Tools
- Development Environment

---

# 📂 Project Structure

```text
malware_lab/
│
├── attachments/
├── urls/
├── reports/
├── samples/
│   ├── document.txt
│   ├── script.sh
│   ├── invoice.pdf.exe
│   └── report.docx
│
├── attachment_scanner.py
├── url_analyzer.py
├── integrated_scanner.py
└── test_urls.txt
```

---

# 🚀 Task 1: File Attachment Analysis

## 🔹 Step 1: Create Lab Environment

```bash
mkdir -p ~/malware_lab/{attachments,urls,samples,reports}

cd ~/malware_lab
```

---

## 🔹 Step 2: Install Required Packages

```bash
pip3 install --user python-magic requests beautifulsoup4
```

```bash
sudo apt update
sudo apt install -y file libmagic1 python3-magic
```

---

# 📁 Create Test Files

## 🟢 Normal Text File

```bash
echo "Normal text document content" > ~/malware_lab/samples/document.txt
```

---

## 📜 Shell Script

```bash
echo -e "#!/bin/bash\necho 'Script content'" > ~/malware_lab/samples/script.sh

chmod +x ~/malware_lab/samples/script.sh
```

---

## ☠️ Suspicious Double Extension File

```bash
echo "Test content" > ~/malware_lab/samples/invoice.pdf.exe
```

---

## 📄 Legitimate Document

```bash
echo "Legitimate business document" > ~/malware_lab/samples/report.docx
```

---

# 🛡️ Task 2: Develop Attachment Scanner

## 📂 File: `attachment_scanner.py`

```python
#!/usr/bin/env python3

import os
import sys
import json
import hashlib
import magic
from datetime import datetime


class AttachmentScanner:

    def __init__(self):

        self.suspicious_extensions = [
            '.exe',
            '.scr',
            '.bat',
            '.cmd',
            '.vbs',
            '.js',
            '.jar',
            '.zip',
            '.rar'
        ]

        self.scan_results = []

    def calculate_hash(self, filepath):

        with open(filepath, "rb") as f:
            content = f.read()

        md5_hash = hashlib.md5(content).hexdigest()
        sha256_hash = hashlib.sha256(content).hexdigest()

        return md5_hash, sha256_hash

    def get_file_info(self, filepath):

        return {
            "size": os.path.getsize(filepath),
            "mime": magic.from_file(filepath, mime=True),
            "description": magic.from_file(filepath)
        }

    def calculate_risk_score(self, filepath, filename):

        score = 0
        warnings = []

        extension = os.path.splitext(filename)[1].lower()

        if extension in self.suspicious_extensions:
            score += 30
            warnings.append("Suspicious extension detected")

        if filename.count('.') > 1:
            score += 40
            warnings.append("Double extension detected")

        info = self.get_file_info(filepath)

        if "executable" in info["description"].lower():
            score += 25
            warnings.append("Executable file detected")

        if info["size"] < 100:
            score += 5
            warnings.append("Very small file size")

        return score, warnings

    def scan_file(self, filepath):

        filename = os.path.basename(filepath)

        md5_hash, sha256_hash = self.calculate_hash(filepath)

        info = self.get_file_info(filepath)

        score, warnings = self.calculate_risk_score(
            filepath,
            filename
        )

        if score >= 50:
            threat = "HIGH"
        elif score >= 25:
            threat = "MEDIUM"
        elif score >= 10:
            threat = "LOW"
        else:
            threat = "CLEAN"

        result = {
            "filename": filename,
            "risk_score": score,
            "threat_level": threat,
            "warnings": warnings,
            "md5": md5_hash,
            "sha256": sha256_hash,
            "file_info": info
        }

        self.scan_results.append(result)

        print(result)

    def scan_directory(self, directory):

        for file in os.listdir(directory):

            full_path = os.path.join(directory, file)

            if os.path.isfile(full_path):
                self.scan_file(full_path)

    def generate_report(self):

        with open("reports/attachment_report.json", "w") as f:
            json.dump(self.scan_results, f, indent=4)

        print("\nReport Saved: reports/attachment_report.json")


def main():

    scanner = AttachmentScanner()

    target = sys.argv[1]

    if os.path.isdir(target):
        scanner.scan_directory(target)
    else:
        scanner.scan_file(target)

    scanner.generate_report()


if __name__ == "__main__":
    main()
```

---

# ▶️ Run Attachment Scanner

```bash
chmod +x ~/malware_lab/attachment_scanner.py
```

```bash
python3 ~/malware_lab/attachment_scanner.py ~/malware_lab/samples/script.sh
```

```bash
python3 ~/malware_lab/attachment_scanner.py ~/malware_lab/samples/
```

---

# 🌐 Task 3: URL Analysis System

## 📄 Create Test URL List

```bash
cat > ~/malware_lab/test_urls.txt << 'EOF'
https://www.google.com
https://github.com
http://192.168.1.1/admin
https://bit.ly/shortened
https://secure-bank-verify.suspicious.com
https://www.microsoft.com
EOF
```

---

# 🔍 URL Analyzer

## 📂 File: `url_analyzer.py`

```python
#!/usr/bin/env python3

import requests
import re
import json
import urllib.parse
import sys


class URLAnalyzer:

    def __init__(self):

        self.results = []

        self.url_shorteners = [
            "bit.ly",
            "tinyurl.com",
            "goo.gl",
            "t.co"
        ]

    def extract_domain(self, url):

        return urllib.parse.urlparse(url).netloc

    def analyze_url_structure(self, url):

        score = 0
        warnings = []

        ip_regex = r"\d+\.\d+\.\d+\.\d+"

        if re.search(ip_regex, url):
            score += 25
            warnings.append("IP address used in URL")

        domain = self.extract_domain(url)

        if domain in self.url_shorteners:
            score += 20
            warnings.append("URL shortener detected")

        if len(url) > 200:
            score += 15
            warnings.append("Very long URL")

        return score, warnings

    def analyze_url(self, url):

        score, warnings = self.analyze_url_structure(url)

        if score >= 50:
            level = "HIGH"
        elif score >= 25:
            level = "MEDIUM"
        elif score >= 10:
            level = "LOW"
        else:
            level = "CLEAN"

        result = {
            "url": url,
            "score": score,
            "threat_level": level,
            "warnings": warnings
        }

        self.results.append(result)

        print(result)

    def analyze_url_list(self, filename):

        with open(filename) as f:

            for line in f:
                self.analyze_url(line.strip())

    def generate_report(self):

        with open("reports/url_report.json", "w") as f:
            json.dump(self.results, f, indent=4)


def main():

    analyzer = URLAnalyzer()

    target = sys.argv[1]

    if target.startswith("http"):
        analyzer.analyze_url(target)
    else:
        analyzer.analyze_url_list(target)

    analyzer.generate_report()


if __name__ == "__main__":
    main()
```

---

# ▶️ Run URL Analyzer

```bash
chmod +x ~/malware_lab/url_analyzer.py
```

```bash
python3 ~/malware_lab/url_analyzer.py https://www.google.com
```

```bash
python3 ~/malware_lab/url_analyzer.py ~/malware_lab/test_urls.txt
```

---

# 🔗 Task 4: Integrated Security Scanner

## 📂 File: `integrated_scanner.py`

```python
#!/usr/bin/env python3

import os
import re
from datetime import datetime


class EmailSecurityScanner:

    def __init__(self):

        self.results = {
            "attachments": [],
            "urls": [],
            "overall_risk": "CLEAN",
            "timestamp": datetime.now().isoformat()
        }

    def extract_urls_from_text(self, text):

        pattern = r'https?://[^\s]+'

        return re.findall(pattern, text)

    def analyze_email(self, email_file, attachments_dir):

        with open(email_file) as f:
            content = f.read()

        urls = self.extract_urls_from_text(content)

        self.results["urls"] = urls

        self.results["attachments"] = os.listdir(
            attachments_dir
        )

        print(self.results)

    def calculate_overall_risk(self):

        url_count = len(self.results["urls"])

        if url_count > 2:
            self.results["overall_risk"] = "HIGH"
        elif url_count > 0:
            self.results["overall_risk"] = "MEDIUM"

        return self.results["overall_risk"]


def main():

    import sys

    scanner = EmailSecurityScanner()

    scanner.analyze_email(
        sys.argv[1],
        sys.argv[2]
    )

    print(
        "Overall Risk:",
        scanner.calculate_overall_risk()
    )


if __name__ == "__main__":
    main()
```

---

# 📧 Sample Email

```bash
cat > ~/malware_lab/sample_email.txt << 'EOF'
Subject: Urgent Account Verification

Dear Customer,

Your account requires immediate verification. Click here:
https://secure-verify-account.suspicious-site.com/login

Please also review the attached security document.

Regards,
Security Team
EOF
```

---

# ▶️ Run Integrated Analysis

```bash
python3 ~/malware_lab/integrated_scanner.py \
~/malware_lab/sample_email.txt \
~/malware_lab/samples/
```

---

# 📊 Threat Scoring Model

| Indicator | Score |
|------------|---------|
| Suspicious Extension | +30 |
| Executable File | +25 |
| Double Extension | +40 |
| IP-based URL | +25 |
| URL Shortener | +20 |
| Long URL | +15 |

---

# 🚨 Threat Levels

| Score | Level |
|---------|---------|
| 0-9 | CLEAN |
| 10-24 | LOW |
| 25-49 | MEDIUM |
| 50+ | HIGH |

---

# 🛠️ Troubleshooting

## Import Errors

```bash
pip3 install --user python-magic requests beautifulsoup4
```

---

## Permission Errors

```bash
chmod +x *.py
```

---

## Magic Library Errors

```bash
sudo apt install libmagic1 python3-magic
```

---

## Network Timeout Issues

Increase timeout value inside:

```python
requests.get(url, timeout=10)
```

---

## Verify File Exists

```bash
ls -la ~/malware_lab/samples/
```

---

# 🎓 Learning Outcomes

After completing this lab, you will have:

✅ Built a File Attachment Scanner

✅ Implemented URL Threat Detection

✅ Calculated MD5 & SHA256 Hashes

✅ Generated Security Reports

✅ Applied Risk Scoring Techniques

✅ Built an Integrated Email Security Scanner

---

# 🏁 Conclusion

This lab provided practical experience in email security analysis through attachment scanning and URL inspection. You developed Python-based tools capable of identifying suspicious files, detecting phishing indicators, calculating risk scores, and generating automated reports.

These techniques are essential for modern cybersecurity professionals working in:

- Security Operations Centers (SOC)
- Incident Response
- Threat Hunting
- Malware Analysis
- Email Security Engineering

> 🚀 Continue expanding these tools by integrating VirusTotal APIs, machine learning detection models, sandbox analysis, and threat intelligence feeds.

---

<div align="center">

### 🛡️ Detect Threats • Analyze Risks • Secure Email Systems

⭐ Happy Hunting & Stay Secure! ⭐

</div>
