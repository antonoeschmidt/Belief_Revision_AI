
import unittest

from sympy import Symbol
from sympy.logic.boolalg import *

from agent import Entail
from knowledge_base import Knowledge_base

class TestStringMethods(unittest.TestCase):

    def test_one(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))

        sentence = And(q, p)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_two(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))

        sentence = And(p,r)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

    def test_three(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')
        s = Symbol('S')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))
        kb.add(Implies(q,p))
        kb.add(Implies(p,And(r,s)))

        sentence = And(p,r,s)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_four(self):
        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(p)

        sentence = q

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
