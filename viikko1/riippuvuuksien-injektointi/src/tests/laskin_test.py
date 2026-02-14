import unittest
from laskin import Laskin


class StubIO:
    def __init__(self, inputs):
        self.inputs = inputs
        self.outputs = []

    def lue(self, teksti):
        return self.inputs.pop(0)

    def kirjoita(self, teksti):
        self.outputs.append(teksti)


class TestLaskin(unittest.TestCase):
    def test_yksi_summa_oikein(self):
        io = StubIO(["1", "3", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 4")


    def test_perform_two_operations(self):
        io = StubIO(["10", "20", "5", "5", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(io.outputs[0], "Summa: 30")
        self.assertEqual(io.outputs[1], "Summa: 10")
        
    def test_quit_with_second_input(self):
        io = StubIO(["1", "-9999"])
        laskin = Laskin(io)
        laskin.suorita()

        self.assertEqual(len(io.outputs), 0)