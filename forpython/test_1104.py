import unittest
import class_test

class TestStudent(unittest.TestCase):
	"""docstring for TestStudent"""
	# def __init__(self, arg):
	# 	super(TestStudent, self).__init__()
	# 	self.arg = arg
	def test_invalid(self):
		s1=class_test.Student(1,56)
		s2=class_test.Student('nio',102)
		with self.assertRaises(ValueError):
			s1.get_name()
		with self.assertRaises(ValueError):
			s2.get_grade()
	def test_80_100(self):
		s1=class_test.Student('lee',81)
		s2=class_test.Student('jsion',100)
		self.assertEqual(s1.get_grade(),'A')
		self.assertEqual(s2.get_grade(),'A')
	def test_60_80(self):
		s1=class_test.Student('lee',60)
		s2=class_test.Student('jsion',79)
		self.assertEqual(s1.get_grade(),'B')
		self.assertEqual(s2.get_grade(),'B')
	def test_0_60(self):
		s1=class_test.Student('lee',1)
		s2=class_test.Student('jsion',59)
		self.assertEqual(s1.get_grade(),'C')
		self.assertEqual(s2.get_grade(),'C')
if __name__=='__main__':
	unittest.main()
