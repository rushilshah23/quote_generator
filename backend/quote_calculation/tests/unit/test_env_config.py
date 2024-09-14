# import unittest
# from unittest.mock import patch, mock_open, MagicMock
# import os
# from dotenv import load_dotenv
# from src.configs.env_config import get_env_dir_path, get_environment, load_config, Config  # Adjust import as needed

# class TestConfig(unittest.TestCase):
    
#     @patch('os.path.dirname')
#     @patch('os.path.join')
#     def test_get_env_dir_path(self, mock_join, mock_dirname):
#         # Setup
#         mock_dirname.side_effect = ['/usr', '/usr/src', '/usr/src/app']
#         mock_join.return_value = '/usr/src/app/envs'

#         # Call
#         result = get_env_dir_path()

#         # Assert
#         self.assertEqual(result, '/usr/src/app/envs')
#         mock_dirname.assert_called()
#         mock_join.assert_called_with('/usr/src/app', 'envs')
    
#     @patch('os.environ.get')
#     @patch('dotenv.load_dotenv')
#     @patch('os.path.join')
#     def test_get_environment(self, mock_join, mock_load_dotenv, mock_get_environ):
#         # Setup
#         mock_join.return_value = '/usr/src/app/envs/.flaskenv'
#         mock_get_environ.return_value = 'DEVELOPMENT'

#         # Call
#         result = get_environment()

#         # Assert
#         self.assertEqual(result, 'DEVELOPMENT')
#         mock_load_dotenv.assert_called_with('/usr/src/app/envs/.flaskenv')
#         mock_get_environ.assert_called_with('ENVIRONMENT')
    
#     @patch('os.environ.get')
#     @patch('dotenv.load_dotenv')
#     @patch('os.path.join')
#     @patch('src.configs.env_config.get_environment')
#     def test_load_config(self, mock_get_environment, mock_join, mock_load_dotenv, mock_get_environ):
#         # Setup
#         mock_get_environment.return_value = 'PRODUCTION'
#         mock_join.return_value = '/usr/src/app/envs/.env.prod'
#         mock_get_environ.return_value = None

#         # Call
#         load_config()

#         # Assert
#         mock_get_environment.assert_called()
#         mock_load_dotenv.assert_called_with('/usr/src/app/envs/.env.prod')
    
#     @patch('dotenv.load_dotenv')
#     @patch('os.environ.get')
#     @patch('src.configs.env_config.get_environment')
#     def test_config_class(self, mock_get_environment, mock_get_environ, mock_load_dotenv):
#         # Setup
#         mock_get_environment.return_value = 'PRODUCTION'
#         mock_get_environ.side_effect = lambda key: {
#             'SERVER_PORT': '8000',
#             'SERVER_HOST': 'localhost',
#             'ENVIRONMENT': 'PRODUCTION'
#         }.get(key)
#         mock_load_dotenv = MagicMock()
        
#         # Call
#         config = Config()
#         result = config.get_config_object()

#         # Assert
#         self.assertEqual(result, {
#             'SERVER_PORT': '8000',
#             'SERVER_HOST': 'localhost',
#             'ENVIRONMENT': 'PRODUCTION'
#         })
#         mock_get_environment.assert_called()
#         mock_load_dotenv.assert_called()
#         mock_get_environ.assert_any_call('SERVER_PORT')
#         mock_get_environ.assert_any_call('SERVER_HOST')
#         mock_get_environ.assert_any_call('ENVIRONMENT')

#     @patch('os.path.join')
#     @patch('dotenv.load_dotenv')
#     @patch('src.configs.env_config.get_environment')
#     def test_load_config_invalid_environment(self, mock_get_environment, mock_load_dotenv, mock_join):
#         # Setup
#         mock_get_environment.return_value = 'INVALID_ENV'
#         mock_join.return_value = '/usr/src/app/envs/.env.invalid'
        
#         # Assert
#         with self.assertRaises(Exception) as context:
#             load_config()
#         self.assertEqual(str(context.exception), "Invalid environment value 'INVALID_ENV' found! Expected 'PRODUCTION', 'DEVELOPMENT', or 'TESTING'.")

# if __name__ == '__main__':
#     unittest.main()


import unittest
from unittest.mock import patch
from src.configs.env_config import get_env_dir_path


class TestEnvConfig(unittest.TestCase):

    @patch("os.path.dirname")
    @patch("os.path.join")
    def test_get_env_dir_path(self,mock_join,mock_dirname):
        mock_dirname.side_effect = ['/usr','/usr/src','/usr/src/app']
        mock_join.return_value = '/usr/src/app/envs'


        result = get_env_dir_path()

        self.assertEqual(result,'/usr/src/app/envs')


if __name__  == "__main__":
    unittest.main()