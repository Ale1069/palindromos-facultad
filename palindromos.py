import unittest

def is_palindrome(mystring):
    mystring = mystring.lower().replace(" ", "")  
    for i in range(len(mystring)//2): 
        if mystring[i] != mystring[-i-1]:
            return False
    return True


class TestPalindrome(unittest.TestCase):
       
    def test_a(self):
        resultado = is_palindrome("a")
        self.assertEqual(resultado, True)

    def test_b(self):
        resultado = is_palindrome("aa")
        self.assertEqual(resultado, True)

    def test_c(self):
        resultado = is_palindrome("ab")
        self.assertEqual(resultado, False)

    def test_c(self):
        resultado = is_palindrome("aba")
        self.assertEqual(resultado, True)

    def test_c(self):
        resultado = is_palindrome("acb")
        self.assertEqual(resultado, False)

    def test_c(self):
        resultado = is_palindrome("abba")
        self.assertEqual(resultado, True)

    def test_c(self):
        resultado = is_palindrome("abca")
        self.assertEqual(resultado, False)

unittest.main()


