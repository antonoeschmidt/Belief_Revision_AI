import unittest

from sympy import Symbol
from sympy.logic.boolalg import *

from agent import Entail
from knowledge_base import Knowledge_base

class TestEntails(unittest.TestCase):

#### Single clause KBs
    def test_p_entails_p(self):
        # https://www.umsu.de/trees/#p|=p
        # p|= p is true

        # Arrange
        p = Symbol('P')

        kb = Knowledge_base()
        kb.add(p)

        sentence = p

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_p_Entails_not_p(self):
        # https://www.umsu.de/trees/#p|=~3p
        # p|= ¬p is false

        # Arrange
        p = Symbol('P')

        kb = Knowledge_base()
        kb.add(p)

        sentence = Not(p)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

    def test_p_Entails_q(self):
        # https://www.umsu.de/trees/#p|=q
        # p|=q is false

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(p)

        sentence = q

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

    def test_p_and_q_Entails_p(self):
        # https://www.umsu.de/trees/#p~1q|=p
        # p∧q|= p is true

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(And(p,q))

        sentence = p

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_p_or_q_Entails_p(self):
        # https://www.umsu.de/trees/#p~1q|=p
        # p∨q|= p is false

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(Or(p,q))

        sentence = p

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

    def test_not_p_imples_q_Entails_q_and_p(self):
        # https://www.umsu.de/trees/#~3p~5q|=p~1q
        # ¬p→q |= p∧q is False
        # correspons to test_more_than_one_resolvant

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))

        sentence = And(q, p)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

    def test_not_p_imples_q_Entails_q_or_p(self):
        # https://www.umsu.de/trees/#~3p~5q|=p~1q
        # ¬p→q |= p∨q is true

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))

        sentence = Or(q, p)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_not_p_implies_q_Entails_p_and_q(self):
        # https://www.umsu.de/trees/#~3p~5q|=p~1r
        # ¬p→q|=p∧r is false

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

    def test_not_p_implies_q_Entails_p_or_q(self):
        # https://www.umsu.de/trees/#~3p~5q|=p~1r
        # ¬p→q|=p∨r is false

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')
        r = Symbol('R')

        kb = Knowledge_base()
        kb.add(Implies(Not(p), q))

        sentence = Or(p,r)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)

#### Multi clause KBs
    def test_multi_clause_pq(self):
        # https://www.umsu.de/trees/#p%E2%88%A8q,%C2%ACp|=q
        # p∨q,¬p|=q is true

        # Arrange
        p = Symbol('P')
        q = Symbol('Q')

        kb = Knowledge_base()
        kb.add(Or(p,q))
        kb.add(Not(p))

        sentence = q

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_multi_clause_pqrs(self):
        # https://www.umsu.de/trees/#(~3p~5q)~1(q~5p)~1(p~5(r~1s))|=p~1r~1s
        # (¬p→q)∧(q→p)∧(p→(r∧s))|= p∧r∧s is true

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

    def test_multi_clause_abc(self):
        # https://www.umsu.de/trees/#A~4(B~2C),~3A|=~3B
        # A↔(B∨C), ¬A |=¬B is true

        # Arrange
        a = Symbol('A')
        b = Symbol('B')
        c = Symbol('C')

        kb = Knowledge_base()
        kb.add(Or(Not(a),b,c))
        kb.add(Or(a,Not(b)))
        kb.add(Or(a,Not(c)))
        kb.add(Not(a))

        sentence = Not(b)

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertTrue(result)

    def test_multi_clause_abc_2(self):
        # https://www.umsu.de/trees/#A~4(B~2C),~3A|=B
        # A↔(B∨C), ¬A |=¬B is false

        # Arrange
        a = Symbol('A')
        b = Symbol('B')
        c = Symbol('C')

        kb = Knowledge_base()
        kb.add(Or(Not(a),b,c))
        kb.add(Or(a,Not(b)))
        kb.add(Or(a,Not(c)))
        kb.add(Not(a))

        sentence = b

        # Act
        result = Entail(kb, sentence)

        # Assert
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
