# 🛡️ SIEM Tool Configuration 

<div align="center">

![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-0264D6?style=for-the-badge&logo=wazuh&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-20.04_LTS-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.17-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Visualization-005571?style=for-the-badge&logo=kibana&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Security-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![SOC](https://img.shields.io/badge/SOC-Operations-red?style=for-the-badge)

# 🔍 SIEM Tool Configuration

### Security Information and Event Management with Wazuh

</div>

---

# 🎯Objectives

By the end of this lab, students will be able to:

✅ Understand the fundamentals of Security Information and Event Management (SIEM) systems

✅ Install and configure Wazuh SIEM agent on a Linux machine

✅ Set up Wazuh to collect system logs and security events

✅ Configure basic log analysis and monitoring rules

✅ Generate and analyze security alerts using Wazuh Dashboard

✅ Implement basic threat detection capabilities on a single Linux system

---

# 📚 Prerequisites

Before starting this lab, students should have:

- Basic Linux command line knowledge
- Familiarity with Linux log files
- Basic cybersecurity concepts
- Understanding of TCP/IP networking fundamentals

> 💡 No prior SIEM experience is required.

---

# ☁️ Lab Environment

### Al Nafi Cloud Environment

This lab uses a pre-configured Ubuntu 20.04 LTS machine.

### Environment Includes

| Resource | Specification |
|-----------|-------------|
| Operating System | Ubuntu 20.04 LTS |
| RAM | 4 GB Minimum |
| Disk Space | 20 GB Available |
| Internet Access | Enabled |
| Permissions | Sudo Access |

---

# 📌 Task 1: Install Wazuh Manager and Agent

---

## 🔹 Subtask 1.1: System Preparation

### Update System Packages

```bash
sudo apt update && sudo apt upgrade -y
```

### Install Dependencies

```bash
sudo apt install curl apt-transport-https lsb-release gnupg2 software-properties-common -y
```

### Verify System Information

```bash
uname -a
cat /etc/os-release
```

---

## 🔹 Subtask 1.2: Configure Wazuh Repository

### Add Wazuh GPG Key

```bash
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | \
gpg --no-default-keyring \
--keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg \
--import

chmod 644 /usr/share/keyrings/wazuh.gpg
```

### Add Repository

```bash
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] https://packages.wazuh.com/4.x/apt/ stable main" | \
sudo tee -a /etc/apt/sources.list.d/wazuh.list
```

### Update Package Information

```bash
sudo apt update
```

---

## 🔹 Subtask 1.3: Install Wazuh Manager

### Install Manager

```bash
sudo apt install wazuh-manager -y
```

### Enable and Start Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager
```

### Verify Status

```bash
sudo systemctl status wazuh-manager
```

---

## 🔹 Subtask 1.4: Install Wazuh Agent

### Install Agent

```bash
sudo apt install wazuh-agent -y
```

### Configure Agent

```bash
sudo sed -i 's/<server>.*<\/server>/<server>127.0.0.1<\/server>/' \
/var/ossec/etc/ossec.conf
```

### Configure Agent Variables

```bash
echo "WAZUH_MANAGER='127.0.0.1'" | sudo tee /var/ossec/etc/preloaded-vars.conf

echo "WAZUH_AGENT_NAME='local-agent'" | \
sudo tee -a /var/ossec/etc/preloaded-vars.conf

echo "WAZUH_AGENT_GROUP='default'" | \
sudo tee -a /var/ossec/etc/preloaded-vars.conf
```

### Start Agent

```bash
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

### Verify Agent

```bash
sudo systemctl status wazuh-agent
```

---

# 📌 Task 2: Configure Log Collection and Analysis

---

## 🔹 Subtask 2.1: Install Elasticsearch

### Install Java

```bash
sudo apt install openjdk-11-jdk -y
```

### Add Elasticsearch Repository

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg
```

```bash
echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] https://artifacts.elastic.co/packages/7.x/apt stable main" | \
sudo tee /etc/apt/sources.list.d/elastic-7.x.list
```

### Install Elasticsearch

```bash
sudo apt update
sudo apt install elasticsearch=7.17.13 -y
```

### Configure Elasticsearch

```bash
sudo tee /etc/elasticsearch/elasticsearch.yml > /dev/null <<EOF
network.host: 127.0.0.1
http.port: 9200
cluster.initial_master_nodes: ["node-1"]
node.name: node-1
cluster.name: wazuh-cluster
discovery.type: single-node
EOF
```

### Enable and Start

```bash
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch
```

---

## 🔹 Subtask 2.2: Install Kibana

### Install Kibana

```bash
sudo apt install kibana=7.17.13 -y
```

### Configure Kibana

```bash
sudo tee /etc/kibana/kibana.yml > /dev/null <<EOF
server.host: "127.0.0.1"
server.port: 5601
elasticsearch.hosts: ["http://127.0.0.1:9200"]
EOF
```

### Enable and Start Kibana

```bash
sudo systemctl daemon-reload
sudo systemctl enable kibana
sudo systemctl start kibana
```

---

## 🔹 Subtask 2.3: Install Wazuh Kibana Plugin

```bash
sudo -u kibana /usr/share/kibana/bin/kibana-plugin install \
https://packages.wazuh.com/4.x/ui/kibana/wazuh_kibana-4.5.4_7.17.13-1.zip
```

### Restart Kibana

```bash
sudo systemctl restart kibana
```

---

## 🔹 Subtask 2.4: Configure Log Collection

Edit Wazuh configuration:

```bash
sudo nano /var/ossec/etc/ossec.conf
```

Add:

```xml
<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/auth.log</location>
</localfile>

<localfile>
  <log_format>syslog</log_format>
  <location>/var/log/syslog</location>
</localfile>

<localfile>
  <log_format>apache</log_format>
  <location>/var/log/apache2/access.log</location>
</localfile>

<localfile>
  <log_format>apache</log_format>
  <location>/var/log/apache2/error.log</location>
</localfile>
```

---

### File Integrity Monitoring

```xml
<syscheck>
  <directories check_all="yes">/etc,/usr/bin,/usr/sbin</directories>
  <directories check_all="yes">/bin,/sbin</directories>
  <directories check_all="yes" realtime="yes">/home</directories>
</syscheck>
```

---

### Rootcheck Configuration

```xml
<rootcheck>
  <rootkit_files>/var/ossec/etc/rootcheck/rootkit_files.txt</rootkit_files>
  <rootkit_trojans>/var/ossec/etc/rootcheck/rootkit_trojans.txt</rootkit_trojans>
</rootcheck>
```

### Restart Services

```bash
sudo systemctl restart wazuh-manager
sudo systemctl restart wazuh-agent
```

---

## 🔹 Subtask 2.5: Verify Connectivity

### Check Services

```bash
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-agent
sudo systemctl status elasticsearch
sudo systemctl status kibana
```

### Test Elasticsearch

```bash
curl -X GET "127.0.0.1:9200/_cluster/health?pretty"
```

### Wait for Kibana

```bash
sleep 180
curl -I http://127.0.0.1:5601
```

### Check Agent Registration

```bash
sudo /var/ossec/bin/agent_control -l
```

---

# 📌 Task 3: Generate and Analyze Security Events

---

## 🔹 Subtask 3.1: Generate Security Events

### Failed Login Events

```bash
for i in {1..5}; do
  echo "wrong_password" | su - nonexistent_user 2>/dev/null || true
  sleep 2
done
```

### File Integrity Events

```bash
sudo touch /etc/test_file_$(date +%s)

sudo echo "test content" > /tmp/test_modification

sudo mv /tmp/test_modification /etc/
```

### Network Activity

```bash
curl -s http://httpbin.org/ip > /dev/null

ping -c 3 8.8.8.8 > /dev/null
```

---

## 🔹 Subtask 3.2: Access Dashboard

### Open Browser

```text
http://127.0.0.1:5601
```

### Wazuh API Configuration

```text
URL: https://127.0.0.1
Port: 55000
Username: wazuh
Password: wazuh
```

---

## 🔹 Subtask 3.3: Create Custom Rules

```bash
sudo nano /var/ossec/etc/rules/local_rules.xml
```

Add:

```xml
<group name="local,">

  <rule id="100001" level="10">
    <if_matched_sid>5503</if_matched_sid>
    <same_source_ip />
    <description>
      Multiple failed login attempts from same source
    </description>
    <group>authentication_failures,</group>
  </rule>

  <rule id="100002" level="7">
    <category>ossec</category>
    <decoded_as>syscheck_new_entry</decoded_as>
    <match>/etc</match>
    <description>
      New file created in /etc directory
    </description>
    <group>syscheck,</group>
  </rule>

</group>
```

Restart Manager:

```bash
sudo systemctl restart wazuh-manager
```

---

## 🔹 Subtask 3.4: Real-Time Monitoring

Monitor alerts:

```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```

Generate additional events:

```bash
sudo touch /etc/another_test_file

echo "test" | sudo tee /etc/test_config_change
```

Agent statistics:

```bash
sudo /var/ossec/bin/agent_control -s
```

---

# 📌 Task 4: Configure Advanced Monitoring

---

## 🔹 Subtask 4.1: Active Response

Add:

```xml
<active-response>
  <disabled>no</disabled>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_id>100001</rules_id>
  <timeout>300</timeout>
</active-response>
```

Restart:

```bash
sudo systemctl restart wazuh-manager
```

---

## 🔹 Subtask 4.2: Email Notifications

```xml
<global>
  <email_notification>yes</email_notification>
  <smtp_server>localhost</smtp_server>
  <email_from>wazuh@localhost</email_from>
  <email_to>admin@localhost</email_to>
</global>

<email_alerts>
  <email_to>admin@localhost</email_to>
  <level>10</level>
  <do_not_delay />
</email_alerts>
```

---

## 🔹 Subtask 4.3: Complete SIEM Test

Create:

```bash
nano test_siem.sh
```

```bash
#!/bin/bash

echo "Running comprehensive SIEM test..."

for i in {1..3}; do
  echo "wrong_password" | su - testuser 2>/dev/null || true
  sleep 1
done

sudo touch /etc/critical_file_$(date +%s)

sudo chmod 777 /etc/passwd 2>/dev/null || true
sudo chmod 644 /etc/passwd

nmap -sS 127.0.0.1 -p 22,80,443 > /dev/null 2>&1 || true

echo "Test events generated."
```

Run:

```bash
chmod +x test_siem.sh
./test_siem.sh
```

---

# ✅ Verification Checklist

Verify:

- [ ] Wazuh Manager Running
- [ ] Wazuh Agent Connected
- [ ] Elasticsearch Operational
- [ ] Kibana Accessible
- [ ] Security Events Generated
- [ ] Custom Rules Triggering
- [ ] File Integrity Monitoring Active
- [ ] Authentication Monitoring Working
- [ ] Alerts Generated Successfully

---

# 🛠 Troubleshooting

## Issue 1: Services Not Starting

Check resources:

```bash
free -h
df -h
```

View logs:

```bash
sudo journalctl -u wazuh-manager -f
sudo journalctl -u elasticsearch -f
```

---

## Issue 2: Agent Not Connecting

Check configuration:

```bash
sudo cat /var/ossec/etc/ossec.conf
```

Restart:

```bash
sudo systemctl restart wazuh-agent
```

Verify connectivity:

```bash
sudo netstat -tlnp | grep 1514
```

---

## Issue 3: Kibana Not Accessible

```bash
sudo systemctl status kibana

sudo journalctl -u kibana -f

sudo netstat -tlnp | grep 5601
```

Check Elasticsearch:

```bash
curl -X GET "127.0.0.1:9200/_cluster/health"
```

---

# 🎉 Expected Outcomes

After completing this lab, students should have:

✅ Functional Wazuh SIEM deployment

✅ Log collection and analysis configured

✅ File Integrity Monitoring enabled

✅ Authentication monitoring operational

✅ Custom alert rules implemented

✅ Active response configuration deployed

✅ Security dashboard available through Kibana

✅ Real-time threat detection capability

---

# 📖 Conclusion

In this lab, you successfully deployed and configured a complete SIEM solution using **Wazuh**, **Elasticsearch**, and **Kibana** on Ubuntu Linux.

You learned how to:

- Install and configure Wazuh components
- Collect and analyze security logs
- Configure custom detection rules
- Implement file integrity monitoring
- Generate security alerts
- Build real-time monitoring capabilities
- Understand SIEM workflows used in enterprise SOC environments

---

# 🚀 Next Steps

- Explore Wazuh Vulnerability Detection
- Configure Compliance Monitoring
- Integrate Threat Intelligence Feeds
- Create Advanced Correlation Rules
- Build Custom Dashboards in Kibana
- Deploy Wazuh in Multi-Agent Enterprise Environments

---

<div align="center">

### 🔐 Security Monitoring • Threat Detection • Incident Response

**Hands-on SIEM Operations with Wazuh**

⭐ Happy Learning & Stay Secure ⭐

</div>
