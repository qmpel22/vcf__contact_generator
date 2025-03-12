import unittest
import os
import sys


from vcf_contact_generator.contacts import create_single_contact


class TestCreateSingleContact(unittest.TestCase):

    def test_create_single_contact_valid(self):
        # Test: Prawidłowe dane
        filepath = 'test_contact.vcf'
        name = 'John Doe'
        phone = '+1234567890'
        
        result = create_single_contact(filepath, name, phone)
        
        # Sprawdzamy, czy plik został utworzony
        self.assertTrue(os.path.exists(filepath))
        
        # Sprawdzamy, czy w pliku znajduje się odpowiedni kontakt
        with open(filepath, 'r', encoding='utf-8') as file:
            content = file.read()
            self.assertIn('FN:John Doe', content)
            self.assertIn('TEL;TYPE=CELL:+1234567890', content)
        
        # Sprzątanie po teście
        os.remove(filepath)

    def test_create_single_contact_invalid_filepath(self):
        # Test: Nieprawidłowa ścieżka
        with self.assertRaises(ValueError):
            create_single_contact('', 'John Doe', '+1234567890')

    def test_create_single_contact_invalid_name(self):
        # Test: Nieprawidłowa nazwa
        with self.assertRaises(ValueError):
            create_single_contact('test_contact.vcf', '', '+1234567890')

    def test_create_single_contact_invalid_phone(self):
        # Test: Nieprawidłowy numer telefonu
        with self.assertRaises(ValueError):
            create_single_contact('test_contact.vcf', 'John Doe', '')

