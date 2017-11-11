# (from: https://qiita.com/masashi127/items/5bfcba5cad8e82958844)

import unittest
import nwtgck_hello

class NwtgckHelloTest(unittest.TestCase):

  def test_1(self):
    self.assertEqual(nwtgck_hello.hello(), "hello, world from setup-py-prac!!")


def suite():
  suite = unittest.TestSuite()
  suite.addTest(unittest.makeSuite(NwtgckHelloTest))
  return suite