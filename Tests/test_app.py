
import unittest
import sys
import os

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app import app

class test_energy_API(unittest.TestCase):

    def setUp(self):
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_energy_by_region(self):
        response = self.client.get('/api/energy_by_region')
        self.assertEqual(response.status_code, 200)

    def test_region_data_valid(self):
        """Test region data"""
        response = self.client.get('/api/region/US%20East%20(Northern%20Virginia)')
        self.assertEqual(response.status_code, 200)

    def test_region_data_not_exist(self):
        """Tets regions that do not exist"""
        response = self.client.get('/api/region/NotExistRegion123')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total: 0', response.data)

    def test_region_data_empty_param(self):
        """emty parameter"""
        response = self.client.get('/api/region/')
        self.assertEqual(response.status_code, 404)

    def test_region_data_invalid_encoding(self):
        """special character"""
        response = self.client.get('/api/region/%ZZ')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Total: 0', response.data)

    def test_energy_by_region_invalid_method(self):
        """ Tes invalid method"""
        response = self.client.post('/api/energy_by_region')
        self.assertEqual(response.status_code, 405)  


    def test_region_data_special_characters(self):
        """test special characters (space, quotation)"""
        response = self.client.get('/api/region/Region%20With%20Spaces')
        self.assertEqual(response.status_code, 200) 