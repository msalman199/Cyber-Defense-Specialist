
# 🛡️ SIEM Tool Configuration 

![Wazuh](https://img.shields.io/badge/Wazuh-SIEM%20Platform-005571?style=for-the-badge&logo=wazuh&logoColor=white)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Log%20Storage-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Dashboard-E8478B?style=for-the-badge&logo=kibana&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FCC624?style=for-the-badge&logo=linux&logoColor=black)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash&logoColor=white)
![Security](https://img.shields.io/badge/Threat-Detection-red?style=for-the-badge&logo=shield&logoColor=white)

---

## 🎯Objectives

By the end of this lab, students will be able to:

- 💡 Understand the fundamentals of **Security Information and Event Management (SIEM)** systems
- ⚙️ Install and configure **Wazuh SIEM agent** on a Linux machine
- 📋 Set up Wazuh to **collect system logs** and security events
- 🔧 Configure basic **log analysis and monitoring rules**
- 📊 Generate and analyze **security alerts** using Wazuh dashboard
- 🚨 Implement basic **threat detection capabilities** on a single Linux system

---

## ✅ Prerequisites

| Requirement | Description |
|---|---|
| 🖥️ Linux CLI | Basic understanding of Linux command line operations |
| 📋 System Logs | Familiarity with system logs and log file locations |
| 🛡️ Cybersecurity | Basic knowledge of cybersecurity concepts |
| 🌐 Networking | Understanding of TCP/IP basics |
| 🎓 SIEM Experience | None required — this lab starts from the beginning |

---

## 🧪 Lab Environment

> 💡 **Al Nafi** provides pre-configured Linux-based cloud machines.  
> Click **Start Lab** to access your dedicated Ubuntu 20.04 LTS machine with all necessary permissions and network access.  
> No need to build your own VM or configure additional systems.

**🛠️ System Requirements:**

| Component | Specification |
|---|---|
| 🐧 OS | Ubuntu 20.04 LTS (provided by Al Nafi) |
| 🧠 RAM | Minimum 4 GB |
| 💾 Disk | 20 GB available space |
| 🌐 Network | Internet connectivity for package downloads |

---

# 📋 Task 1 — Install Wazuh Manager and Agent on Linux Machine

![Wazuh](https://img.shields.io/badge/Wazuh-Manager%20%2B%20Agent-005571?style=flat-square&logo=wazuh&logoColor=white)
![APT](https://img.shields.io/badge/APT-Repository%20Setup-orange?style=flat-square)

---

## 🔧 Subtask 1.1 — System Preparation and Updates

🔄 **Update the system packages:**

```bash
sudo apt update && sudo apt upgrade -y
```

📦 **Install required dependencies:**

```bash
sudo apt install curl apt-transport-https lsb-release gnupg2 software-properties-common -y
```

🔍 **Check system information:**

```bash
uname -a
cat /etc/os-release
```

---

## 📦 Subtask 1.2 — Install Wazuh Repository

🔑 **Add Wazuh GPG key:**

```bash
curl -s https://packages.wazuh.com/key/GPG-KEY-WAZUH | \
  gpg --no-default-keyring \
  --keyring gnupg-ring:/usr/share/keyrings/wazuh.gpg \
  --import && chmod 644 /usr/share/keyrings/wazuh.gpg
```

📋 **Add Wazuh repository:**

```bash
echo "deb [signed-by=/usr/share/keyrings/wazuh.gpg] \
  https://packages.wazuh.com/4.x/apt/ stable main" | \
  sudo tee -a /etc/apt/sources.list.d/wazuh.list
```

🔄 **Update package information:**

```bash
sudo apt update
```

---

## ⚙️ Subtask 1.3 — Install Wazuh Manager

📥 **Install Wazuh Manager:**

```bash
sudo apt install wazuh-manager -y
```

🚀 **Enable and start Wazuh Manager service:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable wazuh-manager
sudo systemctl start wazuh-manager
```

✅ **Verify Wazuh Manager status:**

```bash
sudo systemctl status wazuh-manager
```

---

## 🤖 Subtask 1.4 — Install Wazuh Agent on Same Machine

> 💡 For this lab, we'll install the Wazuh agent on the **same machine** to monitor local system activities.

📥 **Install Wazuh Agent:**

```bash
sudo apt install wazuh-agent -y
```

🔗 **Configure the agent to connect to local manager:**

```bash
sudo sed -i 's/<server>.*<\/server>/<server>127.0.0.1<\/server>/' \
  /var/ossec/etc/ossec.conf
```

🏷️ **Set agent name and group:**

```bash
echo "WAZUH_MANAGER='127.0.0.1'" | sudo tee /var/ossec/etc/preloaded-vars.conf
echo "WAZUH_AGENT_NAME='local-agent'" | sudo tee -a /var/ossec/etc/preloaded-vars.conf
echo "WAZUH_AGENT_GROUP='default'" | sudo tee -a /var/ossec/etc/preloaded-vars.conf
```

🚀 **Enable and start Wazuh Agent:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable wazuh-agent
sudo systemctl start wazuh-agent
```

✅ **Verify agent status:**

```bash
sudo systemctl status wazuh-agent
```

---

# 📋 Task 2 — Set Up Wazuh to Collect and Analyze Logs

![Elasticsearch](https://img.shields.io/badge/Elasticsearch-7.x-005571?style=flat-square&logo=elasticsearch&logoColor=white)
![Kibana](https://img.shields.io/badge/Kibana-Dashboard-E8478B?style=flat-square&logo=kibana&logoColor=white)
![Logs](https://img.shields.io/badge/Log-Collection%20Config-blue?style=flat-square)

---

## 🗄️ Subtask 2.1 — Install Elasticsearch for Log Storage

☕ **Install Java (required for Elasticsearch):**

```bash
sudo apt install openjdk-11-jdk -y
```

📋 **Add Elasticsearch repository:**

```bash
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | \
  sudo gpg --dearmor -o /usr/share/keyrings/elasticsearch-keyring.gpg

echo "deb [signed-by=/usr/share/keyrings/elasticsearch-keyring.gpg] \
  https://artifacts.elastic.co/packages/7.x/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/elastic-7.x.list
```

📥 **Update and install Elasticsearch:**

```bash
sudo apt update
sudo apt install elasticsearch=7.17.13 -y
```

📄 **Configure Elasticsearch:**

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

🚀 **Enable and start Elasticsearch:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable elasticsearch
sudo systemctl start elasticsearch
```

---

## 📊 Subtask 2.2 — Install Kibana for Visualization

📥 **Install Kibana:**

```bash
sudo apt install kibana=7.17.13 -y
```

📄 **Configure Kibana:**

```bash
sudo tee /etc/kibana/kibana.yml > /dev/null <<EOF
server.host: "127.0.0.1"
server.port: 5601
elasticsearch.hosts: ["http://127.0.0.1:9200"]
EOF
```

🚀 **Enable and start Kibana:**

```bash
sudo systemctl daemon-reload
sudo systemctl enable kibana
sudo systemctl start kibana
```

---

## 🔌 Subtask 2.3 — Install Wazuh Kibana Plugin

📥 **Install Wazuh Kibana plugin:**

```bash
sudo -u kibana /usr/share/kibana/bin/kibana-plugin install \
  https://packages.wazuh.com/4.x/ui/kibana/wazuh_kibana-4.5.4_7.17.13-1.zip
```

🔄 **Restart Kibana to load the plugin:**

```bash
sudo systemctl restart kibana
```

---

## 📋 Subtask 2.4 — Configure Log Collection

📄 **Configure Wazuh to monitor system logs:**

```bash
sudo tee -a /var/ossec/etc/ossec.conf > /dev/null <<EOF

<!-- Additional log monitoring -->
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

<!-- File integrity monitoring -->
<syscheck>
  <directories check_all="yes">/etc,/usr/bin,/usr/sbin</directories>
  <directories check_all="yes">/bin,/sbin</directories>
  <directories check_all="yes" realtime="yes">/home</directories>
</syscheck>

<!-- Rootcheck -->
<rootcheck>
  <rootkit_files>/var/ossec/etc/rootcheck/rootkit_files.txt</rootkit_files>
  <rootkit_trojans>/var/ossec/etc/rootcheck/rootkit_trojans.txt</rootkit_trojans>
  <system_audit>/var/ossec/etc/rootcheck/system_audit_rcl.txt</system_audit>
  <system_audit>/var/ossec/etc/rootcheck/cis_debian_linux_rcl.txt</system_audit>
</rootcheck>
EOF
```

> **📁 Monitored Log Sources:**

| Log File | Format | Purpose |
|---|---|---|
| `/var/log/auth.log` | syslog | 🔐 Authentication events |
| `/var/log/syslog` | syslog | 🖥️ General system events |
| `/var/log/apache2/access.log` | apache | 🌐 Web access logs |
| `/var/log/apache2/error.log` | apache | ⚠️ Web error logs |
| `/etc`, `/usr/bin`, `/bin` | syscheck | 📁 File integrity monitoring |
| `/home` | syscheck realtime | 👤 Real-time home dir monitoring |

🔄 **Restart Wazuh Manager and Agent to apply configuration:**

```bash
sudo systemctl restart wazuh-manager
sudo systemctl restart wazuh-agent
```

---

## ✅ Subtask 2.5 — Verify Services and Connectivity

🔍 **Check all services are running:**

```bash
sudo systemctl status wazuh-manager
sudo systemctl status wazuh-agent
sudo systemctl status elasticsearch
sudo systemctl status kibana
```

🌐 **Test Elasticsearch connectivity:**

```bash
curl -X GET "127.0.0.1:9200/_cluster/health?pretty"
```

⏳ **Wait for Kibana to fully start** *(this may take 2–3 minutes)*:

```bash
echo "Waiting for Kibana to start..."
sleep 180
curl -I http://127.0.0.1:5601
```

🔗 **Check Wazuh agent connection:**

```bash
sudo /var/ossec/bin/agent_control -l
```

---

# 📋 Task 3 — Generate Test Events and Analyze Logs

![Events](https://img.shields.io/badge/Security-Event%20Generation-red?style=flat-square)
![Dashboard](https://img.shields.io/badge/Wazuh-Dashboard%20Analysis-005571?style=flat-square&logo=wazuh&logoColor=white)
![Rules](https://img.shields.io/badge/Custom-Detection%20Rules-orange?style=flat-square)

---

## 🎭 Subtask 3.1 — Generate Security Events

🔐 **Create failed login attempts:**

```bash
echo "Generating failed login events..."
for i in {1..5}; do
  echo "wrong_password" | su - nonexistent_user 2>/dev/null || true
  sleep 2
done
```

📁 **Create file integrity monitoring events:**

```bash
sudo touch /etc/test_file_$(date +%s)
sudo echo "test content" > /tmp/test_modification
sudo mv /tmp/test_modification /etc/
```

🌐 **Generate network activity:**

```bash
curl -s http://httpbin.org/ip > /dev/null
ping -c 3 8.8.8.8 > /dev/null
```

---

## 🖥️ Subtask 3.2 — Access Wazuh Dashboard

🌐 **Open your web browser and navigate to Kibana:**

```
URL: http://127.0.0.1:5601
```

> 💡 If using a remote connection, replace `127.0.0.1` with your machine's IP address.

⚙️ **Configure the Wazuh plugin:**

| Field | Value |
|---|---|
| 🔗 URL | `https://127.0.0.1` |
| 🔌 Port | `55000` |
| 👤 Username | `wazuh` |
| 🔒 Password | `wazuh` |

> Click on **"Wazuh"** in the left sidebar and add the API connection using the values above.

---

## 🔍 Subtask 3.3 — Analyze Generated Events

📊 **View security events in Wazuh dashboard:**

- Navigate to the **"Security Events"** section
- Filter events by time range: **last 1 hour**
- Look for **authentication failures** and **file integrity alerts**

✏️ **Create custom rules for analysis:**

```bash
sudo tee /var/ossec/etc/rules/local_rules.xml > /dev/null <<EOF
<group name="local,">

  <!-- Custom rule for multiple failed logins -->
  <rule id="100001" level="10">
    <if_matched_sid>5503</if_matched_sid>
    <same_source_ip />
    <description>Multiple failed login attempts from same source</description>
    <group>authentication_failures,</group>
  </rule>

  <!-- Custom rule for file modifications in /etc -->
  <rule id="100002" level="7">
    <category>ossec</category>
    <decoded_as>syscheck_new_entry</decoded_as>
    <match>/etc</match>
    <description>New file created in /etc directory</description>
    <group>syscheck,</group>
  </rule>

</group>
EOF
```

> **📋 Custom Rules Summary:**

| Rule ID | Level | Trigger | Group |
|---|---|---|---|
| `100001` | 🔴 10 | Multiple failed logins from same IP | `authentication_failures` |
| `100002` | 🟠 7 | New file created in `/etc` | `syscheck` |

🔄 **Restart Wazuh Manager to load new rules:**

```bash
sudo systemctl restart wazuh-manager
```

---

## 👁️ Subtask 3.4 — Monitor Real-time Alerts

📋 **Monitor Wazuh alerts in real-time:**

```bash
sudo tail -f /var/ossec/logs/alerts/alerts.log
```

🎭 **Generate more test events while monitoring** *(in another terminal)*:

```bash
sudo touch /etc/another_test_file
echo "test" | sudo tee /etc/test_config_change
```

📊 **Check agent statistics:**

```bash
sudo /var/ossec/bin/agent_control -s
```

---

# 📋 Task 4 — Configure Advanced Monitoring

![ActiveResponse](https://img.shields.io/badge/Active-Response-red?style=flat-square)
![Email](https://img.shields.io/badge/Email-Alerting-blue?style=flat-square)
![Testing](https://img.shields.io/badge/SIEM-Full%20Test-green?style=flat-square)

---

## 🚨 Subtask 4.1 — Set Up Active Response

📄 **Configure active response for failed logins:**

```bash
sudo tee -a /var/ossec/etc/ossec.conf > /dev/null <<EOF

<!-- Active Response Configuration -->
<active-response>
  <disabled>no</disabled>
  <command>firewall-drop</command>
  <location>local</location>
  <rules_id>100001</rules_id>
  <timeout>300</timeout>
</active-response>
EOF
```

🔄 **Restart Wazuh Manager:**

```bash
sudo systemctl restart wazuh-manager
```

---

## 📧 Subtask 4.2 — Configure Email Alerts

📄 **Configure email notifications:**

```bash
sudo tee -a /var/ossec/etc/ossec.conf > /dev/null <<EOF

<!-- Email notification configuration -->
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
EOF
```

---

## 🧪 Subtask 4.3 — Test Complete SIEM Functionality

✏️ **Create a comprehensive test script:**

```bash
#!/bin/bash
echo "Running comprehensive SIEM test..."

# Generate authentication events
for i in {1..3}; do
  echo "wrong_password" | su - testuser 2>/dev/null || true
  sleep 1
done

# Generate file integrity events
sudo touch /etc/critical_file_$(date +%s)
sudo chmod 777 /etc/passwd 2>/dev/null || true
sudo chmod 644 /etc/passwd

# Generate network events
nmap -sS 127.0.0.1 -p 22,80,443 > /dev/null 2>&1 || true

echo "Test events generated. Check Wazuh dashboard for alerts."
```

▶️ **Save and run the test script:**

```bash
chmod +x test_siem.sh
./test_siem.sh
```

✅ **Verify all components are working:**

```bash
# Check service status
sudo systemctl status wazuh-manager wazuh-agent elasticsearch kibana

# Check log processing
sudo tail -20 /var/ossec/logs/ossec.log

# Check alerts generated
sudo tail -10 /var/ossec/logs/alerts/alerts.log
```

---

# 🔧 Troubleshooting Common Issues

<details>
<summary>🔴 Services Not Starting</summary>

Check system resources:

```bash
free -h
df -h
```

Check service logs:

```bash
sudo journalctl -u wazuh-manager -f
sudo journalctl -u elasticsearch -f
```

</details>

<details>
<summary>🔴 Agent Not Connecting to Manager</summary>

Check agent configuration:

```bash
sudo cat /var/ossec/etc/ossec.conf | grep -A 5 -B 5 server
```

Restart agent and check connectivity:

```bash
sudo systemctl restart wazuh-agent
sudo netstat -tlnp | grep 1514
```

</details>

<details>
<summary>🔴 Kibana Not Accessible</summary>

Check Kibana status and logs:

```bash
sudo systemctl status kibana
sudo journalctl -u kibana -f
```

Verify port binding and Elasticsearch connectivity:

```bash
sudo netstat -tlnp | grep 5601
curl -X GET "127.0.0.1:9200/_cluster/health"
```

</details>

---

# 📝 Lab Verification Checklist

Before completing the lab, verify the following:

- [ ] ✅ Wazuh Manager is running and processing logs
- [ ] ✅ Wazuh Agent is connected and sending data
- [ ] ✅ Elasticsearch is storing log data
- [ ] ✅ Kibana dashboard is accessible at `http://127.0.0.1:5601`
- [ ] ✅ Security events are being generated and detected
- [ ] ✅ Custom rules are working correctly
- [ ] ✅ File integrity monitoring is active
- [ ] ✅ Authentication monitoring is functional
- [ ] ✅ Alerts are being generated for security events

---

# ✅ Expected Outcomes

After completing this lab, students should have:

- ✅ A fully **installed and configured Wazuh SIEM** on a single Linux machine
- ✅ **Log collection** from auth, syslog, Apache, and file integrity sources
- ✅ **Custom detection rules** for failed logins and `/etc` file changes
- ✅ **Active response** blocking repeat offenders via firewall-drop
- ✅ **Email alerting** configured for level 10+ events
- ✅ **Kibana dashboard** showing real-time security events and alerts

---

# 🎓 Conclusion

In this comprehensive lab, you successfully installed and configured a complete **SIEM solution using Wazuh** on a single Linux machine. Here's a summary of key accomplishments:

| Area | Achievement |
|---|---|
| ⚙️ Installation | Wazuh Manager + Agent + Elasticsearch + Kibana stack deployed |
| 📋 Log Collection | Auth, syslog, Apache, and real-time file integrity monitoring |
| 🔍 Event Detection | Failed logins, file changes, and rootkit checks |
| 📜 Custom Rules | Rule IDs 100001 & 100002 for tailored threat detection |
| 🚨 Active Response | Automatic firewall-drop for brute force attackers |
| 📧 Alerting | Email notifications for critical severity events |

---

## 💡 Key Takeaways

| # | Takeaway |
|---|---|
| 🛡️ | **SIEM tools** provide centralized log management and real-time threat detection |
| 📋 | **Log correlation** across multiple sources reveals attack patterns |
| 📜 | **Custom rules** tailor detection to your specific environment |
| 🚨 | **Active response** automates containment before manual intervention |
| 👁️ | **Real-time monitoring** reduces attacker dwell time significantly |
| 📊 | **Dashboard visibility** is essential for effective incident response |

---

## 🚀 Next Steps

![Vulnerability](https://img.shields.io/badge/Next-Vulnerability%20Detection-red?style=flat-square)
![Compliance](https://img.shields.io/badge/Next-Compliance%20Monitoring-blue?style=flat-square)
![ThreatIntel](https://img.shields.io/badge/Next-Threat%20Intelligence-orange?style=flat-square)
![Advanced](https://img.shields.io/badge/Next-Advanced%20Wazuh%20Features-005571?style=flat-square&logo=wazuh&logoColor=white)

- 🔴 Explore **vulnerability detection** modules in Wazuh
- 🔵 Study **compliance monitoring** (PCI-DSS, HIPAA, GDPR) with Wazuh
- 🟠 Integrate **threat intelligence feeds** for IOC-based detection
- 🟢 Learn advanced **log correlation** across distributed agents

---

<div align="center">

![Made with](https://img.shields.io/badge/Made%20with-❤️%20for%20Security-blueviolet?style=for-the-badge)
![Al Nafi](https://img.shields.io/badge/Al%20Nafi-Lab%20Guide-0077B5?style=for-the-badge)

</div>
