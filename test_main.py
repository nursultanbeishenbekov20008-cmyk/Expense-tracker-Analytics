import unittest
import requests

class TestExpenseAPI(unittest.TestCase):
    
    BASE_URL = 'http://localhost:5000/api'  # Replace with your API URL if different

    def test_add_expense(self):
        response = requests.post(f"{self.BASE_URL}/expenses", json={
            'amount': 100,
            'description': 'Test expense',
            'category': 'Food'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('id', response.json())

    def test_get_expenses(self):
        response = requests.get(f"{self.BASE_URL}/expenses")
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), list)

    def test_delete_expense(self):
        # Create an expense to delete
        response = requests.post(f"{self.BASE_URL}/expenses", json={
            'amount': 50,
            'description': 'Delete test expense',
            'category': 'Transport'
        })
        expense_id = response.json().get('id')
        
        response = requests.delete(f"{self.BASE_URL}/expenses/{expense_id}")
        self.assertEqual(response.status_code, 204)

if __name__ == '__main__':
    unittest.main()