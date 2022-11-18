import datetime
import os
import sys
from pathlib import Path
import unittest
sys.path.append('')
from functions import functions
# docs_from_tests setup
from docs_from_tests.instrument_call_hierarchy import (
    instrument_and_import_package,
    initialise_call_hierarchy,
    finalise_call_hierarchy
)

instrument_and_import_package(
    os.path.join(
        Path(__file__).parent.absolute(),
        '..',
        'functions'
    ), 'functions'
)


class TestFunctions(unittest.TestCase):

    def test_sumar(self):
        # Start sequence
        initialise_call_hierarchy('start')
        # Test
        self.assertEqual(functions.sumar(2, 3), 5)
        self.assertEqual(functions.sumar(-4, 8, -2), 2)
        self.assertEqual(functions.sumar(3, -15, 8, 0, -3), -7)
        self.assertEqual(functions.sumar(1, [3, 2], 9), None)
        self.assertEqual(functions.sumar(3, 6, '10'), None)
        # End sequence
        root_call = finalise_call_hierarchy()
        # Return sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Write sequence file in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__),
            '..',
            'docs',
            'diagrama_de_secuencia_suma.md'
            )
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_restar(self):
        # Start sequence
        initialise_call_hierarchy('start')
        # Test
        self.assertEqual(functions.restar(6, 2), 4)
        self.assertEqual(functions.restar(8, -5, -4), 17)
        self.assertEqual(functions.restar(-5, 11, -4, 1, -3), -10)
        self.assertEqual(functions.restar(4, {-4, 1}, -7), None)
        self.assertEqual(functions.restar({3: 2}, 4, '-8'), None)

        # End sequence
        root_call = finalise_call_hierarchy()
        # Return sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Write sequence file in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__),
            '..',
            'docs',
            'diagrama_de_secuencia_resta.md'
            )
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_multiplicar(self):
        # Start sequence
        initialise_call_hierarchy('start')
        # Test
        self.assertEqual(functions.multiplicar(0, 6), 0)
        self.assertEqual(functions.multiplicar(1, 3), 3)
        self.assertEqual(functions.multiplicar(7, -8, 6, 2), -672)
        self.assertEqual(functions.multiplicar(1, '3', 4, -2), None)
        self.assertEqual(functions.multiplicar(7, -8, 0, -1, {2, -4}), None)
        # End sequence
        root_call = finalise_call_hierarchy()
        # Return sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Write sequence file in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__),
            '..',
            'docs',
            'diagrama_de_secuencia_multiplicacion.md'
            )
        Path(sequence_diagram_filename).write_text(sequence_diagram)

    def test_dividir(self):
        # Start sequence
        initialise_call_hierarchy('start')
        # Test
        self.assertEqual(functions.dividir(5, 5), 1)
        self.assertEqual(functions.dividir(-12, 4), -3)
        self.assertEqual(functions.dividir(128, 2, 2, 2, 2, 2), 4)
        self.assertEqual(functions.dividir(12, 0, -2), None)
        self.assertEqual(functions.dividir(5, '4', -2, [1, 2]), None)
        # End sequence
        root_call = finalise_call_hierarchy()
        # Return sequence diagram
        sequence_diagram = root_call.sequence_diagram(
            show_private_functions=False,
            excluded_functions=[]
        )
        # Write sequence file in markdown format
        sequence_diagram_filename = os.path.join(
            os.path.dirname(__file__),
            '..',
            'docs',
            'diagrama_de_secuencia_division.md'
            )
        Path(sequence_diagram_filename).write_text(sequence_diagram)


def insert_header(file):
    file.write('\n')
    file.write('*************TESTING*************')
    file.write('\n')
    now = datetime.datetime.now()
    date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
    file.write(date_time)
    file.write('\n')
    return file


def main(out=sys.stderr, verbosity=2):
    loader = unittest.TestLoader()

    suite = loader.loadTestsFromModule(sys.modules[__name__])
    unittest.TextTestRunner(out, verbosity=verbosity).run(suite)


if __name__ == '__main__':
    with open('testing.txt', 'a') as f:
        f = insert_header(f)
        main(f)
