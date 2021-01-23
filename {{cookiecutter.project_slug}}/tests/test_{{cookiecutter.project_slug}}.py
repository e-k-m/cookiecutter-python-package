import unittest

import {{ cookiecutter.project_slug }}


class TestSay(unittest.TestCase):
    def test_say(self):
        message = "I love batman"
        self.assertTrue(message in {{ cookiecutter.project_slug }}.say(message))


if __name__ == "__main__":
    unittest.main()
