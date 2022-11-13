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
        self.assertEqual(functions.sumar(6, 13), 19)
        self.assertEqual(functions.sumar(-5, -4), -9)
        with self.assertRaises(TypeError):
            functions.sumar(5, 'hello')
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
        self.assertEqual(functions.restar(4, 1), 3)
        self.assertEqual(functions.restar(3, -2), 5)
        self.assertEqual(functions.restar(4, 6), -2)
        with self.assertRaises(TypeError):
            functions.restar(8, 'asd')
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
        self.assertEqual(functions.multiplicar(7, -8), -56)
        with self.assertRaises(TypeError):
            functions.multiplicar(1, 'asd')
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
        self.assertEqual(functions.dividir(12, 4), 3)
        with self.assertRaises(TypeError):
            functions.dividir(3, 'bye')
        # self.assertEqual(functions.dividir(3, 0), None)
        with self.assertRaises(ZeroDivisionError):
            functions.dividir(6, 0)
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
