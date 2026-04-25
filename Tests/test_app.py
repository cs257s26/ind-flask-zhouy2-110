import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

class test_energy_API (unittest.TestCase):
    """Test cases for Energy Consumption API routes."""

    def setUp(self):
        """Set up test client before each test."""
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_energy_by_region(self):
        """Test first function in app"""
        response = self.client.get('/api/energy_by_region')
        self.assertEqual(response.status_code, 200)
    
    def test_region_data(self):
        """Test second function in app"""
        response = self.client.get('/api/region/US%20East%20(Northern%20Virginia)')
        self.assertEqual(response.status_code, 200)
