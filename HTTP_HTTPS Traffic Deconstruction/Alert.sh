# Append to summary if the alerts log exists and is not empty
if [ -s "$ALERTS_LOG" ]; then 
    echo "=== Alerts ===" >> "${OUTPUT_DIR}/summary.log" 
    tail -n 50 "$ALERTS_LOG" >> "${OUTPUT_DIR}/summary.log" 
fi 

main() { 
    echo "Starting Real-time HTTP/HTTPS Traffic Monitor (iface=$INTERFACE, window=${DURATION}s)" 
    
    while true; do 
        monitor_http_traffic 
        monitor_https_traffic 
        analyze_patterns 
        
        echo "Cycle complete. Logs in: $OUTPUT_DIR" 
        
        # Rotate pcap filenames for next cycle 
        HTTP_PCAP="${OUTPUT_DIR}/http_$(date +%s).pcap" 
        HTTPS_PCAP="${OUTPUT_DIR}/https_$(date +%s).pcap" 
        
        # Pause to match your window duration and prevent 100% CPU usage
        sleep "${DURATION:-10}"
    done 
}
