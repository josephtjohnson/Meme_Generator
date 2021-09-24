import unittest
import main

class TestMeme(unittest.TestCase):
  
  def test_meme(self):
    self.assertRaise(Exception, meme.generate_meme, None, None, None)
    self.assertRaises(FileNotFoundError, meme.generate_meme, None, None, None)
      
      
      
