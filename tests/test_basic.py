import os
import unittest
import botocore
from mock import patch, call
import awstwitter
import StringIO
import json

TESTDATA_FILENAME = os.path.join(os.path.dirname(__file__), 'ssm_response.json')

@patch('botocore.client.BaseClient._make_api_call')
class BasicCredentialsTest(unittest.TestCase):
    
    def test_retrieval(self, boto_mock):
        testdata = json.loads(open(TESTDATA_FILENAME).read())
        boto_mock.side_effect = [testdata]
        response = awstwitter.retrieve_credentials('test')
        assert len(response) == 4
        assert response['access_token_secret'] == 'r_access_token_secret'
        assert response['access_token'] == 'r_access_token'

if __name__ == '__main__':
    unittest.main()