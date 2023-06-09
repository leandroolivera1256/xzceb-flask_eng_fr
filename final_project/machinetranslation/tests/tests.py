import unittest
from translator import english_to_french,french_to_english

class TestTranslator(unittest.TestCase):
    def test_englishToFrench(self):
        self.assertEqual(english_to_french("Hello"),"Bonjour")
        self.assertEqual(english_to_french("Goodbye"),"Au revoir")
        self.assertEqual(english_to_french("Thank you"),"Merci")

    def test_frenchToEnglish(self):
        self.assertEqual(french_to_english("Bonjour"),"Hello")
        self.assertEqual(french_to_english("Au revoir"),"Goodbye")
        self.assertEqual(french_to_english("Merci"),"Thank you")

if __name__ == '__main__':
    unittest.main()
