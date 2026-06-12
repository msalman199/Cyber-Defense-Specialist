#!/bin/bash

clear
echo "=================================="
echo "    SOC MONITORING DASHBOARD     "
echo "=================================="
echo ""

# Check system status
echo "SYSTEM STATUS:"
echo "- Elasticsearch: $(systemctl is-active elasticsearch)"
echo "- Kibana: $(systemctl is-active kibana)"
echo "- Logstash: $(systemctl is-active logstash)"
echo ""

# Check recent log entries
echo "RECENT SECURITY EVENTS (Last 10):"
echo "-----------------------------------"
tail -10 /var/log/auth.log | grep -E "(Failed|Accepted|Invalid)" || echo "No recent authentication events"
echo ""

# Check ElastAlert status
echo "ALERT SYSTEM STATUS:"
echo "--------------------"
if pgrep -f elastalert > /dev/null; then
    echo "- ElastAlert: RUNNING"
    echo "- Recent alerts: $(tail -5 /var/log/elastalert/elastalert.log | grep -c "Alert sent" || echo "0")"
else
    echo "- ElastAlert: STOPPED"
fi
echo ""

# Check Elasticsearch indices
echo "ELASTICSEARCH INDICES:"
echo "----------------------"
curl -s "localhost:9200/_cat/indices?v" | grep soc-logs || echo "No SOC indices found"
echo ""

# Display current time
echo "Last Updated: $(date)"
echo "=================================="
