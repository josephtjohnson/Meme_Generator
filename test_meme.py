import unittest
import meme

class TestMeme(unittest.TestCase):
  
  def test_meme(self):
    with self.assertRaise(Exception):
      meme.generate_meme(None, None, None)
      meme.generate_meme('./_data/photos/dog/xander_1.jpg', None, 'None')
      
