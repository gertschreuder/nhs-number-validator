#!/usr/bin/env python
# coding=utf-8

import unittest
from src.validator import Validator


class ValidatorTests(unittest.TestCase):

    def setUp(self):
        self.validator = Validator()

    def test_validatorNone(self):
        self.validator.validate(None)
        self.assertFalse(self.validator.isValid)

    def test_validatorNum(self):
        self.validator.validate("None")
        self.assertFalse(self.validator.isValid)

        self.validator.validate("12a312")
        self.assertFalse(self.validator.isValid)

        self.validator.validate(True)
        self.assertFalse(self.validator.isValid)

        val = Validator()
        self.validator.validate(val)
        self.assertFalse(self.validator.isValid)

        self.validator.validate("1745438912")
        self.assertTrue(self.validator.isValid)

    def test_validatorTrim(self):
        self.validator.validate(" 1745438912")
        self.assertTrue(self.validator.isValid)
        self.validator.validate("1745438912 ")
        self.assertTrue(self.validator.isValid)

    def test_validatorLen(self):
        self.validator.validate(" 1745438912")
        self.assertTrue(self.validator.isValid)
        self.validator.validate(" 174543812")
        self.assertFalse(self.validator.isValid)
        self.validator.validate("745438912")
        self.assertFalse(self.validator.isValid)
        self.validator.validate("1745438912")
        self.assertTrue(self.validator.isValid)

    def test_validator(self):
        # test remainder 10
        self.validator.validate("1645418912")
        self.assertFalse(self.validator.isValid)
        # test remainder 11
        self.validator.validate("1645418822")
        self.assertFalse(self.validator.isValid)

    def tearDown(self):
        self.validator = None


if __name__ == '__main__':
    unittest.main(exit=False)
