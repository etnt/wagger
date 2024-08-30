import unittest
from unittest.mock import patch, Mock
from api_client import KeyAPI

# Run it as:  ./venv/binpython3 -m unittest test_api_client.py 



class TestKeyAPI(unittest.TestCase):
    def setUp(self):
        self.api = KeyAPI("http://test.com", "username", "password")

    @patch('api_client.requests.get')
    def test_get_top(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"key:top": [{"name": "John", "surname": "Doe"}]}
        mock_get.return_value = mock_response

        result = self.api.get_top("John", "Doe")
        
        mock_get.assert_called_once_with(
            "http://test.com/data/key:top=John,Doe",
            auth=("username", "password"),
            headers=self.api.headers
        )
        self.assertEqual(result, {"key:top": [{"name": "John", "surname": "Doe"}]})

    @patch('api_client.requests.post')
    def test_create_top(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 201
        mock_post.return_value = mock_response

        result = self.api.create_top("John", "Doe", 30, 42)
        
        mock_post.assert_called_once_with(
            "http://test.com/data",
            auth=("username", "password"),
            headers=self.api.headers,
            json={"key:top": [{"name": "John", "surname": "Doe", "age": 30, "shoe-size": 42}]}
        )
        self.assertTrue(result)

    @patch('api_client.requests.patch')
    def test_update_top(self, mock_patch):
        mock_response = Mock()
        mock_response.status_code = 204
        mock_patch.return_value = mock_response

        result = self.api.update_top("John", "Doe", age=31)
        
        mock_patch.assert_called_once_with(
            "http://test.com/data/key:top=John,Doe",
            auth=("username", "password"),
            headers=self.api.headers,
            json={"key:top": [{"age": 31}]}
        )
        self.assertTrue(result)

    @patch('api_client.requests.delete')
    def test_delete_top(self, mock_delete):
        mock_response = Mock()
        mock_response.status_code = 204
        mock_delete.return_value = mock_response

        result = self.api.delete_top("John", "Doe")
        
        mock_delete.assert_called_once_with(
            "http://test.com/data/key:top=John,Doe",
            auth=("username", "password"),
            headers=self.api.headers
        )
        self.assertTrue(result)

    @patch('api_client.requests.get')
    def test_get_age(self, mock_get):
        mock_response = Mock()
        mock_response.json.return_value = {"key:age": 30}
        mock_get.return_value = mock_response

        result = self.api.get_age("John", "Doe")
        
        mock_get.assert_called_once_with(
            "http://test.com/data/key:top=John,Doe/age",
            auth=("username", "password"),
            headers=self.api.headers
        )
        self.assertEqual(result, 30)

    @patch('api_client.requests.put')
    def test_set_shoe_size(self, mock_put):
        mock_response = Mock()
        mock_response.status_code = 204
        mock_put.return_value = mock_response

        result = self.api.set_shoe_size("John", "Doe", 43)
        
        mock_put.assert_called_once_with(
            "http://test.com/data/key:top=John,Doe/shoe-size",
            auth=("username", "password"),
            headers=self.api.headers,
            json={"key:shoe-size": 43}
        )
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
