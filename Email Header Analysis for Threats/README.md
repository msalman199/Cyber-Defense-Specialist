# 📧 Email Header Analysis for Threats

<div align="center">

![Cybersecurity](https://img.shields.io/badge/Cybersecurity-Email%20Security-red?style=for-the-badge&logo=protonmail&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?style=for-the-badge&logo=ubuntu&logoColor=white)
![DNS](https://img.shields.io/badge/DNS-Analysis-green?style=for-the-badge&logo=cloudflare&logoColor=white)
![SPF](https://img.shields.io/badge/SPF-Validation-success?style=for-the-badge)
![DKIM](https://img.shields.io/badge/DKIM-Verification-blueviolet?style=for-the-badge)
![DMARC](https://img.shields.io/badge/DMARC-Policy%20Check-important?style=for-the-badge)

### 🛡️ Email Security | 🔍 Threat Detection | 📊 Threat Intelligence

</div>

---

# 📖 Overview

Email remains one of the most common attack vectors used by cybercriminals. Attackers frequently exploit phishing, spoofing, malware attachments, and social engineering techniques to compromise organizations.

In this hands-on lab, students will build a complete email threat analysis platform capable of:

✅ Parsing email headers

✅ Detecting phishing indicators

✅ Validating SPF records

✅ Verifying DKIM signatures

✅ Checking DMARC policies

✅ Calculating threat scores

✅ Generating automated security reports

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- 📧 Parse and analyze email headers
- 🔍 Identify phishing indicators
- 🛡️ Implement SPF validation
- 🔐 Implement DKIM verification
- 📜 Validate DMARC policies
- 🤖 Create automated threat analysis tools
- 📊 Generate threat scores
- 🚨 Detect email spoofing attempts
- 📈 Produce comprehensive threat reports

---

# 🧰 Prerequisites

Before starting this lab, ensure you have:

- Basic Python programming skills
- Understanding of SMTP and IMAP
- Familiarity with DNS concepts
- Linux command-line experience
- Basic cybersecurity knowledge

---

# 🏗️ Lab Environment

Al Nafi Cloud provides a pre-configured Linux machine with:

- Python 3
- DNS Utilities
- Email Analysis Libraries
- Network Connectivity
- Development Environment

---

# 📂 Project Structure

```text
email_lab/
│
├── samples/
│   ├── legitimate.eml
│   ├── phishing.eml
│   └── malware.eml
│
├── scripts/
│   ├── header_analyzer.py
│   ├── spf_validator.py
│   ├── dkim_validator.py
│   ├── dmarc_validator.py
│   └── threat_reporter.py
│
└── output/
```

---

# 🚀 Task 1: Setting Up Email Analysis Environment

## 🔹 Step 1: Create Lab Workspace

```bash
mkdir -p ~/email_lab/{samples,scripts,output}

cd ~/email_lab
```

---

## 🔹 Step 2: Verify Python Installation

```bash
python3 --version
```

Expected Output:

```text
Python 3.x.x
```

---

## 🔹 Step 3: Install Required Packages

```bash
pip3 install dnspython email-validator
```

---

# 📧 Task 2: Create Sample Email Headers

## 🟢 Legitimate Email Sample

```bash
cat > samples/legitimate.eml << 'EOF'
Return-Path: <sender@company.com>
Received: from mail.company.com (mail.company.com [192.0.2.10])
    by mx.recipient.com with ESMTP id ABC123
From: John Doe <sender@company.com>
To: recipient@recipient.com
Subject: Quarterly Report
Date: Mon, 15 Jan 2024 10:30:00 +0000
Message-ID: <msg123@company.com>
DKIM-Signature: v=1; a=rsa-sha256; d=company.com; s=default;
    h=from:to:subject; bh=abc123; b=xyz789
SPF: pass

Please review the attached quarterly report.
EOF
```

---

## 🔴 Phishing Email Sample

```bash
cat > samples/phishing.eml << 'EOF'
Return-Path: <alert@security-bank-verify.net>
Received: from suspicious.example.com (suspicious.example.com [203.0.113.50])
    by mx.victim.com with SMTP id XYZ789
From: Bank Security <security@yourbank.com>
Reply-To: noreply@security-bank-verify.net
To: victim@victim.com
Subject: URGENT: Verify Your Account Now
Date: Tue, 16 Jan 2024 14:20:00 +0000
X-Mailer: BulkMailer Pro
X-Originating-IP: 203.0.113.50

Your account will be suspended. Click here immediately to verify.
EOF
```

---

## ☠️ Malware Email Sample

```bash
cat > samples/malware.eml << 'EOF'
Return-Path: <invoice@fake-vendor.biz>
Received: from compromised.host.org (compromised.host.org [198.51.100.25])
    by mx.target.com with ESMTP id MAL456
From: Accounting <billing@legitimate-vendor.com>
To: target@target.com
Subject: Invoice #2024-001 Payment Due
Date: Wed, 17 Jan 2024 09:15:00 +0000
X-Attachment: invoice.pdf.exe
X-Spam-Score: 8.5

Attached invoice requires immediate payment.
EOF
```

---

# 🔍 Task 3: Build Email Header Analyzer

## 🎯 Purpose

The Email Header Analyzer will:

- Extract critical email metadata
- Identify spoofing attempts
- Detect suspicious routing paths
- Examine email content
- Calculate threat scores

---

## 📝 Create Header Analyzer

```bash
nano scripts/header_analyzer.py
```

Paste the provided starter template into the file.

Make executable:

```bash
chmod +x scripts/header_analyzer.py
```

---

## ▶️ Execute Analyzer

```bash
python3 scripts/header_analyzer.py
```

---

# 🛡️ Task 4: Implement SPF Validation

## 📖 What is SPF?

SPF (Sender Policy Framework) allows domain owners to specify which mail servers are authorized to send emails on behalf of their domain.

Benefits:

✅ Prevents spoofing

✅ Reduces phishing attacks

✅ Improves email trust

---

## 📝 Create SPF Validator

```bash
nano scripts/spf_validator.py
```

Paste the provided SPF Validator template.

Make executable:

```bash
chmod +x scripts/spf_validator.py
```

---

## ▶️ Run SPF Validation

```bash
python3 scripts/spf_validator.py
```

Expected Output:

```text
Validating SPF: company.com from 192.0.2.10
Result: Pass
```

---

# 🔐 Task 5: Implement DKIM Validation

## 📖 What is DKIM?

DKIM (DomainKeys Identified Mail) digitally signs outgoing emails.

Benefits:

- Ensures message integrity
- Prevents tampering
- Verifies sender authenticity

---

## 📝 Create DKIM Validator

```bash
nano scripts/dkim_validator.py
```

Paste the provided DKIM template.

Make executable:

```bash
chmod +x scripts/dkim_validator.py
```

---

## ▶️ Execute DKIM Validation

```bash
python3 scripts/dkim_validator.py
```

---

# 📜 Task 6: Implement DMARC Validation

## 📖 What is DMARC?

DMARC combines SPF and DKIM results to determine whether an email should be trusted.

Policies:

| Policy | Action |
|----------|----------|
| none | Monitor only |
| quarantine | Send to spam |
| reject | Block message |

---

## 📝 Create DMARC Validator

```bash
nano scripts/dmarc_validator.py
```

Paste the provided DMARC template.

Make executable:

```bash
chmod +x scripts/dmarc_validator.py
```

---

## ▶️ Execute DMARC Validation

```bash
python3 scripts/dmarc_validator.py
```

---

# 📊 Task 7: Create Integrated Threat Reporter

## 🎯 Purpose

This component combines:

- Header Analysis
- SPF Validation
- DKIM Verification
- DMARC Validation
- Threat Scoring

into a single report.

---

## 📝 Create Threat Reporter

```bash
nano scripts/threat_reporter.py
```

Paste the provided starter template.

Make executable:

```bash
chmod +x scripts/threat_reporter.py
```

---

## ▶️ Run Integrated Analysis

```bash
python3 scripts/threat_reporter.py
```

---

# 📈 Threat Scoring Model

| Indicator | Points |
|------------|----------|
| Spoofing Indicator | +3 |
| Suspicious Content | +2 |
| Suspicious IP | +4 |

---

## 🚨 Threat Levels

| Score | Level |
|---------|---------|
| 0 | Minimal |
| 1-4 | Low |
| 5-9 | Medium |
| 10+ | High |

---

# 📄 Generated Reports

Example:

```json
{
  "file": "phishing.eml",
  "spf_result": "Fail",
  "dkim_result": false,
  "dmarc_result": "Reject",
  "threat_score": 14,
  "threat_level": "HIGH"
}
```

---

# 🧪 Testing Checklist

## ✅ Header Analysis

```bash
python3 scripts/header_analyzer.py
```

---

## ✅ SPF Validation

```bash
python3 scripts/spf_validator.py
```

---

## ✅ DKIM Validation

```bash
python3 scripts/dkim_validator.py
```

---

## ✅ DMARC Validation

```bash
python3 scripts/dmarc_validator.py
```

---

## ✅ Complete Threat Report

```bash
python3 scripts/threat_reporter.py
```

---

# 🛠️ Troubleshooting

## DNS Resolution Errors

```bash
echo "nameserver 8.8.8.8" | sudo tee /etc/resolv.conf
```

---

## Python Import Errors

```bash
export PYTHONPATH=$PYTHONPATH:~/email_lab/scripts
```

```bash
pip3 install --upgrade dnspython email-validator
```

---

## File Permission Errors

```bash
chmod +x scripts/*.py
```

```bash
chmod 644 samples/*.eml
```

---

## Verify Permissions

```bash
ls -la samples/
```

---

# 🎓 Learning Outcomes

After completing this lab, you will have:

✅ Built an Email Header Parser

✅ Implemented SPF Validation

✅ Implemented DKIM Verification

✅ Implemented DMARC Policy Checking

✅ Created Automated Threat Detection Tools

✅ Generated Comprehensive Security Reports

✅ Detected Phishing and Spoofing Attempts

✅ Improved Email Security Analysis Skills

---

# 🔑 Key Takeaways

### 📧 Email headers contain valuable security intelligence.

### 🛡️ SPF validates authorized senders.

### 🔐 DKIM verifies email integrity.

### 📜 DMARC enforces authentication policies.

### 🚨 Threat scoring improves detection accuracy.

### 🤖 Automation accelerates email security investigations.

---

# 🏁 Conclusion

This lab provided practical experience in email threat analysis and authentication technologies. You developed tools capable of identifying phishing attempts, validating email authenticity, detecting spoofing indicators, and generating comprehensive threat reports.

By combining SPF, DKIM, and DMARC validation with automated threat scoring, security analysts can significantly improve their ability to detect and respond to email-based attacks.

> 🚀 Continue expanding the project by integrating machine learning, threat intelligence feeds, and real-world email samples to build enterprise-grade email security solutions.

---

<div align="center">

### 🛡️ Secure Emails • Detect Threats • Defend Organizations

⭐ Happy Hunting & Stay Secure! ⭐

</div>
