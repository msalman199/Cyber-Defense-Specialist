# 🛡️ SOAR Tool Integration

<div align="center">

![SOAR](https://img.shields.io/badge/SOAR-Security%20Automation-red?style=for-the-badge\&logo=securityscorecard\&logoColor=white)
![Wazuh](https://img.shields.io/badge/Wazuh-SIEM-blue?style=for-the-badge)
![TheHive](https://img.shields.io/badge/TheHive-Case%20Management-yellow?style=for-the-badge)
![Cortex](https://img.shields.io/badge/Cortex-Threat%20Analysis-purple?style=for-the-badge)
![Docker](https://img.shields.io/badge/Docker-Containers-2496ED?style=for-the-badge\&logo=docker\&logoColor=white)
![Python](https://img.shields.io/badge/Python-Automation-success?style=for-the-badge\&logo=python\&logoColor=white)

### 🚨 Security Orchestration • 🤖 Automation • ⚡ Incident Response

</div>

---

# 📖 Overview

Security Orchestration, Automation, and Response (SOAR) platforms help security teams automate repetitive tasks, streamline investigations, and accelerate incident response workflows.

In this lab, students will deploy and integrate open-source SOAR technologies including Wazuh SIEM, TheHive, and Cortex to create an automated incident response ecosystem.

This lab focuses on:

✅ Deploying Wazuh SIEM

✅ Deploying TheHive Case Management

✅ Deploying Cortex Analysis Engine

✅ Building API Connectors

✅ Creating Automated Response Playbooks

✅ Implementing Workflow Orchestration

✅ Automating Incident Case Creation

✅ Testing and Validating SOAR Workflows

---

# 🎯 Objectives

By the end of this lab, students will be able to:

* 🤖 Install and configure open-source SOAR tools
* 🛡️ Integrate Wazuh SIEM with TheHive and Cortex
* 🚨 Create automated security response playbooks
* 🔄 Build workflow orchestration engines
* 📊 Automate incident handling processes
* 📁 Create security cases automatically
* ⚡ Test automated response actions
* 🔍 Validate security automation workflows

---

# 🧰 Prerequisites

Before starting this lab, ensure you have:

* Basic Linux command-line proficiency
* Understanding of security incident response
* Familiarity with SIEM systems
* Basic Python scripting knowledge
* Understanding of JSON and YAML formats

---

# 🏗️ Lab Environment

This lab uses:

* Ubuntu 20.04 LTS
* Docker
* Docker Compose
* Python 3.x
* Wazuh SIEM
* TheHive
* Cortex
* YAML Configuration Files

---

# 📂 Project Structure

```text
soar-integration/
│
├── connectors/
│   ├── wazuh_connector.py
│   └── thehive_connector.py
│
├── playbooks/
│   ├── malware_response.py
│   └── bruteforce_response.py
│
├── workflows/
│   └── orchestrator.py
│
├── logs/
│
├── tests/
│   └── test_integration.py
│
├── config.yaml
│
└── main.py
```

---

# 🚀 Task 1: Install and Configure SOAR Components

## 🔄 Step 1: Update System and Verify Docker

```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Verify Docker installation
docker --version
docker-compose --version

# Ensure Docker service is running
sudo systemctl status docker
```

---

## 🛡️ Step 2: Deploy Wazuh SIEM

```bash
mkdir -p ~/wazuh-soar-lab

cd ~/wazuh-soar-lab

curl -so docker-compose.yml \
https://raw.githubusercontent.com/wazuh/wazuh-docker/v4.7.0/single-node/docker-compose.yml

docker-compose up -d

sleep 300

docker-compose ps
```

### 🌐 Access Information

```text
URL: https://localhost:443

Username: admin
Password: admin
```

---

## 🐝 Step 3: Deploy TheHive Case Management Platform

```bash
mkdir -p ~/thehive-soar

cd ~/thehive-soar
```

### 📄 Create Docker Compose Configuration

```yaml
version: '3.8'

services:

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.9

    environment:
      - discovery.type=single-node
      - cluster.name=hive
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms256m -Xmx256m"

    ports:
      - "9200:9200"

    volumes:
      - es_data:/usr/share/elasticsearch/data

  thehive:
    image: thehiveproject/thehive4:4.1.24-1

    depends_on:
      - elasticsearch

    ports:
      - "9000:9000"

    volumes:
      - thehive_data:/opt/thp/thehive/data

    command: '--no-config --no-config-secret'

volumes:
  es_data:
  thehive_data:
```

### ▶️ Start Services

```bash
docker-compose up -d

sleep 120

docker-compose ps
```

### 🌐 Access TheHive

```text
http://localhost:9000
```

---

## 🧠 Step 4: Deploy Cortex Analysis Engine

```bash
mkdir -p ~/cortex-soar

cd ~/cortex-soar
```

### 📄 Create Docker Compose Configuration

```yaml
version: '3.8'

services:

  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:7.17.9

    environment:
      - discovery.type=single-node
      - cluster.name=cortex
      - xpack.security.enabled=false
      - "ES_JAVA_OPTS=-Xms256m -Xmx256m"

    ports:
      - "9201:9200"

    volumes:
      - cortex_es_data:/usr/share/elasticsearch/data

  cortex:
    image: thehiveproject/cortex:3.1.7-1

    depends_on:
      - elasticsearch

    ports:
      - "9001:9001"

    volumes:
      - cortex_jobs:/tmp/cortex-jobs

    environment:
      - 'JOB_DIRECTORY=/tmp/cortex-jobs'

volumes:
  cortex_es_data:
  cortex_jobs:
```

### ▶️ Start Cortex

```bash
docker-compose up -d

sleep 90

docker-compose ps
```

### 🌐 Access Cortex

```text
http://localhost:9001
```

---

# 🔗 Task 2: Create SOAR Integration Framework

## 📁 Step 1: Create Directory Structure

```bash
mkdir -p ~/soar-integration/{connectors,playbooks,workflows,logs}

cd ~/soar-integration

pip3 install requests urllib3 pyyaml
```

---

## 🔌 Step 2: Create Wazuh API Connector

### 📄 File: `connectors/wazuh_connector.py`

```python
#!/usr/bin/env python3

import requests
import logging
from requests.auth import HTTPBasicAuth
import urllib3

urllib3.disable_warnings(
    urllib3.exceptions.InsecureRequestWarning
)

class WazuhConnector:

    """
    Connector for Wazuh SIEM API integration.
    """

    def __init__(
        self,
        url: str,
        username: str,
        password: str
    ):

        self.url = url
        self.username = username
        self.password = password
        self.token = None

    def authenticate(self) -> bool:
        pass

    def get_alerts(
        self,
        limit: int = 10,
        min_level: int = 0
    ) -> list:
        pass

    def get_agent_info(
        self,
        agent_id: str
    ) -> dict:
        pass
```

---

## 🐝 Step 3: Create TheHive API Connector

### 📄 File: `connectors/thehive_connector.py`

```python
#!/usr/bin/env python3

import requests
import logging
from datetime import datetime

class TheHiveConnector:

    """
    Connector for TheHive Case Management Platform.
    """

    def __init__(
        self,
        url: str,
        username: str = None,
        password: str = None
    ):

        self.url = url
        self.session = None

    def login(
        self,
        username: str,
        password: str
    ) -> bool:
        pass

    def create_case(
        self,
        title: str,
        description: str,
        severity: int = 2,
        tags: list = None
    ) -> str:
        pass

    def add_observable(
        self,
        case_id: str,
        data_type: str,
        data: str
    ) -> bool:
        pass

    def update_case_status(
        self,
        case_id: str,
        status: str
    ) -> bool:
        pass
```

---

# 🤖 Task 3: Develop Automated Response Playbooks

## 🚨 Step 1: Malware Detection Response Playbook

### 📄 File: `playbooks/malware_response.py`

```python
#!/usr/bin/env python3

import logging
from datetime import datetime

class MalwareResponsePlaybook:

    """
    Automated Malware Response Playbook
    """

    def __init__(self):

        self.playbook_name = (
            "Malware Detection Response"
        )

        self.version = "1.0"

    def execute(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def isolate_host(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def collect_forensics(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def scan_system(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def update_threat_intel(
        self,
        alert_data: dict
    ) -> dict:
        pass
```

---

## 🔐 Step 2: Brute Force Attack Response Playbook

### 📄 File: `playbooks/bruteforce_response.py`

```python
#!/usr/bin/env python3

import logging
from datetime import datetime

class BruteForceResponsePlaybook:

    """
    Automated Brute Force Response Playbook
    """

    def __init__(self):

        self.playbook_name = (
            "Brute Force Attack Response"
        )

        self.version = "1.0"

    def execute(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def block_source_ip(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def analyze_attack_pattern(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def check_account_compromise(
        self,
        alert_data: dict
    ) -> dict:
        pass

    def enforce_security_policy(
        self,
        alert_data: dict
    ) -> dict:
        pass
```

---

# ⚙️ Task 4: Build Workflow Orchestration Engine

## 🧩 Step 1: Create Workflow Orchestrator

### 📄 File: `workflows/orchestrator.py`

```python
#!/usr/bin/env python3

import sys
import os
import logging

from datetime import datetime

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from connectors.wazuh_connector import WazuhConnector
from connectors.thehive_connector import TheHiveConnector

from playbooks.malware_response import (
    MalwareResponsePlaybook
)

from playbooks.bruteforce_response import (
    BruteForceResponsePlaybook
)


class WorkflowOrchestrator:

    """
    Main SOAR Workflow Engine
    """

    def __init__(
        self,
        config: dict
    ):
        pass

    def process_alerts(
        self,
        poll_interval: int = 60
    ):
        pass

    def route_alert(
        self,
        alert: dict
    ) -> str:
        pass

    def execute_playbook(
        self,
        playbook_name: str,
        alert: dict
    ) -> dict:
        pass

    def create_case_from_alert(
        self,
        alert: dict,
        playbook_results: dict
    ) -> str:
        pass
```

---

## 📄 Step 2: Create Configuration File

### File: `config.yaml`

```yaml
wazuh:
  url: "https://localhost:55000"
  username: "wazuh"
  password: "wazuh"
  poll_interval: 60
  min_alert_level: 7

thehive:
  url: "http://localhost:9000"
  username: "admin@thehive.local"
  password: "admin123"

cortex:
  url: "http://localhost:9001"
  api_key: ""

playbooks:

  malware_detection:
    enabled: true
    rule_ids:
      - 510
      - 511
      - 512
      - 553
      - 554
    severity: 3

  brute_force:
    enabled: true
    rule_ids:
      - 5710
      - 5712
      - 5720
    severity: 2

logging:
  level: "INFO"
  file: "logs/soar_integration.log"
```

---

## 🚀 Step 3: Create Main Execution Script

### 📄 File: `main.py`

```python
#!/usr/bin/env python3

import yaml
import logging
import sys

from workflows.orchestrator import (
    WorkflowOrchestrator
)

def setup_logging(
    config: dict
):
    pass

def load_config(
    config_file: str = 'config.yaml'
) -> dict:
    pass

def main():

    pass

if __name__ == "__main__":
    main()
```

---

# 🧪 Task 5: Test and Validate SOAR Integration

## 🔥 Step 1: Generate Test Alerts

### Generate Brute Force Attempts

```bash
for i in {1..10}
do
    ssh invalid_user@localhost 2>/dev/null
    sleep 2
done
```

### Create Test File

```bash
echo "test" > /tmp/test_file.txt
```

---

## 🧪 Step 2: Create Integration Tests

### 📄 File: `tests/test_integration.py`

```python
#!/usr/bin/env python3

import unittest
import sys
import os

sys.path.append(
    os.path.dirname(
        os.path.dirname(__file__)
    )
)

from connectors.wazuh_connector import (
    WazuhConnector
)

from connectors.thehive_connector import (
    TheHiveConnector
)


class TestSOARIntegration(
    unittest.TestCase
):

    def test_wazuh_authentication(self):
        pass

    def test_wazuh_alert_retrieval(self):
        pass

    def test_thehive_case_creation(self):
        pass

    def test_playbook_execution(self):
        pass


if __name__ == '__main__':
    unittest.main()
```

---

## ▶️ Step 3: Run Integration

```bash
cd ~/soar-integration

python3 main.py
```

---

## 📊 Monitor Logs

```bash
tail -f logs/soar_integration.log
```

---

## 🐝 Verify Cases in TheHive

```text
Open Browser:

http://localhost:9000
```

Verify:

* New Cases Created
* Observables Added
* Playbook Results Attached
* Incident Workflow Executed

---

# 📊 Expected Outcomes

After completing this lab, you should have:

| Component     | Outcome                        |
| ------------- | ------------------------------ |
| Wazuh SIEM    | Fully Operational              |
| TheHive       | Integrated Case Management     |
| Cortex        | Threat Analysis Platform       |
| Connectors    | Working API Integration        |
| Playbooks     | Malware & Brute Force Response |
| Orchestrator  | Automated Workflow Engine      |
| Case Creation | Automatic Incident Cases       |
| Logging       | Automated Action Logs          |

---

# 📂 Generated Artifacts

```text
soar-integration/
│
├── logs/
│   ├── soar_integration.log
│   ├── playbook_execution.log
│   └── workflow.log
│
├── reports/
│
├── cases/
│
└── artifacts/
```

---

# 🛠️ Troubleshooting

## Docker Containers Not Starting

```bash
df -h
```

```bash
sudo systemctl status docker
```

```bash
docker-compose logs
```

---

## API Authentication Failures

Verify:

```bash
curl -k https://localhost:55000
```

Check:

* Service startup time
* Credentials
* Network connectivity
* Firewall rules

---

## Playbooks Not Executing

Verify:

```bash
pip3 list
```

```bash
python3 -m pip install requests urllib3 pyyaml
```

Check:

* Alert severity
* Routing logic
* Playbook configuration
* Log files

---

## TheHive Case Creation Issues

```bash
docker-compose logs thehive
```

```bash
docker-compose logs elasticsearch
```

Verify:

* Elasticsearch Running
* Authentication Valid
* API Reachable
* Session Active

---

# 🎓 Learning Outcomes

After completing this lab, you will have:

✅ Deployed Wazuh SIEM

✅ Deployed TheHive Case Management

✅ Deployed Cortex Analysis Engine

✅ Created API Connectors

✅ Built Automated Response Playbooks

✅ Developed Workflow Orchestration

✅ Automated Case Creation

✅ Tested SOAR Workflows

✅ Improved Security Automation Skills

---

# 🔑 Key Takeaways

### 🤖 SOAR reduces manual incident response effort.

### ⚡ Automated playbooks accelerate containment and remediation.

### 🛡️ Integration between SIEM and SOAR improves security operations.

### 📊 Case management platforms improve analyst efficiency.

### 🔄 Workflow orchestration ensures consistent incident handling.

### 🚨 Automated response reduces Mean Time To Respond (MTTR).

---

# 🏁 Conclusion

In this lab, you implemented a complete Security Orchestration, Automation, and Response (SOAR) environment using Wazuh, TheHive, and Cortex. You created API connectors, developed automated response playbooks, and built a workflow orchestration engine capable of automatically responding to security incidents.

These technologies form the foundation of modern Security Operations Centers (SOCs), enabling organizations to automate repetitive security tasks, improve response consistency, and significantly reduce incident response times.

🚀 Continue expanding your SOAR platform with additional playbooks, threat intelligence integrations, endpoint response actions, and advanced orchestration workflows to create a production-ready security automation ecosystem.

---

<div align="center">

### 🚨 Detect • Orchestrate • Automate • Respond

⭐ Happy Hunting & Stay Secure! ⭐

</div>
