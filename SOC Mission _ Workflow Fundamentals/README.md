# 🛡️ SOC Mission & Workflow Fundamentals

<div align="center">

![SOC](https://img.shields.io/badge/SOC-Security%20Operations%20Center-blue?style=for-the-badge&logo=securityscorecard&logoColor=white)
![ELK](https://img.shields.io/badge/ELK-Stack-005571?style=for-the-badge&logo=elastic&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.x-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Logstash](https://img.shields.io/badge/Logstash-Data%20Pipeline-005571?style=for-the-badge&logo=logstash&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Visualization-F04E98?style=for-the-badge&logo=kibana&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

</div>

---

# 📖 Overview

This lab introduces the **mission, workflows, and operational procedures of a Security Operations Center (SOC)**. Students will gain hands-on experience deploying an open-source SIEM solution using the **ELK Stack (Elasticsearch, Logstash, Kibana)**, implementing security monitoring, configuring alerting systems, and creating SOC operational procedures.

---

# 🎯 Objectives

By the end of this lab, students will be able to:

✅ Define the mission and purpose of a Security Operations Center (SOC)

✅ Understand SOC maturity levels and their characteristics

✅ Set up and configure a basic SIEM tool using open-source software

✅ Create and configure alerting systems for security monitoring

✅ Implement basic log collection and analysis workflows

✅ Demonstrate understanding of SOC operational procedures

---

# 📋 Prerequisites

Before starting this lab, students should have:

- Basic Linux command line operations
- Understanding of networking concepts
- Familiarity with cybersecurity terminology
- Experience with text editors (nano/vim)
- Basic system administration knowledge

---

# 🖥️ Lab Environment

Al Nafi provides a ready-to-use Ubuntu cloud machine.

### Environment Includes

| Component | Version |
|------------|----------|
| Ubuntu | 20.04 LTS |
| Elasticsearch | 7.x |
| Kibana | 7.x |
| Logstash | 7.x |
| Java | OpenJDK 11 |
| ElastAlert | Latest |

---

# 🏢 Task 1: Define SOC Mission and Maturity Levels

---

## 📌 Subtask 1.1: Understanding SOC Mission

A Security Operations Center (SOC) is a centralized facility responsible for:

- Prevention
- Detection
- Response
- Recovery
- Continuous Improvement

### Core SOC Mission

```text
Monitor → Detect → Analyze → Respond → Improve
```

---

## 📌 Subtask 1.2: SOC Maturity Levels

### 🔹 Level 1 — Initial / Ad Hoc

- Reactive security
- Manual responses
- Minimal documentation

### 🔹 Level 2 — Developing

- Basic SIEM
- Defined response team
- Security awareness training

### 🔹 Level 3 — Defined

- Standardized procedures
- Integrated tools
- Threat hunting

### 🔹 Level 4 — Managed

- Advanced automation
- Metrics-driven decisions
- Threat intelligence

### 🔹 Level 5 — Optimizing

- Predictive security
- Full automation
- Continuous optimization

---

## 📌 Subtask 1.3: Create SOC Documentation

### Create Documentation Directory

```bash
mkdir -p ~/soc-lab/documentation
```

### Create Mission Statement

```bash
cat > ~/soc-lab/documentation/soc-mission.txt << 'EOF'
SOC MISSION STATEMENT
====================

Mission: To provide continuous monitoring, detection, and response to cybersecurity
threats while maintaining confidentiality, integrity, and availability.

Core Objectives:
1. Monitor network traffic and logs
2. Detect security incidents
3. Respond rapidly to threats
4. Document security events
5. Improve security posture

KPIs:
- MTTD
- MTTR
- Incident Count
- False Positive Rate
- System Availability

SOC Maturity Level: Level 2
Target Maturity Level: Level 3
EOF
```

Display file:

```bash
cat ~/soc-lab/documentation/soc-mission.txt
```

---

# ⚙️ Task 2: Deploy ELK Stack SIEM

---

## 🔧 Step 1: Install Java

```bash
sudo apt update
sudo apt install -y openjdk-11-jdk

java -version
```

---

## 🔧 Step 2: Install Elasticsearch

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -

echo "deb https://artifacts.elastic.co/packages/7.x/apt stable main" | sudo tee /etc/apt/sources.list.d/elastic-7.x.list

sudo apt update

sudo apt install -y elasticsearch
```

### Configure Elasticsearch

```bash
sudo sed -i 's/#network.host: 192.168.0.1/network.host: localhost/' /etc/elasticsearch/elasticsearch.yml

sudo sed -i 's/#http.port: 9200/http.port: 9200/' /etc/elasticsearch/elasticsearch.yml
```

### Start Service

```bash
sudo systemctl start elasticsearch
sudo systemctl enable elasticsearch

sleep 30

curl -X GET "localhost:9200/"
```

---

## 🔧 Step 3: Install Kibana

```bash
sudo apt install -y kibana
```

### Configure Kibana

```bash
sudo sed -i 's/#server.host: "localhost"/server.host: "0.0.0.0"/' /etc/kibana/kibana.yml

sudo sed -i 's/#elasticsearch.hosts:/elasticsearch.hosts:/' /etc/kibana/kibana.yml
```

### Start Kibana

```bash
sudo systemctl start kibana
sudo systemctl enable kibana

sleep 60
```

---

## 🔧 Step 4: Install Logstash

```bash
sudo apt install -y logstash
```

Create configuration directory:

```bash
sudo mkdir -p /etc/logstash/conf.d
```

### Create Logstash Pipeline

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
      match => {
        "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:message}"
      }
    }
  }

  if [type] == "auth" {
    grok {
      match => {
        "message" => "%{SYSLOGTIMESTAMP:timestamp} %{IPORHOST:host} %{DATA:program}(?:\[%{POSINT:pid}\])?: %{GREEDYDATA:auth_message}"
      }
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
```

Move configuration:

```bash
sudo mv /tmp/logstash-syslog.conf /etc/logstash/conf.d/
```

Start service:

```bash
sudo systemctl start logstash
sudo systemctl enable logstash
```

---

# 📊 Task 3: Configure Log Collection

---

## Generate Security Events

```bash
mkdir -p ~/soc-lab/scripts
```

Create script:

```bash
nano ~/soc-lab/scripts/generate-events.sh
```

Make executable:

```bash
chmod +x ~/soc-lab/scripts/generate-events.sh
```

Run script:

```bash
~/soc-lab/scripts/generate-events.sh
```

---

## Verify Data Collection

```bash
sleep 60

curl -X GET "localhost:9200/_cat/indices?v"
```

Search logs:

```bash
curl -X GET "localhost:9200/soc-logs-*/_search?pretty"
```

---

# 🚨 Task 4: Configure Alerting System

---

## Install ElastAlert

```bash
sudo apt install -y python3-pip

sudo pip3 install elastalert
```

Create directories:

```bash
sudo mkdir -p /etc/elastalert/rules
sudo mkdir -p /var/log/elastalert
```

---

## Create ElastAlert Configuration

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
```

Move file:

```bash
sudo mv /tmp/elastalert-config.yaml /etc/elastalert/config.yaml
```

---

## Create Failed SSH Rule

```bash
sudo nano /etc/elastalert/rules/failed-ssh-rule.yaml
```

Create brute-force detection rule.

---

## Initialize ElastAlert

```bash
elastalert-create-index \
--config /etc/elastalert/config.yaml
```

Test rule:

```bash
elastalert-test-rule \
--config /etc/elastalert/config.yaml \
/etc/elastalert/rules/failed-ssh-rule.yaml
```

Start service:

```bash
nohup elastalert \
--config /etc/elastalert/config.yaml \
--verbose \
> /var/log/elastalert/elastalert.log 2>&1 &
```

---

# 📈 Task 5: SOC Dashboard

---

## Create Dashboard Script

```bash
nano ~/soc-lab/scripts/soc-dashboard.sh
```

Make executable:

```bash
chmod +x ~/soc-lab/scripts/soc-dashboard.sh
```

Run dashboard:

```bash
~/soc-lab/scripts/soc-dashboard.sh
```

Dashboard displays:

- Elasticsearch Status
- Kibana Status
- Logstash Status
- Recent Security Events
- Alert Status
- Elasticsearch Indices

---

# 📑 Task 6: Incident Response Procedures

Create file:

```bash
nano ~/soc-lab/documentation/incident-response.txt
```

### Incident Lifecycle

| Phase | Description |
|---------|-------------|
| Preparation | Readiness activities |
| Identification | Detect incidents |
| Containment | Stop spread |
| Eradication | Remove threat |
| Recovery | Restore services |
| Lessons Learned | Improve processes |

---

# 🧪 Task 7: Test SOC Detection

Generate failed logins:

```bash
for i in {1..5}; do
logger -p auth.warning \
"sshd[$(($RANDOM + 1000))]: Failed password for invalid user hacker$i from 192.168.1.$(($RANDOM % 255)) port 22 ssh2"
sleep 2
done
```

Generate blocked connections:

```bash
for i in {1..7}; do
logger -p daemon.warning \
"kernel: [UFW BLOCK] IN=eth0 OUT= MAC= SRC=10.0.0.$(($RANDOM % 255)) DST=192.168.1.1 PROTO=TCP SPT=$(($RANDOM + 10000)) DPT=22"
sleep 1
done
```

Wait for processing:

```bash
sleep 30
```

---

# 🛠️ Task 8: SOC Operations Menu

Run operations interface:

```bash
~/soc-lab/scripts/soc-operations.sh
```

Menu Features:

```text
1. View Dashboard
2. Generate Test Events
3. Check System Status
4. View Alerts
5. Search Logs
6. View Documentation
7. Exit
```

---

# ✅ Verification & Testing

Check services:

```bash
sudo systemctl status elasticsearch
sudo systemctl status kibana
sudo systemctl status logstash
```

Check ElastAlert:

```bash
pgrep -f elastalert
```

Verify cluster health:

```bash
curl -s "localhost:9200/_cluster/health?pretty"
```

Check indices:

```bash
curl -s "localhost:9200/_cat/indices?v"
```

Launch dashboard:

```bash
~/soc-lab/scripts/soc-dashboard.sh
```

---

# 🌐 Access Kibana

```bash
http://localhost:5601
```

### Configure Index Pattern

```text
Management
 └── Stack Management
      └── Index Patterns
            └── soc-logs-*
```

Select:

```text
@timestamp
```

as the Time Field.

---

# 🚑 Troubleshooting

---

## Elasticsearch Won't Start

```bash
java -version

sudo journalctl -u elasticsearch -f

sudo systemctl restart elasticsearch
```

---

## No Data in Elasticsearch

```bash
sudo systemctl status logstash

sudo journalctl -u logstash -f

sudo systemctl restart logstash
```

---

## ElastAlert Not Working

```bash
elastalert-test-rule \
--config /etc/elastalert/config.yaml \
/etc/elastalert/rules/failed-ssh-rule.yaml
```

Check logs:

```bash
tail -f /var/log/elastalert/elastalert.log
```

---

# 📚 Key Concepts Summary

### SOC

Centralized team responsible for:

- Monitoring
- Detection
- Analysis
- Response

### SIEM

Security Information and Event Management platform that:

- Collects logs
- Correlates events
- Generates alerts
- Provides visibility

### ELK Stack

- Elasticsearch → Data Storage
- Logstash → Data Processing
- Kibana → Visualization

### Alerting

Automated notifications triggered by suspicious activity.

### Incident Response

Structured methodology for handling security events.

---

# 🎓 Expected Outcomes

After completing this lab you will have:

✅ Functional ELK Stack SIEM

✅ Automated log collection

✅ Security event monitoring

✅ Real-time alerting with ElastAlert

✅ SOC dashboard and reporting

✅ Incident response procedures

✅ Understanding of SOC maturity levels

---

# 🏁 Conclusion

In this lab, you successfully built a foundational Security Operations Center (SOC) environment using industry-standard open-source technologies. You explored SOC missions and maturity levels, deployed the ELK Stack for centralized logging, implemented alerting with ElastAlert, created monitoring dashboards, and established incident response procedures.

These practical skills mirror real-world SOC operations and provide a strong foundation for careers in:

- Security Operations (SOC Analyst)
- Threat Detection
- Incident Response
- Cyber Defense
- SIEM Engineering
- Security Monitoring

By mastering ELK Stack, ElastAlert, and SOC workflows, you gain hands-on experience with technologies and processes widely used across enterprise security environments.

---

<div align="center">

### 🛡️ Security Operations Center Complete

**Monitor • Detect • Analyze • Respond • Improve**

⭐ Happy Hunting & Stay Secure ⭐

</div>
