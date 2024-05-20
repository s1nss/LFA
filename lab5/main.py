import os

from chomskyConverter import ChomskyConverter
from grammar import Grammar


class Main:

    @staticmethod
    def run():
        my_grammar = Grammar(VN={'S', 'A', 'B', 'C'},
                             VT={'a', 'd'},
                             P={
                                 'S': {'dB', 'A'},
                                 'A': {'d', 'dS', 'aBdAB'},
                                 'B': {'a', 'dA', 'A', ''},
                                 'C': {'Aa'}
                             })
        print(my_grammar)

        convertor = ChomskyConverter(my_grammar.VN, my_grammar.VT, my_grammar.P)
        upd_grammar = convertor.convert()

        print(upd_grammar)


if os.path.basename(__file__) == "main.py":
    Main.run()
