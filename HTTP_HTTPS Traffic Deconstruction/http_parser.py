#!/usr/bin/env python3
"""
HTTP Traffic Parser and Analyzer
Students: Complete the TODO sections to implement full functionality
"""

import re
import sys
from collections import defaultdict

class HTTPParser:
    def __init__(self):
        self.suspicious_patterns = {
            'sql_injection': [r'union\s+select', r'drop\s+table', r"'.*or.*'"],
            'xss': [r'<script>', r'javascript:', r'onerror='],
            'path_traversal': [r'\.\./', r'%2e%2e'],
            'command_injection': [r';\s*(cat|ls|whoami)', r'\|.*\|']
        }
    
    def parse_request(self, request_text):
        """
        Parse HTTP request into components.
        
        Args:
            request_text: Raw HTTP request string
            
        Returns:
            Dictionary with method, path, version, and headers
        """
        # TODO: Split request into lines
        # TODO: Extract method, path, and HTTP version from first line
        # TODO: Parse headers from remaining lines
        # TODO: Return structured dictionary
        pass
    
    def detect_anomalies(self, parsed_request):
        """
        Detect suspicious patterns in HTTP request.
        
        Args:
            parsed_request: Parsed request dictionary
            
        Returns:
            List of detected anomalies
        """
        anomalies = []
        
        # TODO: Check path against suspicious patterns
        # TODO: Validate User-Agent header
        # TODO: Check for suspicious headers (X-Forwarded-For, etc.)
        # TODO: Detect unusual request characteristics
        
        return anomalies
    
    def generate_report(self, requests):
        """
        Generate analysis report for all requests.
        
        Args:
            requests: List of HTTP request strings
        """
        # TODO: Parse all requests
        # TODO: Count methods, detect anomalies
        # TODO: Print formatted report with statistics
        pass

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 http_parser.py <input_file>")
        sys.exit(1)
    
    # TODO: Read input file
    # TODO: Split into individual requests
    # TODO: Create parser instance and generate report
    pass

if __name__ == "__main__":
    main()
