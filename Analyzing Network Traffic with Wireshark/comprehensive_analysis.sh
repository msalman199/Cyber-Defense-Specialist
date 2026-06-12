#!/bin/bash

REPORT_FILE="/tmp/network_analysis_report.txt"

echo "=== COMPREHENSIVE NETWORK TRAFFIC ANALYSIS REPORT ===" > $REPORT_FILE
echo "Generated on: $(date)" >> $REPORT_FILE
echo "Analyst: $(whoami)" >> $REPORT_FILE
echo "=========================================" >> $REPORT_FILE

echo -e "\n1. TRAFFIC SUMMARY" >> $REPORT_FILE
echo "Total packets captured:" >> $REPORT_FILE
ls -la /tmp/*.pcap | wc -l >> $REPORT_FILE

echo -e "\n2. PROTOCOL DISTRIBUTION" >> $REPORT_FILE
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)" >> $REPORT_FILE
        tshark -r "$file" -q -z io,phs | head -20 >> $REPORT_FILE
        echo "" >> $REPORT_FILE
    fi
done

echo -e "\n3. SECURITY FINDINGS" >> $REPORT_FILE
echo "DNS Analysis Results:" >> $REPORT_FILE
/tmp/analyze_dns.sh >> $REPORT_FILE 2>/dev/null

echo -e "\nHTTP Analysis Results:" >> $REPORT_FILE
/tmp/analyze_http.sh >> $REPORT_FILE 2>/dev/null

echo -e "\nTLS Analysis Results:" >> $REPORT_FILE
/tmp/analyze_tls.sh >> $REPORT_FILE 2>/dev/null

echo -e "\n4. RECOMMENDATIONS" >> $REPORT_FILE
echo "- Monitor DNS queries for unusual patterns" >> $REPORT_FILE
echo "- Implement HTTP security headers" >> $REPORT_FILE
echo "- Ensure TLS 1.2 or higher is used" >> $REPORT_FILE
echo "- Regular security monitoring recommended" >> $REPORT_FILE

echo "Report generated: $REPORT_FILE"
cat $REPORT_FILE
