#!/usr/bin/env python3
"""
Traffic Alert System
Students: Implement alert logic
"""

import os
import json
import logging
from datetime import datetime

class TrafficAlertSystem:
    def __init__(self, log_file="alerts.log"):
        self.alert_threshold = {
            'sql_injection': 1,
            'xss': 1,
            'path_traversal': 1,
            'unusual_user_agent': 3
        }
        self.log_file = log_file
        
        # Configure logging to write alerts to a file
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def check_alerts(self, analysis_results):
        """
        Check if alerts should be triggered by comparing counts to thresholds.
        
        Args:
            analysis_results: Dictionary with analysis data (e.g., {'sql_injection': 2})
            
        Returns:
            List of alerts to trigger
        """
        alerts = []
        
        for attack_type, count in analysis_results.items():
            # Check if the attack type exists in our thresholds
            if attack_type in self.alert_threshold:
                threshold = self.alert_threshold[attack_type]
                
                # Trigger alert if the count meets or exceeds the threshold
                if count >= threshold:
                    alert_msg = f"[ALERT] {attack_type.upper()} detected! Count: {count} (Threshold: {threshold})"
                    alerts.append(alert_msg)
                    
        return alerts
    
    def send_alert(self, alert_message):
        """
        Send alert notification to console and the log file.
        
        Args:
            alert_message: Alert text to send
        """
        # Print to console with high visibility
        print(f"\033[91m{alert_message}\033[0m") 
        
        # Log alert to file
        logging.info(alert_message)
        
        # (Optional) Placeholder for Webhook/Email
        # self._send_webhook(alert_message)

def main():
    print("Initializing Traffic Alert System...")
    alert_system = TrafficAlertSystem(log_file="alerts.log")
    
    # Mock data simulating parsed traffic analysis results
    mock_traffic_snapshots = [
        {
            'sql_injection': 0,
            'xss': 2,
            'path_traversal': 0,
            'unusual_user_agent': 1
        },
        {
            'sql_injection': 1,
            'xss': 0,
            'path_traversal': 3,
            'unusual_user_agent': 4
        }
    ]
    
    # Process each snapshot of analyzed traffic
    for index, snapshot in enumerate(mock_traffic_snapshots, 1):
        print(f"\n--- Processing Traffic Batch #{index} ---")
        
        # 1. Check for alerts
        triggered_alerts = alert_system.check_alerts(snapshot)
        
        # 2. Dispatch alerts if any are found
        if triggered_alerts:
            for alert in triggered_alerts:
                alert_system.send_alert(alert)
        else:
            print("Traffic clean. No alerts triggered.")

if __name__ == "__main__":
    main()
