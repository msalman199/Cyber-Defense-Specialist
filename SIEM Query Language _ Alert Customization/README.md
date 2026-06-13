# 🛡️ SIEM Query Language & Alert Customization 

<div align="center">

![SIEM](https://img.shields.io/badge/SIEM-Wazuh-1E88E5?style=for-the-badge&logo=elasticstack&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-FFB300?style=for-the-badge&logo=linux&logoColor=black)
![Security](https://img.shields.io/badge/Security-Alerting-D32F2F?style=for-the-badge)
![Elasticsearch](https://img.shields.io/badge/Elasticsearch-Queries-005571?style=for-the-badge&logo=elasticsearch&logoColor=white)

</div>

---

# 🎯 Objectives

By the end of this lab, students will be able to:

- 🧠 Understand SIEM query language fundamentals  
- 🔍 Write custom Wazuh queries for threat detection  
- 🚨 Create and configure custom alert rules  
- ⚙️ Automate alert generation for threat scenarios  
- 🎚️ Customize severity levels and response actions  
- ⚡ Optimize queries for performance  
- 🧪 Validate SIEM queries in a controlled environment  

---

# 📚 Prerequisites

Students should have:

- 🐧 Linux command line basics  
- 📄 Log analysis understanding  
- 📦 JSON structure familiarity  
- 🔐 Basic cybersecurity knowledge  
- 🧩 Optional: regex understanding  

---

# ☁️ Lab Environment

### 🚀 Al Nafi Cloud Machine

This lab runs on a pre-configured **Ubuntu 20.04 LTS** environment with:

- 🧠 Wazuh Manager installed  
- 📊 Elasticsearch / Indexer  
- 📡 Dashboard UI  
- 🧪 Sample security logs  

---

# 🧩 Task 1: Wazuh Query Language Basics

## ⚙️ Step 1.1: Start Services

```bash
sudo systemctl start wazuh-manager
sudo systemctl start wazuh-indexer
sudo systemctl start wazuh-dashboard
sudo systemctl status wazuh-manager
```

### 🌐 Open Dashboard
Open your web browser and navigate to the dashboard address:
```text
firefox http://localhost:5601 &
```
🔑 **Default login:** `admin` / `admin`

### 📄 Basic Query Structure
```json
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "rule.level": "10"
          }
        }
      ]
    }
  }
}
```

## 🔐 Step 1.2: Failed Login Query

This DSL query targets index data identifying event logs with authorization errors occurring within the past hour.

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "rule.groups": "authentication_failed"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h"
            }
          }
        }
      ]
    }
  }
}
```

### 💾 Save Query
```bash
cat > /tmp/failed_login_query.json << 'EOF'
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "rule.groups": "authentication_failed"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-1h"
            }
          }
        }
      ]
    }
  }
}
EOF
```

### 🚀 Execute Query
Submit the payload payload request against the REST endpoints:
```bash
curl -X POST "localhost:9200/wazuh-alerts-*/_search" \
-H "Content-Type: application/json" \
-u admin:admin \
-d @/tmp/failed_login_query.json
```

---

# 🧩 Task 2: Advanced SIEM Queries

## 🚨 Brute Force Detection
This structure groups authentication failures from the last 10 minutes, generating an aggregation bucket to expose the top 10 offending source IP addresses.

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "rule.groups": "authentication_failed"
          }
        },
        {
          "range": {
            "@timestamp": {
              "gte": "now-10m"
            }
          }
        }
      ]
    }
  },
  "aggs": {
    "source_ips": {
      "terms": {
        "field": "data.srcip.keyword",
        "size": 10
      }
    }
  }
}
```

## 📁 File Access Monitoring
Query designed to alert on File Integrity Monitoring (`syscheck`) activities that specifically target critical system files like `passwd`.

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "match": {
            "rule.groups": "syscheck"
          }
        },
        {
          "wildcard": {
            "syscheck.path.keyword": "*passwd*"
          }
        }
      ]
    }
  }
}
```

## 🌐 Network Anomaly Query
Isolates firewall blocks with a severity score of Level 7 or higher and breaks down the top 5 most frequently blocked target IPs.

```json
{
  "query": {
    "bool": {
      "must": [
        {
          "range": {
            "rule.level": {
              "gte": 7
            }
          }
        },
        {
          "match": {
            "rule.groups": "firewall"
          }
        }
      ]
    }
  },
  "aggs": {
    "top_blocked_ips": {
      "terms": {
        "field": "data.srcip.keyword",
        "size": 5
      }
    }
  }
}
```

---

# 🧩 Task 3: Custom Alert Rules

## ⚙️ Step 3.1: Create Rule Directory
```bash
sudo mkdir -p /var/ossec/etc/rules/custom
sudo chown ossec:ossec /var/ossec/etc/rules/custom
```

## 🚨 Authentication Rules
Append custom rules to detect threshold failures originating from identical source addresses.

📄 `/var/ossec/etc/rules/custom/custom_auth_rules.xml`

```xml
<group name="custom,authentication,">

  <rule id="100001" level="10">
    <if_matched_sid>5503</if_matched_sid>
    <same_source_ip />
    <description>Multiple authentication failures detected</description>
  </rule>

  <rule id="100002" level="8">
    <if_matched_sid>5501</if_matched_sid>
    <same_source_ip />
    <description>Successful login after failures</description>
  </rule>

