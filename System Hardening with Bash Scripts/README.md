# 🛡️ System Hardening with Bash Scripts 

![Linux](https://img.shields.io/badge/Linux-Ubuntu_20.04-E95420?style=for-the-badge&logo=ubuntu)
![Bash](https://img.shields.io/badge/Bash-Scripting-4EAA25?style=for-the-badge&logo=gnubash)
![Security](https://img.shields.io/badge/CyberSecurity-System_Hardening-red?style=for-the-badge&logo=probot)
![Automation](https://img.shields.io/badge/Automation-Scripts-blue?style=for-the-badge&logo=github)

---

# 🎯 Objectives

✨ Create automated Bash scripts for Linux system hardening  
✨ Configure firewall rules using UFW and iptables  
✨ Secure SSH configurations through scripting  
✨ Implement user account security policies  
✨ Verify system hardening implementations  

---

# 📌 Prerequisites

✔ Basic Linux command line skills  
✔ File permissions & ownership knowledge  
✔ Basic Bash scripting  
✔ sudo/root access  

---

# 🖥️ Lab Environment

🧪 Al Nafi Ubuntu 20.04 LTS Cloud Machine

Includes:
- 🔐 Root (sudo) access  
- 🧰 Pre-installed Linux tools  
- 🖥️ Terminal access  

---

# 🚀 Task 1: System Hardening Script

---

## 🧱 Step 1: Create Working Directory

```bash
mkdir ~/system-hardening
cd ~/system-hardening
🛠️ Step 2: Main Hardening Script

📄 system_hardening.sh

#!/bin/bash

# 🛡️ System Hardening Script

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m'

# 📌 Logging Function
log_action() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')] $1${NC}" \
    | tee -a /var/log/system_hardening.log
}

# 🔐 Check Root Access
check_root() {
    if [[ $EUID -ne 0 ]]; then
        echo -e "${RED}Run as root!${NC}"
        exit 1
    fi
}

# 🔄 System Update
update_system() {
    log_action "Updating system packages..."
    apt update && apt upgrade -y
}

# 🔑 Password Policy
configure_password_policy() {
    log_action "Configuring password policies..."
    apt install -y libpam-pwquality
}

# 🚫 Disable Services
disable_unnecessary_services() {
    SERVICES=("apache2" "cups" "avahi-daemon")
    for service in "${SERVICES[@]}"; do
        systemctl disable $service
        log_action "Disabled $service"
    done
}

# 🧠 Kernel Hardening
configure_kernel_parameters() {
    log_action "Applying kernel security settings..."
    sysctl -w net.ipv4.ip_forward=0
    sysctl -w net.ipv4.conf.all.send_redirects=0
    sysctl -w net.ipv4.tcp_syncookies=1
}

# 🔒 File Permissions
secure_file_permissions() {
    chmod 600 /etc/shadow
    chmod 644 /etc/passwd
}

# 🚀 Main Execution
main() {
    echo "======================================"
    echo "   🛡️ SYSTEM HARDENING STARTED"
    echo "======================================"

    check_root
    update_system
    configure_password_policy
    disable_unnecessary_services
    configure_kernel_parameters
    secure_file_permissions

    log_action "System hardening completed successfully!"
}

main "$@"
▶️ Run Script
chmod +x system_hardening.sh
sudo ./system_hardening.sh
🔐 Task 2: User Security Script

📄 user_security.sh

#!/bin/bash

log_action() {
    echo "[SECURITY] $(date): $1"
}

# 🔍 Empty Password Check
check_empty_passwords() {
    awk -F: '($2==""){print $1}' /etc/shadow
}

# 👥 Duplicate UID Check
check_duplicate_uids() {
    cut -d: -f3 /etc/passwd | sort | uniq -d
}

# 🔒 Password Aging
set_password_aging() {
    for user in $(awk -F: '$3>=1000 {print $1}' /etc/passwd); do
        chage -M 90 -m 7 -W 14 $user
        log_action "Updated password aging for $user"
    done
}

main() {
    check_empty_passwords
    check_duplicate_uids
    set_password_aging
}

main "$@"
🔥 Task 3: Firewall Automation
🧱 UFW Firewall Script

📄 firewall_config.sh

#!/bin/bash

log_action() {
    echo "[FIREWALL] $(date): $1"
}

check_root() {
    [[ $EUID -ne 0 ]] && exit 1
}

configure_ufw() {
    apt install ufw -y
    ufw reset
    ufw default deny incoming
    ufw default allow outgoing
}

configure_basic_rules() {
    ufw allow 22/tcp   # SSH
    ufw allow 80/tcp   # HTTP
    ufw allow 443/tcp  # HTTPS
    ufw allow 53       # DNS
}

configure_rate_limiting() {
    ufw limit ssh
    ufw deny 3389
    ufw deny 445
}

enable_firewall() {
    ufw enable
    ufw status verbose
}

main() {
    check_root
    configure_ufw
    configure_basic_rules
    configure_rate_limiting
    enable_firewall
}

main "$@"
🧱 iptables Advanced Script

📄 iptables_advanced.sh

#!/bin/bash

configure_syn_flood_protection() {
    iptables -A INPUT -p tcp --syn -m limit --limit 1/s --limit-burst 3 -j ACCEPT
}

configure_port_scan_protection() {
    iptables -A INPUT -p tcp --tcp-flags ALL NONE -j DROP
    iptables -A INPUT -p tcp --tcp-flags ALL ALL -j DROP
}

block_invalid_packets() {
    iptables -A INPUT -m state --state INVALID -j DROP
}

save_rules() {
    apt install iptables-persistent -y
    netfilter-persistent save
}

main() {
    configure_syn_flood_protection
    configure_port_scan_protection
    block_invalid_packets
    save_rules
}

main "$@"
🔐 Task 4: SSH Hardening

📄 ssh_hardening.sh

#!/bin/bash

backup_ssh_config() {
    cp /etc/ssh/sshd_config /etc/ssh/sshd_config.bak
}

configure_ssh_security() {
    sed -i 's/#PermitRootLogin yes/PermitRootLogin no/' /etc/ssh/sshd_config
    sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/' /etc/ssh/sshd_config
    echo "MaxAuthTries 3" >> /etc/ssh/sshd_config
}

configure_ssh_banner() {
    echo "WARNING: Authorized Access Only" > /etc/ssh/banner
    echo "Banner /etc/ssh/banner" >> /etc/ssh/sshd_config
}

restart_ssh_service() {
    systemctl restart ssh
}

main() {
    backup_ssh_config
    configure_ssh_security
    configure_ssh_banner
    restart_ssh_service
}

main "$@"
🧪 SSH Validation Script

📄 validate_ssh.sh

#!/bin/bash

check_ssh_setting() {
    grep "$1" /etc/ssh/sshd_config | grep "$2"
}

main() {
    echo "🔍 SSH Validation Report"
    check_ssh_setting "PermitRootLogin" "no"
    check_ssh_setting "PasswordAuthentication" "no"
    check_ssh_setting "MaxAuthTries" "3"
}

main "$@"
📁 Task 5: File System Security

📄 filesystem_security.sh

#!/bin/bash

find_suid_files() {
    find / -perm -4000 2>/dev/null
}

find_world_writable() {
    find / -type f -perm -002 2>/dev/null
}

secure_temp_directories() {
    chmod 1777 /tmp /var/tmp
}

setup_aide() {
    apt install aide -y
    aideinit
}

main() {
    mkdir -p /var/log/security-reports
    find_suid_files
    find_world_writable
    secure_temp_directories
    setup_aide
}

main "$@"
✅ Task 6: Verification Script

📄 verify_hardening.sh

#!/bin/bash

verify_firewall() {
    ufw status verbose
}

verify_ssh_config() {
    grep "PermitRootLogin no" /etc/ssh/sshd_config
}

verify_services() {
    systemctl list-unit-files --state=enabled
}

generate_report() {
    echo "System Hardening Report" > /var/log/hardening_report.txt
}

main() {
    verify_firewall
    verify_ssh_config
    verify_services
    generate_report
}

main "$@"
🚀 Expected Outcomes

✔ Fully hardened Linux system
✔ Secure SSH configuration
✔ Active firewall rules
✔ Protected file system
✔ Automated security scripts

🧠 Skills Learned

✨ Linux security hardening
✨ Bash scripting automation
✨ Firewall configuration (UFW + iptables)
✨ SSH security controls
✨ System verification techniques

🚀 Conclusion

This lab teaches real-world Linux system hardening automation, used in enterprise security and SOC environments.

🛡️ You now know how to secure Linux systems using Bash scripting.
