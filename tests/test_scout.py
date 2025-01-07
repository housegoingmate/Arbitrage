import unittest
from main import ArbitrageScout

class TestArbitrageScout(unittest.TestCase):
    def setUp(self):
        self.scout = ArbitrageScout()

    def test_retailer_config(self):
        """Test that retailer configuration is loaded correctly"""
        self.assertIn('Up There Store', self.scout.retailers)
        self.assertEqual(
            self.scout.retailers['Up There Store'],
            'https://uptherestore.com.au'
        )
        # Test configuration object
        self.assertEqual(len(self.scout.config.retailers), 1)
        self.assertEqual(self.scout.config.retailers[0].name, 'Up There Store')

    def test_resale_platform_config(self):
        """Test that resale platform configuration is loaded correctly"""
        self.assertIn('StockX', self.scout.resale_platforms)
        self.assertEqual(
            self.scout.resale_platforms['StockX'],
            'https://stockx.com'
        )
        # Test configuration object
        self.assertEqual(len(self.scout.config.resale_platforms), 2)
        self.assertEqual(self.scout.config.resale_platforms[0].name, 'StockX')

if __name__ == '__main__':
    unittest.main()
