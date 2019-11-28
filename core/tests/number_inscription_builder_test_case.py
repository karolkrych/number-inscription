from django.test import TestCase

from core.utils import NumberInscriptionBuilder


class NumberInscriptionBuilderTestCase(TestCase):
    def test_get_inscription_with_ten_number(self):
        builder = NumberInscriptionBuilder('111')
        output = builder.get_inscription()
        expected_output = 'sto jedenaście'
        self.assertEqual(output, expected_output)

    def test_get_inscription_with_thousands_number(self):
        builder = NumberInscriptionBuilder('87654')
        output = builder.get_inscription()
        expected_output = 'osiemdziesiąt siedem tysięcy sześćset pięćdziesiąt cztery'
        self.assertEqual(output, expected_output)

    def test_get_inscription_with_millions_number(self):
        builder = NumberInscriptionBuilder('123456789')
        output = builder.get_inscription()
        expected_output = 'sto dwadzieścia trzy miliony czterysta pięćdziesiąt sześć tysięcy ' \
                          'siedemset osiemdziesiąt dziewięć'
        self.assertEqual(output, expected_output)

    def test_get_inscription_with_zero(self):
        builder = NumberInscriptionBuilder('0')
        output = builder.get_inscription()
        expected_output = 'zero'
        self.assertEqual(output, expected_output)

    def test_get_inscription_with_many_zeros(self):
        builder = NumberInscriptionBuilder('0000000000')
        output = builder.get_inscription()
        expected_output = 'zero'
        self.assertEqual(output, expected_output)

    def test_max_numbers(self):
        self.assertEqual(NumberInscriptionBuilder.max_numbers(), 15)
