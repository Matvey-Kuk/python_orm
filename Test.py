import unittest

from Models.TableA import *


class Test(unittest.TestCase):

    @staticmethod
    def test_save():
        table_a = TableA()
        table_a.set_value('ids', '')
        table_a.save()