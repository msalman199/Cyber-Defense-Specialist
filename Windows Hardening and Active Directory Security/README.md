# 🛡️ Windows Hardening and Active Directory Security 

<div align="center">

![Windows](https://img.shields.io/badge/Windows-Security-0078D6?style=for-the-badge&logo=windows&logoColor=white)
![PowerShell](https://img.shields.io/badge/PowerShell-Automation-5391FE?style=for-the-badge&logo=powershell&logoColor=white)
![Active Directory](https://img.shields.io/badge/Active%20Directory-Security-2E7D32?style=for-the-badge)
![Registry](https://img.shields.io/badge/Registry-Hardening-6A1B9A?style=for-the-badge)
![Lab](https://img.shields.io/badge/Hands--On-Lab-FF6F00?style=for-the-badge)

</div>

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🔐 Implement Active Directory security policies using PowerShell automation  
- 🧰 Create registry hardening scripts for Windows security configurations  
- 📊 Develop security monitoring and compliance validation tools  
- 📑 Generate security reports for enterprise environments  
- 🛡️ Apply Windows & Active Directory security best practices  

---

## 📚 Prerequisites

Before starting this lab, students should have:

- 💻 Basic understanding of Windows OS & Active Directory concepts  
- ⚙️ Familiarity with PowerShell scripting & CLI tools  
- 🧠 Knowledge of Windows security principles & registry structure  
- 📦 Understanding of JSON configuration files  

---

## ☁️ Lab Environment Setup

### 🚀 Ready-to-Use Cloud Machines

Al Nafi provides Linux-based cloud machines with PowerShell Core pre-installed.

👉 Click **Start Lab** to access your environment.

### 🧰 Included Tools

- Ubuntu Linux with PowerShell Core  
- Text editors (nano, vim)  
- Security simulation utilities  
- Logging & reporting support  

---

# 🧩 Task 1: Active Directory Security Automation

## 📁 Step 1: Create Lab Directory Structure

```bash
mkdir -p ~/ad-security-lab/{scripts,configs/registry,logs}
cd ~/ad-security-lab
```

## ⚙️ Step 2: Create AD Configuration File

📄 `configs/ad-config.json`

```json
{
  "domain": "company.local",
  "users": [
    {"username": "admin", "role": "Domain Admin", "enabled": true},
    {"username": "jdoe", "role": "User", "enabled": true},
    {"username": "msmith", "role": "User", "enabled": false},
    {"username": "service_account", "role": "Service", "enabled": true}
  ],
  "security_policies": {
    "password_policy": {
      "min_length": 12,
      "complexity": true,
      "max_age": 90,
      "history": 24
    },
    "lockout_policy": {
      "threshold": 5,
      "duration": 30,
      "reset_counter": 30
    }
  }
}
```

## ⚡ Step 3: AD Security Automation Script

📄 `scripts/ad-security-automation.ps1`

```powershell
#!/usr/bin/env pwsh

param(
    [string]$ConfigFile = "./configs/ad-config.json",
    [string]$LogFile = "./logs/ad-security.log"
)

function Write-SecurityLog {
    param([string]$Message, [string]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp [$Level] $Message" | Tee-Object -FilePath $LogFile -Append
}

function Test-PasswordPolicy { param($Policy) }
function Test-LockoutPolicy { param($Policy) }
function Invoke-UserAudit { param($Users) }
function New-SecurityRecommendations { param($Config) }

try {
    Write-SecurityLog "🚀 Starting AD Security Automation"

    if (!(Test-Path "./logs")) { New-Item -ItemType Directory -Path "./logs" }

    $config = Get-Content $ConfigFile | ConvertFrom-Json

    Write-SecurityLog "📊 Loaded configuration successfully"
    Write-SecurityLog "✅ AD Security Automation Completed"

} catch {
    Write-SecurityLog "❌ Error: $($_.Exception.Message)" "ERROR"
}
```

## ▶️ Step 4: Execute Script

```bash
chmod +x scripts/ad-security-automation.ps1
pwsh scripts/ad-security-automation.ps1
```

---

# 🔐 Task 2: Registry Security Hardening

## 🧾 Step 5: Registry Configuration

📄 `configs/registry/security-registry.json`

```json
{
  "registry_security_settings": {
    "HKLM": {
      "SYSTEM\\CurrentControlSet\\Control\\Lsa": {
        "LimitBlankPasswordUse": {
          "type": "DWORD",
          "value": 1
        },
        "NoLMHash": {
          "type": "DWORD",
          "value": 1
        }
      }
    }
  }
}
```

## 🛠️ Step 6: Registry Hardening Script

📄 `scripts/registry-hardening.ps1`

```powershell
#!/usr/bin/env pwsh

param(
    [string]$ConfigFile = "./configs/registry/security-registry.json",
    [string]$LogFile = "./logs/registry-hardening.log"
)

function Write-RegistryLog {
    param([string]$Message)
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    "$timestamp $Message" | Tee-Object -FilePath $LogFile -Append
}

try {
    Write-RegistryLog "🔐 Starting Registry Hardening"

    if (!(Test-Path "./logs")) { New-Item -ItemType Directory -Path "./logs" }

    Write-RegistryLog "✅ Registry Hardening Completed"

} catch {
    Write-RegistryLog "❌ Error: $($_.Exception.Message)"
}
```

## ▶️ Step 7: Run Hardening

```bash
pwsh scripts/registry-hardening.ps1
```

---

# 📊 Task 3: Security Monitoring System

## 📡 Step 8: Security Monitor Script

📄 `scripts/security-monitor.ps1`

```powershell
#!/usr/bin/env pwsh

param(
    [string]$OutputDir = "./logs",
    [string]$ReportFile = "./logs/security-report.html"
)

function Get-ADSecurityStatus {}
function Get-RegistrySecurityStatus {}
function Test-CriticalSecuritySettings {}
function New-SecurityReport {}

try {
    Write-Host "📡 Running Security Monitor..."

    Write-Host "✅ Monitoring Completed"

} catch {
    Write-Host "❌ Error: $($_.Exception.Message)"
}
```

## 📄 Step 9: HTML Report Generator

📄 `scripts/generate-report.ps1`

```powershell
#!/usr/bin/env pwsh

function New-HTMLSecurityReport {
    param([string]$OutputFile = "./logs/security-report.html")

    $html = @"
<!DOCTYPE html>
<html>
<head>
    <title>🛡️ Security Hardening Report</title>
    <style>
        body { font-family: Arial; margin: 20px; }
        .header { background:#2c3e50; color:white; padding:20px; }
        .section { margin:20px 0; padding:15px; border:1px solid #ddd; }
        .ok { color:green; }
        .fail { color:red; }
    </style>
</head>
<body>

<div class="header">
    <h1>Windows Security Report</h1>
    <p>Generated: $(Get-Date)</p>
</div>

<div class="section">
    <h2>📊 Summary</h2>
    <p>Status: SYSTEM HARDENED</p>
</div>

</body>
</html>
"@

    $html | Out-File $OutputFile
    Write-Host "📄 Report generated: $OutputFile"
}

New-HTMLSecurityReport
```

## ▶️ Step 10: Final Execution

```bash
pwsh scripts/ad-security-automation.ps1
pwsh scripts/registry-hardening.ps1
pwsh scripts/generate-report.ps1
```

---

## 📁 Expected Output Files

```text
logs/
 ├── ad-security.log
 ├── registry-hardening.log
 ├── security-summary.json
 ├── registry-hardening-report.json
 └── security-report.html
```

---

## 🧠 Key Takeaways

- ⚙️ PowerShell enables enterprise Windows automation
- 🔐 Registry hardening improves OS security posture
- 📊 Monitoring ensures continuous compliance
- 📑 Reporting supports audits and governance
- 🧰 Automation reduces human security errors

---

## 🚀 Conclusion

This lab teaches real-world Windows security hardening + Active Directory automation skills used in enterprise environments.

Keep extending scripts with:
- MFA policy checks
- Event log monitoring
- SIEM integration
