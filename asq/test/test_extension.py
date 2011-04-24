import unittest
from asq._portability import function_name

from asq.extension import add_method, extend

__author__ = 'Robert Smallshire'

class TestExtension(unittest.TestCase):

    def test_add_method_default_name(self):

        class Extendee(object):
            pass

        instance = Extendee()

        self.assertFalse(hasattr(Extendee, "method"))
        self.assertFalse(hasattr(instance, "method"))

        def method(self):
            "This is the test extension method."
            return "The result of method()"

        add_method(method, Extendee)

        self.assertTrue(hasattr(Extendee, "method"))
        self.assertTrue(hasattr(instance, "method"))
        
        self.assertEqual(method.__doc__, Extendee.method.__doc__)
        self.assertEqual(function_name(method), function_name(Extendee.method))

        self.assertEqual(instance.method(), "The result of method()")

    def test_add_method_with_name(self):

        class Extendee(object):
            pass

        instance = Extendee()

        self.assertFalse(hasattr(Extendee, "method"))
        self.assertFalse(hasattr(instance, "method"))

        def method(self):
            "This is the test extension method."
            return "The result of method()"

        add_method(method, Extendee, "foo")

        self.assertTrue(hasattr(Extendee, "foo"))
        self.assertTrue(hasattr(instance, "foo"))

        self.assertEqual(method.__doc__, Extendee.foo.__doc__)
        self.assertEqual(function_name(method), function_name(Extendee.foo))

        self.assertEqual(instance.foo(), "The result of method()")

    def test_extend_decorator(self):

        class Extendee(object):
            pass

        instance = Extendee()

        self.assertFalse(hasattr(Extendee, "method"))
        self.assertFalse(hasattr(instance, "method"))
        self.assertFalse(hasattr(Extendee, "foo"))
        self.assertFalse(hasattr(instance, "foo"))

        @extend(Extendee)
        def method(self):
            "This is the test extension method."
            return "The result of method()"

        self.assertTrue(hasattr(Extendee, "method"))
        self.assertTrue(hasattr(instance, "method"))

        self.assertEqual(method.__doc__, Extendee.method.__doc__)
        # TODO: [asq 1.0] Check function name

        self.assertEqual(instance.method(), "The result of method()")
        self.assertEqual(function_name(method), function_name(Extendee.method))

    def test_extend_decorator_with_name(self):

        class Extendee(object):
            pass

        instance = Extendee()

        self.assertFalse(hasattr(Extendee, "method"))
        self.assertFalse(hasattr(instance, "method"))
        self.assertFalse(hasattr(Extendee, "foo"))
        self.assertFalse(hasattr(instance, "foo"))

        @extend(Extendee, "foo")
        def method(self):
            "This is the test extension method."
            return "The result of method()"

        self.assertTrue(hasattr(Extendee, "foo"))
        self.assertTrue(hasattr(instance, "foo"))

        self.assertEqual(method.__doc__, Extendee.foo.__doc__)
        self.assertEqual(function_name(method), function_name(Extendee.foo))

        self.assertEqual(instance.foo(), "The result of method()")