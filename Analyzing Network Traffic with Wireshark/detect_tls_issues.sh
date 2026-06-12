#!/bin/bash

echo "=== TLS Security Issue Detection ==="

echo "Checking for weak TLS versions..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 1" -T fields -e tls.handshake.version | \
while read version; do
    case $version in
        "0x0300") echo "WARNING: SSL 3.0 detected (insecure)" ;;
        "0x0301") echo "WARNING: TLS 1.0 detected (deprecated)" ;;
        "0x0302") echo "WARNING: TLS 1.1 detected (deprecated)" ;;
        "0x0303") echo "INFO: TLS 1.2 detected (acceptable)" ;;
        "0x0304") echo "GOOD: TLS 1.3 detected (recommended)" ;;
    esac
done

echo -e "\nChecking for certificate validation issues..."
# Look for certificate-related alerts
tshark -r /tmp/tls_traffic.pcap -Y "tls.alert_message.desc == 42" -T fields -e frame.time || echo "No bad certificate alerts found"

echo -e "\nAnalyzing cipher suite security..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" -T fields -e tls.handshake.ciphersuite | \
while read cipher; do
    # Check for weak ciphers (this is a simplified check)
    if [[ $cipher == *"RC4"* ]] || [[ $cipher == *"DES"* ]]; then
        echo "WARNING: Weak cipher detected: $cipher"
    fi
done

echo -e "\nChecking for perfect forward secrecy..."
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" -T fields -e tls.handshake.ciphersuite | \
grep -E "(DHE|ECDHE)" && echo "Perfect Forward Secrecy supported" || echo "No PFS detected"
