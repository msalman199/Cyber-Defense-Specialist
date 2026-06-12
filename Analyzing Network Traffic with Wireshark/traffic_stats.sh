#!/bin/bash

echo "=== NETWORK TRAFFIC STATISTICS ==="

echo "Top 10 Destination IPs:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        tshark -r "$file" -T fields -e ip.dst | sort | uniq -c | sort -nr | head -10
    fi
done

echo -e "\nTop 10 Source IPs:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        tshark -r "$file" -T fields -e ip.src | sort | uniq -c | sort -nr | head -10
    fi
done

echo -e "\nProtocol Usage:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)"
        tshark -r "$file" -T fields -e _ws.col.Protocol | sort | uniq -c | sort -nr | head -10
        echo ""
    fi
done

echo -e "\nTraffic Timeline:"
for file in /tmp/*.pcap; do
    if [ -f "$file" ]; then
        echo "File: $(basename $file)"
        tshark -r "$file" -T fields -e frame.time | head -5
        echo "..."
        tshark -r "$file" -T fields -e frame.time | tail -5
        echo ""
    fi
done
