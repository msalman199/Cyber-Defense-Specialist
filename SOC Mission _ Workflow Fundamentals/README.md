# 🏢 SOC Mission & Workflow Fundamentals 

![SOC](https://img.shields.io/badge/SOC-Security%20Operations-darkblue?style=for-the-badge&logo=shield&logoColor=white)
![ELK](https://img.shields.io/badge/ELK-Stack-005571?style=for-the-badge&logo=elastic&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Log%20Storage-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Dashboard-E8478B?style=for-the-badge&logo=kibana&logoColor=white)
![ElastAlert](https://img.shields.io/badge/ElastAlert-Alerting-orange?style=for-the-badge&logo=python&logoColor=white)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)

---

## 🎯 Objectives

By the end of this lab, students will be able to:

- 🏛️ Define the **mission and purpose** of a Security Operations Center (SOC)
- 📊 Understand **SOC maturity levels** and their characteristics
- ⚙️ Set up and configure a **basic SIEM tool** using open-source software
- 🚨 Create and configure **alerting systems** for security monitoring
- 📋 Implement basic **log collection and analysis** workflows
- 🔍 Demonstrate understanding of **SOC operational procedures**

---

## ✅ Prerequisites

| Requirement | Description |
|---|---|
| 🖥️ Linux CLI | Basic understanding of Linux command line operations |
| 🌐 Networking | Fundamental knowledge of IP addresses, ports, protocols |
| 🛡️ Cybersecurity | Basic understanding of cybersecurity terminology |
| ✏️ Text Editors | Familiarity with `nano`, `vim`, or `gedit` |

---

## 🧪 Lab Environment

> 💡 **Al Nafi** provides Linux-based cloud machines for this lab.  
> Click **Start Lab** to access your pre-configured **Ubuntu 20.04 LTS** machine.  
> No additional VM setup is required.

---

# 📋 Task 1 — Define SOC Mission and Maturity Levels

![SOC](https://img.shields.io/badge/SOC-Mission%20%26%20Maturity-darkblue?style=flat-square)
![Docs](https://img.shields.io/badge/Documentation-Creation-blue?style=flat-square)

---

## 🏛️ Subtask 1.1 — Understanding SOC Mission

> 💡 A **Security Operations Center (SOC)** is a centralized facility where security professionals monitor, detect, analyze, and respond to cybersecurity incidents on a **24/7** basis.

**🎯 Core SOC Mission Components:**

| Component | Description |
|---|---|
| 🛡️ Prevention | Implementing security controls to prevent incidents |
| 🔍 Detection | Identifying potential security threats and anomalies |
| ⚡ Response | Taking immediate action to contain and mitigate threats |
| 🔁 Recovery | Restoring normal operations after incidents |
| 📈 Improvement | Learning from incidents to strengthen security posture |

---

## 📊 Subtask 1.2 — SOC Maturity Levels

SOC maturity is typically categorized into **five levels**:

| Level | Name | Key Characteristics |
|---|---|---|
| 1️⃣ | **Initial / Ad Hoc** | Reactive approach, limited docs, manual IR, basic monitoring |
| 2️⃣ | **Developing** | Some documented procedures, basic SIEM, defined IR team |
| 3️⃣ | **Defined** | Standardized processes, integrated tools, proactive threat hunting |
| 4️⃣ | **Managed** | Quantitative management, advanced analytics, threat intel integration |
| 5️⃣ | **Optimizing** | Continuous optimization, advanced threat prediction, full automation |

---

## 📄 Subtask 1.3 — Create SOC Documentation

📁 **Create a directory for SOC documentation:**

```bash
mkdir -p ~/soc-lab/documentation
```

✏️ **Create the SOC mission statement file:**

```bash
cat > ~/soc-lab/documentation/soc-mission.txt << 'EOF'
SOC MISSION STATEMENT
====================

Mission: To provide continuous monitoring, detection, and response to cybersecurity 
threats while maintaining the confidentiality, integrity, and availability of 
organizational assets.

Core Objectives:
1. Monitor network traffic and system logs 24/7
2. Detect and analyze security incidents
3. Respond to threats in a timely manner
4. Document and report security events
5. Continuously improve security posture

Key Performance Indicators:
- Mean Time to Detection (MTTD)
- Mean Time to Response (MTTR)
- Number of incidents detected and resolved
- False positive rate
- System availability percentage

SOC Maturity Level: Level 2 (Developing)
Target Maturity Level: Level 3 (Defined)
EOF
```

📋 **Display the mission statement:**

```bash
cat ~/soc-lab/documentation/soc-mission.txt
```

---

# 📋 Task 2 — Set Up Basic SIEM Tool and Configure Alerting System

![ELK](https://img.shields.io/badge/ELK-Stack%20Setup-005571?style=flat-square&logo=elastic&logoColor=white)
![Logstash](https://img.shields.io/badge/Logstash-Log%20Pipeline-F9A013?style=flat-square&logo=logstash&logoColor=white)
![ElastAlert](https://img.shields.io/badge/ElastAlert-Alert%20Rules-orange?style=flat-square)

---

## ⚙️ Subtask 2.1 — Install and Configure ELK Stack

> 💡 We'll use the **ELK stack** (Elasticsearch, Logstash, Kibana) as our open-source SIEM solution.

---

### ☕ Step 1 — Update System and Install Java

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk
java -version
```

---

### 🔍 Step 2 — Install Elasticsearch

📋 **Add Elasticsearch repository:**

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/elastic-7.x.list
sudo apt update
sudo apt install -y elasticsearch
```

📄 **Configure Elasticsearch:**

```bash
sudo sed -i 's/#network.host: 192.168.0.1/network.host: localhost/' \
  /etc/elasticsearch/elasticsearch.yml
sudo sed -i 's/#http.port: 9200/http.port: 9200/' \
  /etc/elasticsearch/elasticsearch.yml
```

🚀 **Start and enable Elasticsearch:**

```bash
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch
sleep 30
```

✅ **Test Elasticsearch:**

```bash
curl -X GET "localhost:9200/"
```

---

### 📊 Step 3 — Install Kibana

📥 **Install and configure Kibana:**

```bash
sudo apt install -y kibana

sudo sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/' \
  /etc/kibana/kibana.yml
sudo sed -i 's/#elasticsearch.hosts:/elasticsearch.hosts:/' \
  /etc/kibana/kibana.yml
```

🚀 **Start and enable Kibana:**

```bash
sudo systemctl start kibana
sudo systemctl enable kibana
sleep 60
```

---

### 🔄 Step 4 — Install Logstash

📥 **Install Logstash:**

```bash
sudo apt install -y logstash
sudo mkdir -p /etc/logstash/conf.d
```

📄 **Create a basic Logstash configuration:**

```bash
cat > /tmp/logstash-syslog.conf << 'EOF'
input {
  file {
    path => "/var/log/syslog"
    start_position => "beginning"
    type => "syslog"
  }
  file {
    path => "/var/log/auth.log"
    start_position => "beginning"
    type => "auth"
  }
}

filter {
  if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:message}" }
    }
  }

  if [type] == "auth" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:auth_message}" }
    }
  }
}

output {
  elasticsearch {
    hosts => ["localhost:9200"]
    index => "soc-logs-%{+YYYY.MM.dd}"
  }
  stdout { codec => rubydebug }
}
EOF

sudo mv /tmp/logstash-syslog.conf /etc/logstash/conf.d/
```

🚀 **Start and enable Logstash:**

```bash
sudo systemctl start logstash
sudo systemctl enable logstash
```

---

## 📋 Subtask 2.2 — Configure Log Collection and Monitoring

### 🎭 Step 1 — Create Sample Security Events

📁 **Create the scripts directory:**

```bash
mkdir -p ~/soc-lab/scripts
```

✏️ **Create a script to generate sample security events:**

```bash
cat > ~/soc-lab/scripts/generate-events.sh << 'EOF'
#!/bin/bash

# Generate failed SSH login attempts
logger -p auth.warning "sshd[1234]: Failed password for invalid user admin from 192.168.1.100 port 22 ssh2"
logger -p auth.warning "sshd[1235]: Failed password for invalid user root from 10.0.0.50 port 22 ssh2"

# Generate successful login
logger -p auth.info "sshd[1236]: Accepted password for user from 192.168.1.10 port 22 ssh2"

# Generate suspicious network activity
logger -p daemon.warning "kernel: [UFW BLOCK] IN=eth0 OUT= MAC= SRC=192.168.1.200 DST=192.168.1.1 PROTO=TCP SPT=12345 DPT=22"

# Generate system events
logger -p daemon.info "systemd[1]: Started Security monitoring service"
logger -p daemon.warning "systemd[1]: Failed to start suspicious-service.service"

echo "Sample security events generated and logged"
EOF

chmod +x ~/soc-lab/scripts/generate-events.sh
~/soc-lab/scripts/generate-events.sh
```

---

### 🔍 Step 2 — Verify Data in Elasticsearch

⏳ **Wait for Logstash to process logs:**

```bash
sleep 60
```

📊 **Check indexed data:**

```bash
curl -X GET "localhost:9200/_cat/indices?v"
```

🔎 **Search for recent logs:**

```bash
curl -X GET "localhost:9200/soc-logs-*/_search?pretty" \
  -H 'Content-Type: application/json' -d'
{
  "query": { "match_all": {} },
  "size": 5,
  "sort": [{ "@timestamp": { "order": "desc" } }]
}'
```

---

## 🚨 Subtask 2.3 — Configure Alerting System

### 📦 Step 1 — Install ElastAlert

```bash
sudo apt install -y python3-pip
sudo pip3 install elastalert

sudo mkdir -p /etc/elastalert/rules
sudo mkdir -p /var/log/elastalert
```

📄 **Create ElastAlert configuration:**

```bash
cat > /tmp/elastalert-config.yaml << 'EOF'
rules_folder: /etc/elastalert/rules
run_every:
  minutes: 1
buffer_time:
  minutes: 15
es_host: localhost
es_port: 9200
writeback_index: elastalert_status
alert_time_limit:
  days: 2
EOF

sudo mv /tmp/elastalert-config.yaml /etc/elastalert/config.yaml
```

---

### 📜 Step 2 — Create Alerting Rules

🔐 **Create a rule for failed SSH login attempts:**

```bash
cat > /tmp/failed-ssh-rule.yaml << 'EOF'
name: Failed SSH Login Attempts
type: frequency
index: soc-logs-*
num_events: 3
timeframe:
  minutes: 5

filter:
- terms:
    message: ["Failed password", "authentication failure"]

alert:
- "email"
- "debug"

email:
- "soc-admin@company.com"

alert_text: |
  Multiple failed SSH login attempts detected!
  
  Time: {0}
  Host: {1}
  Message: {2}
  
  This could indicate a brute force attack.

alert_text_args:
  - "@timestamp"
  - "host"
  - "message"

include:
  - "@timestamp"
  - "host"
  - "message"
  - "program"
EOF

sudo mv /tmp/failed-ssh-rule.yaml /etc/elastalert/rules/
```

🌐 **Create a rule for blocked network connections:**

```bash
cat > /tmp/blocked-connections-rule.yaml << 'EOF'
name: Blocked Network Connections
type: frequency
index: soc-logs-*
num_events: 5
timeframe:
  minutes: 10

filter:
- terms:
    message: ["UFW BLOCK", "DENIED"]

alert:
- "debug"

alert_text: |
  Multiple blocked network connections detected!
  
  Time: {0}
  Message: {1}
  
  This could indicate a network scan or attack attempt.

alert_text_args:
  - "@timestamp"
  - "message"

include:
  - "@timestamp"
  - "host"
  - "message"
EOF

sudo mv /tmp/blocked-connections-rule.yaml /etc/elastalert/rules/
```

> **📋 Alert Rules Summary:**

| Rule | Trigger | Threshold | Priority |
|---|---|---|---|
| 🔐 Failed SSH Logins | `"Failed password"` / `"authentication failure"` | 3 events in 5 min | 🔴 High |
| 🌐 Blocked Connections | `"UFW BLOCK"` / `"DENIED"` | 5 events in 10 min | 🟠 Medium |

---

### ▶️ Step 3 — Initialize and Test ElastAlert

🔧 **Create ElastAlert index:**

```bash
elastalert-create-index --config /etc/elastalert/config.yaml
```

🧪 **Test the rules:**

```bash
elastalert-test-rule --config /etc/elastalert/config.yaml \
  /etc/elastalert/rules/failed-ssh-rule.yaml
```

🚀 **Start ElastAlert in the background:**

```bash
nohup elastalert --config /etc/elastalert/config.yaml --verbose \
  > /var/log/elastalert/elastalert.log 2>&1 &

echo "ElastAlert started. Check logs with: tail -f /var/log/elastalert/elastalert.log"
```

---

## 🖥️ Subtask 2.4 — Create SOC Dashboard and Monitoring Scripts

### 📊 Step 1 — Create a SOC Monitoring Dashboard Script

```bash
cat > ~/soc-lab/scripts/soc-dashboard.sh << 'EOF'
#!/bin/bash

clear
echo "=================================="
echo "    SOC MONITORING DASHBOARD     "
echo "=================================="
echo ""

# Check system status
echo "SYSTEM STATUS:"
echo "- Elasticsearch: $(systemctl is-active elasticsearch)"
echo "- Kibana: $(systemctl is-active kibana)"
echo "- Logstash: $(systemctl is-active logstash)"
echo ""

# Check recent log entries
echo "RECENT SECURITY EVENTS (Last 10):"
echo "-----------------------------------"
tail -10 /var/log/auth.log | grep -E "(Failed|Accepted|Invalid)" || \
  echo "No recent authentication events"
echo ""

# Check ElastAlert status
echo "ALERT SYSTEM STATUS:"
echo "--------------------"
if pgrep -f elastalert > /dev/null; then
    echo "- ElastAlert: RUNNING"
    echo "- Recent alerts: $(tail -5 /var/log/elastalert/elastalert.log | \
      grep -c "Alert sent" || echo "0")"
else
    echo "- ElastAlert: STOPPED"
fi
echo ""

# Check Elasticsearch indices
echo "ELASTICSEARCH INDICES:"
echo "----------------------"
curl -s "localhost:9200/_cat/indices?v" | grep soc-logs || \
  echo "No SOC indices found"
echo ""

echo "Last Updated: $(date)"
echo "=================================="
EOF

chmod +x ~/soc-lab/scripts/soc-dashboard.sh
```

---

### 📄 Step 2 — Create Incident Response Procedures

```bash
cat > ~/soc-lab/documentation/incident-response.txt << 'EOF'
INCIDENT RESPONSE PROCEDURES
============================

PHASE 1: PREPARATION
- Ensure all monitoring tools are operational
- Verify alert systems are functioning
- Review contact lists and escalation procedures

PHASE 2: IDENTIFICATION
- Monitor alerts from SIEM system
- Analyze log entries for anomalies
- Classify incident severity:
  * LOW:      Minor policy violations
  * MEDIUM:   Potential security threats
  * HIGH:     Active attacks or breaches
  * CRITICAL: System compromise confirmed

PHASE 3: CONTAINMENT
- Isolate affected systems if necessary
- Preserve evidence for analysis
- Implement temporary fixes to prevent spread

PHASE 4: ERADICATION
- Remove malware or unauthorized access
- Patch vulnerabilities
- Update security controls

PHASE 5: RECOVERY
- Restore systems to normal operation
- Monitor for recurring issues
- Validate system integrity

PHASE 6: LESSONS LEARNED
- Document incident details
- Update procedures based on findings
- Conduct post-incident review

ESCALATION CONTACTS:
- SOC Manager:        ext. 1001
- IT Security Team:   ext. 1002
- Network Operations: ext. 1003
- Management:         ext. 1000
EOF
```

---

## 🧪 Subtask 2.5 — Test the Complete SOC Setup

### 🎭 Step 1 — Generate Test Incidents and Verify Detection

🔐 **Generate multiple failed login attempts to trigger alerts:**

```bash
for i in {1..5}; do
    logger -p auth.warning "sshd[$(($RANDOM + 1000))]: Failed password for invalid user hacker$i \
      from 192.168.1.$(($RANDOM % 255)) port 22 ssh2"
    sleep 2
done
```

🌐 **Generate blocked connection attempts:**

```bash
for i in {1..7}; do
    logger -p daemon.warning "kernel: [UFW BLOCK] IN=eth0 OUT= MAC= \
      SRC=10.0.0.$(($RANDOM % 255)) DST=192.168.1.1 PROTO=TCP \
      SPT=$(($RANDOM + 10000)) DPT=22"
    sleep 1
done

echo "Test incidents generated. Waiting for processing..."
sleep 30
```

---

### 📊 Step 2 — Run the SOC Dashboard

```bash
~/soc-lab/scripts/soc-dashboard.sh
```

---

### 🔍 Step 3 — Check for Alerts

📋 **Check ElastAlert logs for triggered alerts:**

```bash
echo "CHECKING FOR TRIGGERED ALERTS:"
echo "==============================="
tail -20 /var/log/elastalert/elastalert.log | \
  grep -E "(Alert|ERROR|WARNING)" || echo "No alerts found in recent logs"
```

🔎 **Verify data in Elasticsearch:**

```bash
curl -s -X GET "localhost:9200/soc-logs-*/_search?pretty" \
  -H 'Content-Type: application/json' -d'
{
  "query": {
    "bool": {
      "should": [
        {"match": {"message": "Failed password"}},
        {"match": {"message": "UFW BLOCK"}}
      ]
    }
  },
  "size": 3,
  "sort": [{"@timestamp": {"order": "desc"}}]
}' | grep -E "(timestamp|message|host)" || echo "No matching events found"
```

---

## 🗂️ Subtask 2.6 — Create SOC Operational Procedures

✏️ **Create the SOC operations menu script:**

```bash
cat > ~/soc-lab/scripts/soc-operations.sh << 'EOF'
#!/bin/bash

while true; do
    clear
    echo "=================================="
    echo "    SOC OPERATIONS MENU          "
    echo "=================================="
    echo "1. View Dashboard"
    echo "2. Generate Test Events"
    echo "3. Check System Status"
    echo "4. View Recent Alerts"
    echo "5. Search Logs"
    echo "6. View Documentation"
    echo "7. Exit"
    echo "=================================="
    read -p "Select an option (1-7): " choice

    case $choice in
        1)
            ~/soc-lab/scripts/soc-dashboard.sh
            read -p "Press Enter to continue..."
            ;;
        2)
            echo "Generating test security events..."
            ~/soc-lab/scripts/generate-events.sh
            read -p "Press Enter to continue..."
            ;;
        3)
            echo "SYSTEM STATUS CHECK:"
            echo "===================="
            systemctl status elasticsearch --no-pager -l
            systemctl status kibana --no-pager -l
            systemctl status logstash --no-pager -l
            read -p "Press Enter to continue..."
            ;;
        4)
            echo "RECENT ALERTS:"
            echo "=============="
            tail -20 /var/log/elastalert/elastalert.log | \
              grep -E "(Alert|Match found)" || echo "No recent alerts"
            read -p "Press Enter to continue..."
            ;;
        5)
            read -p "Enter search term: " search_term
            echo "Searching logs for: $search_term"
            grep -i "$search_term" /var/log/syslog /var/log/auth.log | tail -10
            read -p "Press Enter to continue..."
            ;;
        6)
            echo "AVAILABLE DOCUMENTATION:"
            echo "========================"
            echo "1. SOC Mission Statement"
            echo "2. Incident Response Procedures"
            read -p "Select document (1-2): " doc_choice
            case $doc_choice in
                1) cat ~/soc-lab/documentation/soc-mission.txt ;;
                2) cat ~/soc-lab/documentation/incident-response.txt ;;
                *) echo "Invalid selection" ;;
            esac
            read -p "Press Enter to continue..."
            ;;
        7)
            echo "Exiting SOC Operations..."
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            sleep 2
            ;;
    esac
done
EOF

chmod +x ~/soc-lab/scripts/soc-operations.sh
```

> **🗂️ SOC Operations Menu Options:**

| Option | Action |
|---|---|
| 1️⃣ | View real-time monitoring dashboard |
| 2️⃣ | Generate test security events |
| 3️⃣ | Check ELK stack service status |
| 4️⃣ | View recent ElastAlert triggers |
| 5️⃣ | Search syslog and auth.log by keyword |
| 6️⃣ | View SOC mission or IR procedures |
| 7️⃣ | Exit operations menu |

---

# 🔍 Verification and Testing

## ✅ Final System Check

🔎 **Check all services are running:**

```bash
echo "SERVICE STATUS CHECK:"
echo "====================="
sudo systemctl status elasticsearch --no-pager | grep Active
sudo systemctl status kibana --no-pager | grep Active
sudo systemctl status logstash --no-pager | grep Active
```

⚡ **Check ElastAlert status:**

```bash
echo "ELASTALERT STATUS:"
echo "=================="
if pgrep -f elastalert > /dev/null; then
    echo "ElastAlert is RUNNING"
else
    echo "ElastAlert is STOPPED - Starting it now..."
    nohup elastalert --config /etc/elastalert/config.yaml --verbose \
      > /var/log/elastalert/elastalert.log 2>&1 &
    sleep 5
    echo "ElastAlert started"
fi
```

🌐 **Test Elasticsearch connectivity:**

```bash
curl -s "localhost:9200/_cluster/health?pretty" | grep status
```

📊 **Check for indexed data:**

```bash
curl -s "localhost:9200/_cat/indices?v" | grep soc-logs
```

▶️ **Generate final test events and run dashboard:**

```bash
~/soc-lab/scripts/generate-events.sh
sleep 10
~/soc-lab/scripts/soc-dashboard.sh
```

---

## 🌐 Access Kibana Dashboard

```bash
echo "Kibana is accessible at: http://localhost:5601"
```

> 💡 If accessing from outside the lab, configure port forwarding as needed.

**📋 Kibana Setup Steps:**

| Step | Action |
|---|---|
| 1️⃣ | Go to **Management → Stack Management → Index Patterns** |
| 2️⃣ | Create index pattern: `soc-logs-*` |
| 3️⃣ | Select `@timestamp` as the time field |
| 4️⃣ | Go to **Discover** to view your logs |

---

# 🔧 Troubleshooting Common Issues

<details>
<summary>🔴 Elasticsearch Won't Start</summary>

Check Java installation:

```bash
java -version
```

Check Elasticsearch logs:

```bash
sudo journalctl -u elasticsearch -f
```

Restart Elasticsearch:

```bash
sudo systemctl restart elasticsearch
```

</details>

<details>
<summary>🔴 No Data in Elasticsearch</summary>

Check Logstash status and logs:

```bash
sudo systemctl status logstash
sudo journalctl -u logstash -f
```

Restart Logstash:

```bash
sudo systemctl restart logstash
```

</details>

<details>
<summary>🔴 ElastAlert Not Working</summary>

Test the alert rule configuration:

```bash
elastalert-test-rule --config /etc/elastalert/config.yaml \
  /etc/elastalert/rules/failed-ssh-rule.yaml
```

Monitor ElastAlert logs in real-time:

```bash
tail -f /var/log/elastalert/elastalert.log
```

</details>

---

# 📝 Lab Verification Checklist

Before completing the lab, verify the following:

- [ ] ✅ Elasticsearch is running and accessible at `localhost:9200`
- [ ] ✅ Kibana dashboard is accessible at `http://localhost:5601`
- [ ] ✅ Logstash is collecting and parsing system logs
- [ ] ✅ SOC index pattern `soc-logs-*` is created in Kibana
- [ ] ✅ Sample security events are being generated and indexed
- [ ] ✅ ElastAlert is running and evaluating rules
- [ ] ✅ Failed SSH login rule is configured and tested
- [ ] ✅ Blocked connections rule is configured and tested
- [ ] ✅ SOC dashboard script runs and displays correct service status
- [ ] ✅ Incident response documentation is created

---

# ✅ Expected Outcomes

After completing this lab, students should have:

- ✅ **SOC mission and maturity documentation** created and understood
- ✅ **Full ELK stack** deployed (Elasticsearch + Logstash + Kibana)
- ✅ **Log collection pipeline** ingesting `auth.log` and `syslog`
- ✅ **Two ElastAlert rules** detecting brute force and network scans
- ✅ **SOC dashboard script** showing real-time service and alert status
- ✅ **SOC operations menu** with 7 interactive operational functions
- ✅ **Incident response procedures** document with 6-phase IR framework

---

# 🎓 Conclusion

In this comprehensive lab, you successfully implemented the **foundational components of a modern SOC**. Here's a summary of key accomplishments:

| Area | Achievement |
|---|---|
| 🏛️ SOC Theory | Defined mission, KPIs, and 5-level maturity model |
| 🔍 Elasticsearch | Single-node cluster indexing SOC log data |
| 📊 Kibana | Visualization dashboard connected to Elasticsearch |
| 🔄 Logstash | Parsing pipeline for syslog and auth log formats |
| 🚨 ElastAlert | Frequency-based rules for SSH brute force and network scans |
| 📋 Documentation | SOC mission statement and 6-phase IR procedures |
| 🖥️ Automation | Dashboard and operations menu scripts for SOC workflows |

---

## 💡 Key Takeaways

| # | Takeaway |
|---|---|
| 🏛️ | **SOC maturity** is a journey — organizations progress through 5 levels |
| 📊 | **SIEM tools** correlate logs from multiple sources for unified visibility |
| 🚨 | **Alerting rules** must be tuned carefully to reduce false positives |
| 📋 | **Documented IR procedures** are essential for effective incident handling |
| 🔍 | **Log correlation** reveals attack patterns invisible in single sources |
| ⚡ | **Automation** is key to SOC efficiency at scale |

---

## 🚀 Next Steps

![ThreatIntel](https://img.shields.io/badge/Next-Threat%20Intelligence-red?style=flat-square)
![Kibana](https://img.shields.io/badge/Next-Kibana%20Dashboards-E8478B?style=flat-square&logo=kibana&logoColor=white)
![IR](https://img.shields.io/badge/Next-Incident%20Response%20Drills-orange?style=flat-square)
![Advanced](https://img.shields.io/badge/Next-Advanced%20Log%20Parsing-blue?style=flat-square)

- 🔴 Integrate **threat intelligence feeds** to enhance IOC-based detection
- 🟣 Explore **Kibana visualizations** to build custom security dashboards
- 🟠 Practice **incident response drills** using the documented procedures
- 🔵 Experiment with **additional log sources** and Grok parsing rules

---

<div align="center">

![Made with](https://img.shields.io/badge/Made%20with-❤️%20for%20Security-blueviolet?style=for-the-badge)
![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Lab%20Guide-0077B5?style=for-the-badge)

</div>
