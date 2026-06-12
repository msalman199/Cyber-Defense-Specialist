#!/bin/bash

echo "=== TLS Traffic Analysis ==="

echo "TLS Versions Used:"
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 1" -T fields -e tls.handshake.version | sort | uniq -c

echo -e "\n=== Server Names (SNI) ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.extensions_server_name" -T fields -e tls.handshake.extensions_server_name | sort | uniq

echo -e "\n=== Cipher Suites ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 2" -T fields -e tls.handshake.ciphersuite | head -10

echo -e "\n=== Certificate Analysis ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.handshake.type == 11" -T fields -e x509sat.printableString | head -5

echo -e "\n=== TLS Alerts ==="
tshark -r /tmp/tls_traffic.pcap -Y "tls.alert_message" -T fields -e tls.alert_message.level -e tls.alert_message.desc
