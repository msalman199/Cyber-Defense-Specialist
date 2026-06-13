#!/usr/bin/env python3
"""
Email Header Analyzer - Starter Template
Students: Complete the TODO sections
"""

import re
from email import message_from_file
from email.utils import parseaddr

class EmailAnalyzer:
    def __init__(self):
        self.threat_keywords = ['urgent', 'verify', 'suspended', 'click here', 'act now']
        self.suspicious_domains = ['bit.ly', 'tinyurl.com']
    
    def parse_email(self, filepath):
        """
        Parse email file and return message object
        
        Args:
            filepath: Path to email file
        
        Returns:
            Email message object
        """
        # TODO: Open file and parse email using message_from_file
        # TODO: Handle exceptions for file not found
        pass
    
    def extract_headers(self, message):
        """
        Extract important headers from email
        
        Args:
            message: Email message object
        
        Returns:
            Dictionary of header fields
        """
        headers = {}
        important = ['From', 'To', 'Subject', 'Return-Path', 'Reply-To', 
                    'Received', 'X-Originating-IP', 'Message-ID']
        
        # TODO: Loop through important headers
        # TODO: Extract each header value using message.get()
        # TODO: Store in headers dictionary
        
        return headers
    
    def analyze_received_path(self, message):
        """
        Analyze email routing path from Received headers
        
        Args:
            message: Email message object
        
        Returns:
            Dictionary with hop count and server list
        """
        received_headers = message.get_all('Received', [])
        
        # TODO: Count total hops
        # TODO: Extract server names using regex
        # TODO: Identify suspicious IP addresses
        
        return {
            'hops': 0,  # TODO: Calculate
            'servers': [],  # TODO: Extract
            'suspicious_ips': []  # TODO: Identify
        }
    
    def check_spoofing(self, message):
        """
        Detect potential email spoofing
        
        Args:
            message: Email message object
        
        Returns:
            List of spoofing indicators
        """
        indicators = []
        
        from_header = message.get('From', '')
        reply_to = message.get('Reply-To', '')
        return_path = message.get('Return-Path', '')
        
        # TODO: Compare From and Reply-To addresses
        # TODO: Extract domains from From and Return-Path
        # TODO: Check for domain mismatches
        # TODO: Add findings to indicators list
        
        return indicators
    
    def analyze_content(self, message):
        """
        Analyze email content for threats
        
        Args:
            message: Email message object
        
        Returns:
            List of suspicious content indicators
        """
        suspicious = []
        subject = message.get('Subject', '').lower()
        
        # TODO: Check subject for threat keywords
        # TODO: Check for suspicious domains in headers
        # TODO: Check for suspicious attachments
        
        return suspicious
    
    def calculate_threat_score(self, spoofing, content, routing):
        """
        Calculate overall threat score
        
        Args:
            spoofing: List of spoofing indicators
            content: List of content indicators
            routing: Dictionary of routing analysis
        
        Returns:
            Tuple of (score, threat_level)
        """
        score = 0
        
        # TODO: Add points for spoofing indicators (3 points each)
        # TODO: Add points for content indicators (2 points each)
        # TODO: Add points for suspicious IPs (4 points each)
        
        # TODO: Determine threat level based on score
        # HIGH: >= 10, MEDIUM: >= 5, LOW: > 0, MINIMAL: 0
        
        return score, "MINIMAL"  # TODO: Return calculated values
    
    def analyze(self, filepath):
        """
        Main analysis function
        
        Args:
            filepath: Path to email file
        """
        print(f"\n{'='*60}")
        print(f"ANALYZING: {filepath}")
        print(f"{'='*60}")
        
        # TODO: Parse email
        # TODO: Extract headers and display
        # TODO: Analyze routing
        # TODO: Check for spoofing
        # TODO: Analyze content
        # TODO: Calculate threat score
        # TODO: Display results

def main():
    analyzer = EmailAnalyzer()
    
    samples = [
        'samples/legitimate.eml',
        'samples/phishing.eml',
        'samples/malware.eml'
    ]
    
    for sample in samples:
        analyzer.analyze(sample)

if __name__ == "__main__":
    main()
