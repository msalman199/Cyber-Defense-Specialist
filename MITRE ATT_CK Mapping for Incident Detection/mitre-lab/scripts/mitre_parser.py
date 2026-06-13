#!/usr/bin/env python3
"""
MITRE ATT&CK Framework Parser
Students: Complete the methods to parse and query MITRE ATT&CK data
"""

import json

class MitreAttackParser:
    def __init__(self, json_file_path):
        """Initialize parser with MITRE ATT&CK JSON data"""
        self.json_file_path = json_file_path
        self.techniques = {}
        self.tactics = {}
        self.load_data()
    
    def load_data(self):
        """
        Load MITRE ATT&CK data from JSON file
        TODO: Implement JSON file loading
        TODO: Call parse_techniques() and parse_tactics()
        """
        pass
    
    def parse_techniques(self):
        """
        Parse techniques from MITRE ATT&CK data
        TODO: Iterate through objects with type 'attack-pattern'
        TODO: Extract technique ID from external_references
        TODO: Store technique name, description, tactics, and platforms
        Hint: Look for 'mitre-attack' in source_name
        """
        pass
    
    def parse_tactics(self):
        """
        Parse tactics from MITRE ATT&CK data
        TODO: Iterate through objects with type 'x-mitre-tactic'
        TODO: Extract tactic information
        TODO: Store in self.tactics dictionary
        """
        pass
    
    def get_technique_by_id(self, technique_id):
        """
        Retrieve technique details by ID
        TODO: Return technique from self.techniques dictionary
        """
        pass
    
    def search_techniques_by_keyword(self, keyword):
        """
        Search techniques by keyword in name or description
        TODO: Implement case-insensitive search
        TODO: Return list of matching techniques with id, name, description
        """
        pass
