#!/usr/bin/env python3
"""
SPF Validator - Starter Template
Students: Complete the TODO sections
"""

import dns.resolver
from ipaddress import ip_address, ip_network

class SPFValidator:
    def __init__(self):
        self.qualifiers = {'+': 'Pass', '-': 'Fail', '~': 'SoftFail', '?': 'Neutral'}
    
    def get_spf_record(self, domain):
        """
        Retrieve SPF record from DNS
        
        Args:
            domain: Domain name to query
        
        Returns:
            SPF record string or None
        """
        try:
            # TODO: Query TXT records for domain
            # TODO: Find record starting with 'v=spf1'
            # TODO: Return SPF record
            pass
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def parse_spf(self, spf_record):
        """
        Parse SPF record into mechanisms
        
        Args:
            spf_record: SPF record string
        
        Returns:
            Dictionary with mechanisms and modifiers
        """
        # TODO: Remove 'v=spf1' prefix
        # TODO: Split record into parts
        # TODO: Separate mechanisms from modifiers
        # TODO: Return parsed structure
        pass
    
    def validate_ip(self, domain, sender_ip):
        """
        Validate sender IP against SPF record
        
        Args:
            domain: Sender domain
            sender_ip: IP address of sender
        
        Returns:
            Validation result (Pass/Fail/SoftFail/Neutral/None)
        """
        print(f"\nValidating SPF: {domain} from {sender_ip}")
        
        # TODO: Get SPF record
        # TODO: Parse SPF record
        # TODO: Check each mechanism (ip4, ip6, a, mx, include, all)
        # TODO: Return first matching result
        
        return 'None'
    
    def check_ip4_mechanism(self, mechanism, sender_ip):
        """
        Check ip4 mechanism
        
        Args:
            mechanism: Mechanism string (e.g., 'ip4:192.0.2.0/24')
            sender_ip: Sender IP address
        
        Returns:
            True if IP matches, False otherwise
        """
        # TODO: Extract IP/network from mechanism
        # TODO: Check if sender_ip is in network
        # TODO: Return match result
        pass
    
    def create_spf_record(self, domain, authorized_ips, include_domains=None):
        """
        Generate SPF record for domain
        
        Args:
            domain: Domain name
            authorized_ips: List of authorized IP addresses
            include_domains: List of domains to include
        
        Returns:
            SPF record string
        """
        # TODO: Start with 'v=spf1'
        # TODO: Add ip4 mechanisms for each IP
        # TODO: Add include mechanisms
        # TODO: Add mx mechanism
        # TODO: End with '-all'
        pass

def main():
    validator = SPFValidator()
    
    # Test cases
    test_cases = [
        ('company.com', '192.0.2.10'),
        ('company.com', '203.0.113.50')
    ]
    
    for domain, ip in test_cases:
        result = validator.validate_ip(domain, ip)
        print(f"Result: {result}\n")
    
    # Create sample SPF record
    spf = validator.create_spf_record(
        'mycompany.com',
        ['192.0.2.0/24', '198.51.100.10'],
        ['_spf.google.com']
    )
    print(f"Sample SPF: {spf}")

if __name__ == "__main__":
    main()
