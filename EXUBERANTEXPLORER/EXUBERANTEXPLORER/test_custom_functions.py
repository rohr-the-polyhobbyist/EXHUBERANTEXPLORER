"""
Unit tests for bulk_data_request.py
"""

import unittest

from EXUBERANTEXPLORER.custom_functions import make_api_request, get_bulk_data_metadata, get_bulk_data_info
from EXUBERANTEXPLORER.constants import SCRYFALL_BULK_DATA_URL, HEADERS, TIMEOUT

class TestBulkDataRequest(unittest.TestCase):
    def test_make_api_request(self):
        # Test the make_api_request function
        response = make_api_request(SCRYFALL_BULK_DATA_URL, headers=HEADERS, timeout=TIMEOUT)
        self.assertEqual(response.status_code, 200)

    #def test_make_api_request_error(self):
        # Test the make_api_request function with an error
        #response = make_api_request(SCRYFALL_BULK_DATA_URL+"nonexistentendpoint6767")
        #self.assertEqual(response, None)

    def test_get_bulk_data_metadata(self):
        # Test the get_bulk_data_metadata function
        bulk_data = get_bulk_data_metadata(force=False)
        self.assertTrue("data" in bulk_data)

    def test_get_bulk_data_info(self):
        # Test the get_bulk_data_info function
        bulk_data_info = get_bulk_data_info(card_type="oracle_cards")
        self.assertTrue("Oracle Cards" == bulk_data_info["name"])

if __name__ == "__main__":
    unittest.main()