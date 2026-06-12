#!/bin/bash

echo "=== DNS Tunneling Detection ==="

# Analyze query lengths (DNS tunneling often uses long subdomain names)
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name -Y "dns.flags.response == 0" | \
while read query; do
    if [ ${#query} -gt 50 ]; then
        echo "Suspicious long DNS query: $query (Length: ${#query})"
    fi
done

echo -e "\n=== Query Type Analysis ==="
# Analyze DNS query types
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.type -Y "dns.flags.response == 0" | sort | uniq -c | sort -nr

echo -e "\n=== Subdomain Analysis ==="
# Count subdomains (many subdomains might indicate tunneling)
tshark -r /tmp/dns_traffic.pcap -T fields -e dns.qry.name -Y "dns.flags.response == 0" | \
grep -o '\.' | wc -l | awk '{print "Average dots per query: " $1/NR}'
