import unittest

from os import path
from selenium import webdriver
from templatetags.encoder import obfuscation

APP_DIR = path.dirname(path.abspath(__file__))


class ObfuscationTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_text_obfuscated_and_deobfuscated_equals_original_text(self):
        target = "Text difficult to scrape."
        obfuscated = obfuscation(target)

        # import JS in charge of deobfuscation
        filepath = APP_DIR + r'\static\js\django_template_obfuscator.js'
        with open(filepath) as f:
            js = f"<script>{f.read()}</script>"

        html_content = f"""
            <p class="obfuscated">
            {obfuscated}
            </p>
        """
        self.browser.get(f"data:text/html;charset=utf-8, {html_content} {js}")
        deobfuscated_target = self.browser.find_element_by_xpath('//*[@class="obfuscated"]').text

        self.assertEqual(target, deobfuscated_target)

    def test_obfuscate_function_uses_rot13_encode_algorithm(self):
        obfuscated = obfuscation('Abracadabra!')

        self.assertEqual(obfuscated, 'Noenpnqnoen!')


if __name__ == '__main__':
    unittest.main()
