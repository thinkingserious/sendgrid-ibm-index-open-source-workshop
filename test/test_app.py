import app
try:
    import unittest2 as unittest
except ImportError:
    import unittest

class UnitTests(unittest.TestCase):

    def test_build_response(self):
        response = app.build_response(202)
        self.assertEqual(response, {"status": "success"})

        response = app.build_response(500)
        self.assertEqual(response, {"status": "error"})
