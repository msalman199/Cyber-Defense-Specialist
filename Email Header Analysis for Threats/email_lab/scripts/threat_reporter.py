#!/usr/bin/env python3
"""
Email Threat Reporter - Starter Template
Integrates all validation methods
Students: Complete the TODO sections
"""

from header_analyzer import EmailAnalyzer
from spf_validator import SPFValidator
from dkim_validator import DKIMValidator
from dmarc_validator import DMARCValidator
import json

class ThreatReporter:
    def __init__(self):
        self.header_analyzer = EmailAnalyzer()
        self.spf_validator = SPFValidator()
        self.dkim_validator = DKIMValidator()
        self.dmarc_validator = DMARCValidator()
    
    def analyze_email(self, email_file):
        """
        Perform comprehensive email analysis
        
        Args:
            email_file: Path to email file
        
        Returns:
            Dictionary with complete analysis results
        """
        report = {
            'file': email_file,
            'timestamp': None,  # TODO: Add timestamp
            'header_analysis': {},
            'spf_result': None,
            'dkim_result': None,
            'dmarc_result': None,
            'threat_score': 0,
            'threat_level': 'UNKNOWN',
            'recommendations': []
        }
        
        # TODO: Parse email
        # TODO: Run header analysis
        # TODO: Extract sender domain and IP
        # TODO: Run SPF validation
        # TODO: Run DKIM validation
        # TODO: Run DMARC validation
        # TODO: Calculate overall threat score
        # TODO: Generate recommendations
        
        return report
    
    def generate_recommendations(self, report):
        """
        Generate security recommendations
        
        Args:
            report: Analysis report dictionary
        
        Returns:
            List of recommendations
        """
        recommendations = []
        
        # TODO: Check SPF result and add recommendations
        # TODO: Check DKIM result and add recommendations
        # TODO: Check DMARC result and add recommendations
        # TODO: Check threat score and add recommendations
        
        return recommendations
    
    def export_report(self, report, output_file):
        """
        Export report to JSON file
        
        Args:
            report: Analysis report dictionary
            output_file: Output file path
        """
        # TODO: Write report to JSON file
        # TODO: Format for readability
        pass
    
    def print_report(self, report):
        """
        Print formatted report to console
        
        Args:
            report: Analysis report dictionary
        """
        # TODO: Print formatted report
        # TODO: Include all analysis results
        # TODO: Highlight critical findings
        pass

def main():
    reporter = ThreatReporter()
    
    samples = [
        'samples/legitimate.eml',
        'samples/phishing.eml',
        'samples/malware.eml'
    ]
    
    for sample in samples:
        report = reporter.analyze_email(sample)
        reporter.print_report(report)
        reporter.export_report(report, f'output/{sample.split("/")[-1]}.json')

if __name__ == "__main__":
    main()
