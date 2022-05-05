import unittest
import sys


def divide(a, b):
    return a/b

# class TestDevide(unittest.TestCase):
#     def test_divide_float_by_float(self):
#         self.assertEqual(divide(5.0,2.0), 2.5)
#         self.assertEqual(divide(7.0,2.0), 5.5)
      
#     def test_division_int_by_int(self):
#          self.assertAlmostEqual(divide(4.3), 1.3333)
    
    
#     def test_divition_by_zero(self):
#         with self.assertRaises(ZeroDivisionError):
#                   divide(5, 1)
            
#     def   test_wrong_inputs(self):
#          with self.assertRaises(TypeError):
#                   divide(5, 0)
            
# if __name__=='__main__':
#     unittest.main()
    

    
  
def convert(f, target='c'):
    if target == 'c':
        return (f - 32) / 1.8
    elif target == 'k':
        return ((f - 32) / 1.8) + 273.15
    else:
        raise Exception('wrong target')
        
        
class TestDivide(unittest.TestCase):
    def test_checkconvertion(self):
        self.assertEqual(convert(50), 10)
        self.assertAlmostEqual(convert(70), 21.111111111111)
        self.assertAlmostEqual(convert(90), 32.222222222222)        
        
        

            
if __name__=='__main__':
    unittest.main()       
    
# print(convert(50))
# print(convert(70))
# print(convert(90))

        
    
    
    