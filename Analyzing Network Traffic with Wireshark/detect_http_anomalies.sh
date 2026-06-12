#!/bin/bash

echo "=== HTTP Anomaly Detection ==="

echo "Checking for SQL Injection attempts..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.request.uri | \
grep -iE "(union|select|insert|delete|drop|'|;|--)" || echo "No SQL injection patterns detected"

echo -e "\nChecking for XSS attempts..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.request.uri | \
grep -iE "(<script|javascript:|onload=|onerror=)" || echo "No XSS patterns detected"

echo -e "\nChecking for directory traversal..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.request.uri | \
grep -E "(\.\.\/|\.\.\\)" || echo "No directory traversal patterns detected"

echo -e "\nChecking for unusual HTTP methods..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.request.method | \
grep -vE "^(GET|POST|HEAD|PUT|DELETE|OPTIONS)$" || echo "Only standard HTTP methods found"

echo -e "\nAnalyzing request sizes..."
tshark -r /tmp/http_analysis.pcap -Y "http.request" -T fields -e http.content_length | \
awk '{if($1>10000) print "Large request detected: " $1 " bytes"}'