</group>
```

## 📁 File Integrity Rules
Tracks unauthorized modifications made directly to foundational system identity targets.

📄 `/var/ossec/etc/rules/custom/custom_syscheck_rules.xml`

```xml
<group name="custom,syscheck,">

  <rule id="101001" level="12">
    <if_matched_sid>550</if_matched_sid>
    <field name="file">/etc/passwd|/etc/shadow</field>
    <description>Critical system file modified</description>
  </rule>

</group>
```

## 🌐 Network Rules
Triggers alerts when incoming port discovery scans hit firewall thresholds.

📄 `/var/ossec/etc/rules/custom/custom_firewall_rules.xml`

```xml
<group name="custom,firewall,">

  <rule id="102001" level="8">
    <if_matched_sid>4001</if_matched_sid>
    <same_source_ip />
    <description>Port scan detected</description>
  </rule>

</group>
```

## 🔄 Restart Wazuh
Apply the updated configurations by restarting the manager instance:
```bash
sudo systemctl restart wazuh-manager
sudo systemctl status wazuh-manager
```

---

# 🧩 Task 4: Alert Automation

## 🚨 Generate Test Events
Create a verification script to generate simulated attack patterns in the local log stream.

```bash
cat > /tmp/generate_test_events.sh << 'EOF'
#!/bin/bash

for i in {1..5}; do
  logger "Failed password for user from 192.168.1.100"
done

echo "Test events generated"
EOF

chmod +x /tmp/generate_test_events.sh
/tmp/generate_test_events.sh
```

## 📡 Monitor Alerts
Follow real-time engine processing outcomes via standard tracking outputs:
```bash
tail -f /var/ossec/logs/alerts/alerts.log
```

## 🚫 Alert Response Script
Create an automated defense skeleton that runs basic block actions whenever a specific rule ID is matched.

```bash
cat > /tmp/alert_response.sh << 'EOF'
#!/bin/bash

RULE_ID=$1
IP=$2

if [[ $RULE_ID == "100001" ]]; then
  echo "🚫 Blocking IP: $IP"
fi
EOF

chmod +x /tmp/alert_response.sh
```

---

# ⚡ Task 5: Query Optimization

## 🚀 Performance Test
Measure execution performance against the search engine clusters using a validation harness.

```bash
cat > /tmp/query_perf.sh << 'EOF'
#!/bin/bash

START=$(date +%s)
curl -s localhost:9200/wazuh-alerts-*/_search > /dev/null
END=$(date +%s)

echo "Time: $((END-START)) seconds"
EOF

chmod +x /tmp/query_perf.sh
/tmp/query_perf.sh
```

## ⚡ Optimized Query Concept
To keep SIEM dashboards responsive and ensure fast query execution, follow these best practices:
- **Use filter context instead of query context**: Filters skip relevance scoring and are automatically cached by the search cluster.
- **Limit time range boundaries**: Always include explicit time windows (e.g., `now-15m`) to restrict the volume of index shards searched.
- **Query structured `.keyword` fields**: Perform exact matches against raw keyword fields rather than searching full-text analyzed strings.
- **Reduce aggregation size parameters**: Avoid pulling massive datasets into tracking buckets by keeping sizes minimal (e.g., `size: 5`).

---

# 🧪 Task 6: Validation

## 🧾 System Check
Ensure all management and indexing services are running smoothly:
```bash
systemctl status wazuh-manager
systemctl status wazuh-indexer
```

## 🧪 Final Test
Simulate multi-vector threat indicators to verify that your custom alert rules match incoming log lines correctly:
```bash
echo "Simulating attack events..."
logger "FAILED LOGIN FROM 10.0.0.5"
logger "SQL injection attempt detected"
```

---

# 📊 Expected Outcome

Upon completing this lab, your environment will feature:
