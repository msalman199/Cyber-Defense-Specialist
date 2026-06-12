#!/bin/bash

echo "=== DNS Traffic Analysis ==="
echo "Analyzing DNS queries from capture file..."

# Extract DNS queries using tshark
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name -Y "dns.flags.response == 0" > /tmp/dns_queries.txt

echo "Top DNS queries:"
sort /tmp/dns_queries.txt | uniq -c | sort -nr | head -10

echo -e "\n=== Potential Suspicious Domains ==="
# Look for suspicious patterns
grep -E "(malware|suspicious|phishing|botnet|trojan)" /tmp/dns_queries.txt || echo "No obviously suspicious domains found"

echo -e "\n=== Unusual TLD Analysis ==="
# Extract and analyze top-level domains
grep -o '\.[a-z]*$' /tmp/dns_queries.txt | sort | uniq -c | sort -nr

echo -e "\n=== DNS Response Analysis ==="
# Analyze DNS responses
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.resp.name -e dns.a -Y "dns.flags.response == 1 and dns.a" | head -10
