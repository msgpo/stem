"""
Unit tests for the stem.Endpoint class.
"""

import unittest

import stem


class TestEndpoint(unittest.TestCase):
  def test_constructor(self):
    endpoint = stem.ORPort('12.34.56.78', 80)
    self.assertEqual('12.34.56.78', endpoint.address)
    self.assertEqual(80, endpoint.port)
    self.assertEqual(None, endpoint.link_protocols)

    endpoint = stem.ORPort('12.34.56.78', 80, [3])
    self.assertEqual('12.34.56.78', endpoint.address)
    self.assertEqual(80, endpoint.port)
    self.assertEqual([3], endpoint.link_protocols)

    endpoint = stem.DirPort('12.34.56.78', 80)
    self.assertEqual('12.34.56.78', endpoint.address)
    self.assertEqual(80, endpoint.port)

  def test_validation(self):
    self.assertRaises(ValueError, stem.DirPort, '12.34.56.78', 'hello')
    self.assertRaises(ValueError, stem.DirPort, '12.34.56.78', -5)
    self.assertRaises(ValueError, stem.DirPort, '12.34.56.78', None)
    self.assertRaises(ValueError, stem.DirPort, 'hello', 80)
    self.assertRaises(ValueError, stem.DirPort, -5, 80)
    self.assertRaises(ValueError, stem.DirPort, None, 80)
