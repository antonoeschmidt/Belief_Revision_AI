
import unittest

from sympy import Symbol
from sympy.logic.boolalg import *

from agent import Resolve

class TestStringMethods(unittest.TestCase):

    # http://logic.stanford.edu/intrologic/notes/chapter_05.html

    def test_basic_case(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')

        sentence1 = Or(p, q)
        sentence2 = Or(Not(q), r)

        # Act
        result = Resolve(sentence1, sentence2)

        # Assert
        self.assertEquals(result, [Or(p,r)])

    
    def test_set_single_occurences(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')

        sentence1 = Or(Not(p), q)
        sentence2 = Or(p, q)

        # Act
        result = Resolve(sentence1, sentence2)

        # Assert
        self.assertEquals(result, [q])

    
    def test_one_singleton(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')

        sentence1 = Or(p, q, r)
        sentence2 = Not(p)

        # Act
        result = Resolve(sentence1, sentence2)

        # Assert
        self.assertEquals(result, [Or(q,r)])


    def test_two_singleton(self):
        # Arrange
        p = Symbol('P')

        sentence1 = p
        sentence2 = Not(p)

        # Act
        result = Resolve(sentence1, sentence2)

        # Assert
        self.assertEquals(result, [])

    def test_more_than_one_resolvant(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        sentence1 = Or(p,q)
        sentence2 = Or(Not(p), Not(q))

        # Act
        result = Resolve(sentence1, sentence2)

        # Assert
        self.assertEquals(result, [Or(p, Not(p)), Or(q, Not(q))])

if __name__ == '__main__':
    unittest.main()
