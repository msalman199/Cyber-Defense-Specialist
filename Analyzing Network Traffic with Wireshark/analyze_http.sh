#!/bin/bash

echo "=== HTTP Traffic Analysis ==="

echo "HTTP Methods Used:"
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.request.method | sort | uniq -c

echo -e "\n=== User Agents ==="
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.user_agent | sort | uniq -c

echo -e "\n=== Requested URLs ==="
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.host -e http.request.uri | head -10

echo -e "\n=== HTTP Response Codes ==="
tshark -r /tmp/http_analysis.pcap -Y "http.response" -T fields -e http.response.code | sort | uniq -c

echo -e "\n=== Potential Security Issues ==="
# Look for suspicious patterns
echo "Checking for suspicious user agents..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.user_agent | grep -iE "(bot|crawler|scanner|exploit)" || echo "No obviously suspicious user agents found"

echo -e "\nChecking for authentication headers..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.authorization | grep -v "^$" || echo "No authorization headers found"
