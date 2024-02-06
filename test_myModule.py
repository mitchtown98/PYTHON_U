import unittest
import myModule

class TestMyModule(unittest.TestCase):

  def test_add(self):
    result = myModule.add(100, 100)
    self.assertEqual(result, 200)

  def test_divide(self):
    self.assertEqual(myModule.divide(8, 4), 2)
    
    #self.assertRaises(ValueError, myModule.divide, 10, 0)
    with self.assertRaises(ValueError):
      myModule.divide(10, 0)


if __name__ == '__main__':
  unittest.main()