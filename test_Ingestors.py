import unittest
from Ingestors import Ingestor

class TestIngestors(unittest.TestCase):
  
  def test_string(self):
    types = [True, 1, 1.2,]
    for type in types:
      result = Ingestor.parse(type)
      self.assertIsInstance(result, str)
  
  def test_fail(self):
    file_types = ['.jpg', '.png', '.xml']
    for x in file_types:
      result = Ingestor.parse(x)
      self.assertFalse(result)
    
  def test_pass(self):
    file_types = ['.pdf', '.csv', '.txt', '.docx'] 
    for x in file_types:
      result = Ingestor.parse(x)
      self.assertTrue(result) 
    
    
if __name__ == '__main__':
  unittest.main()
  
