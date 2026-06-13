#!/usr/bin/env python3
"""
DMARC Validator - Starter Template
Students: Complete the TODO sections
"""

import dns.resolver

class DMARCValidator:
    def __init__(self):
        self.policies = ['none', 'quarantine', 'reject']
    
    def get_dmarc_record(self, domain):
        """
        Retrieve DMARC record from DNS
        
        Args:
            domain: Domain name
        
        Returns:
            DMARC record string or None
        """
        # TODO: Query _dmarc.domain for TXT record
        # TODO: Find record starting with 'v=DMARC1'
        # TODO: Return DMARC record
        pass
    
    def parse_dmarc(self, dmarc_record):
        """
        Parse DMARC record into components
        
        Args:
            dmarc_record: DMARC record string
        
        Returns:
            Dictionary of DMARC parameters
        """
        # TODO: Split record by semicolons
        # TODO: Parse key=value pairs
        # TODO: Extract p, sp, pct, rua, ruf parameters
        # TODO: Return dictionary
        pass
    
    def validate_policy(self, domain, spf_result, dkim_result):
        """
        Validate email against DMARC policy
        
        Args:
            domain: Sender domain
            spf_result: SPF validation result
            dkim_result: DKIM validation result
        
        Returns:
            DMARC validation result
        """
        print(f"\nValidating DMARC: {domain}")
        print(f"SPF: {spf_result}, DKIM: {dkim_result}")
        
        # TODO: Get DMARC record
        # TODO: Parse DMARC policy
        # TODO: Check alignment (SPF and/or DKIM must pass)
        # TODO: Apply policy (none/quarantine/reject)
        # TODO: Return result
        pass
    
    def create_dmarc_record(self, domain, policy='quarantine', pct=100):
        """
        Generate DMARC record
        
        Args:
            domain: Domain name
            policy: DMARC policy (none/quarantine/reject)
            pct: Percentage of messages to apply policy
        
        Returns:
            DMARC record string
        """
        # TODO: Create DMARC record format
        # TODO: Include v, p, pct, rua parameters
        # TODO: Return formatted record
        pass

def main():
    validator = DMARCValidator()
    
    # Test DMARC validation
    test_cases = [
        ('company.com', 'Pass', 'Pass'),
        ('company.com', 'Fail', 'Fail'),
        ('company.com', 'Pass', 'Fail')
    ]
    
    for domain, spf, dkim in test_cases:
        result = validator.validate_policy(domain, spf, dkim)
        print(f"DMARC Result: {result}\n")
    
    # Create sample DMARC record
    record = validator.create_dmarc_record('mycompany.com', 'quarantine', 100)
    print(f"Sample DMARC Record:\n{record}")

if __name__ == "__main__":
    main()
