import unittest
import pandas as pd
from src.machine_learning.model import train_model

class TestModel(unittest.TestCase):

    def setUp(self):
        """Prepare a sample dataset for testing."""
        self.sample_data = pd.DataFrame({
            'feature1': [1, 2, 3, 4, 5],
            'feature2': [5, 4, 3, 2, 1],
            'target': [0, 1, 0, 1, 0]
        })

    def test_train_model(self):
        """Test the training of the model."""
        model = train_model(self.sample_data, target_column='target')
        self.assertIsNotNone(model)  # Ensure that the model is not None

if __name__ == "__main__":
    unittest.main()