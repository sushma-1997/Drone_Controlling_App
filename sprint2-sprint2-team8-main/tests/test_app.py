import sys
sys.path.append('..')

import unittest
from unittest.mock import patch
import json
from app import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
    
    def test_index_route(self):
        response = self.app.get('/')
        data = json.loads(response.data)
        self.assertEqual(data['message'], 'Welcome to the drone control API!')

    @patch('app.arm_plane')
    def test_arm_route(self, mock_arm_plane):
        response = self.app.get('/arm')
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'ARM command sent successfully!')
        mock_arm_plane.assert_called_once()

    @patch('app.disarm_plane')
    def test_disarm_route(self, mock_disarm_plane):
        response = self.app.get('/disarm')
        data = json.loads(response.data)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'DISARM command sent successfully!')
        mock_disarm_plane.assert_called_once()

    def test_throttle(self):
        # Test case for setting throttle to 50%
        response = self.app.post('/throttle', json={'throttle_percentage': 50})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Throttle set successfully!')
        
        # Test case for setting throttle to 150%, should raise ValueError
        response = self.app.post('/throttle', json={'throttle_percentage': 150})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Throttle percentage must be between 0 and 100.')
        
    def test_elevator_pitch(self):
        # Test case for setting elevator pitch to 50%
        response = self.app.post('/elevator_pitch', json={'elevator_pitch_percentage': 50})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'success')
        self.assertEqual(data['message'], 'Elevator/pitch set successfully!')
        
        # Test case for setting elevator pitch to -150%, should raise ValueError
        response = self.app.post('/elevator_pitch', json={'elevator_pitch_percentage': -150})
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'error')
        self.assertEqual(data['message'], 'Elevator/pitch percentage must be between -100 and 100.')


if __name__ == 'main':
    unittest.main()