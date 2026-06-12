#!/bin/bash

EXPORT_DIR="/tmp/wireshark_analysis_export"
mkdir -p $EXPORT_DIR

echo "Exporting analysis results to $EXPORT_DIR"

# Copy all capture files
cp /tmp/*.pcap $EXPORT_DIR/ 2>/dev/null

# Export DNS queries
tshark -r /tmp/dns_traffic.pcap -T fields -e frame.time -e dns.qry.name -e dns.qry.type > $EXPORT_DIR/dns_queries.csv 2>/dev/null

# Export HTTP requests
tshark -r /tmp/http_analysis.pcap -T fields -e frame.time -e http.host -e http.request.method -e http.request.uri > $EXPORT_DIR/http_requests.csv 2>/dev/null

# Export TLS connections
tshark -r /tmp/tls_traffic.pcap -T fields -e frame.time -e ip.dst -e tls.handshake.extensions_server_name > $EXPORT_DIR/tls_connections.csv 2>/dev/null

# Copy analysis scripts
cp /tmp/analyze_*.sh $EXPORT_DIR/
cp /tmp/detect_*.sh $EXPORT_DIR/
cp /tmp/comprehensive_analysis.sh $EXPORT_DIR/

# Create summary
echo "Analysis completed on: $(date)" > $EXPORT_DIR/summary.txt
echo "Files analyzed: $(ls /tmp/*.pcap 2>/dev/null | wc -l)" >> $EXPORT_DIR/summary.txt
echo "Total packets: $(tshark -r /tmp/*.pcap -T fields -e frame.number 2>/dev/null | wc -l)" >> $EXPORT_DIR/summary.txt

echo "Export completed. Files available in: $EXPORT_DIR"
ls -la $EXPORT_DIR
