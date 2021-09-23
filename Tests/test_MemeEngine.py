import unittest
import QuoteEngine import MemeEngine

class TestMemeEngine(unittest.TestCase):
  
  def test_init(self):
    with self.assertRaises(Exception):
      MemeEngine.__init__(None)
    
  def test_meme(self):
    with self.assertRaises(Exception):
      MemeEngine.make_meme(None, None, None, None)
      MemeEngine.make_meme('./_data/photos/dog/xander_1.jpg', None, None, 501)
      MemeEngine.make_meme('./_data/photos/dog/xander_1.jpg', None, None, None)
    
if __name__ == '__main__':
  unittest.main()
