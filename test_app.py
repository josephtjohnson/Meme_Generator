import unittest
import app

class TestApp(unittest.TestCase):
  
  def test_app(self):
    with self.assertRaise(ValueError):
      app.setup.quote_files = []
      
