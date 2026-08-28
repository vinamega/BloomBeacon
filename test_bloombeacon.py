# test_bloombeacon.py
"""
Tests for BloomBeacon module.
"""

import unittest
from bloombeacon import BloomBeacon

class TestBloomBeacon(unittest.TestCase):
    """Test cases for BloomBeacon class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = BloomBeacon()
        self.assertIsInstance(instance, BloomBeacon)
        
    def test_run_method(self):
        """Test the run method."""
        instance = BloomBeacon()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
