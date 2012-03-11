import logging
from paip import logic

def main():
    x = logic.Var('x')
    y = logic.Var('y')
    z = logic.Var('z')
    a = logic.Var('a')
    nil = logic.Atom('nil')
    more = logic.Var('more')
    zero = logic.Atom('0')

    length_nil = logic.Fact(logic.Relation('length', (nil, zero)))
    length_one = logic.Rule(
        logic.Relation('length',
                       (logic.Relation('pair', (x, more)),
                        logic.Relation('+1', [a]))),
        [logic.Relation('length', (more, a))])

    db = logic.Database()
    db.store(length_nil)
    db.store(length_one)

    print 'Database:'
    print db
    print

    four = logic.Relation(
        '+1', [logic.Relation(
                '+1', [logic.Relation(
                        '+1', [logic.Relation('+1', [zero])])])])
    
    query = logic.Relation('length', (x, four))
    print 'Query:', query
    print
    
    logic.prolog_prove([query], db)
