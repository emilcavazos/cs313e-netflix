#TestNetflix.py

#imports

from io import StringIO
from unittest import main, TestCase
from Netflix import netflix_read, netflix_predict, netflix_return, rmse, netflix_solve

#-----------
#TestNetflix
#-----------

class TestNetflix(TestCase):

    #read

    def test_read_1(self):
        r = StringIO("13396")
        movie = netflix_read(r)
        self.assertEqual(movie, 13396)
    
    def test_read_2(self):
        r = StringIO("1234:\n432798")
        customer = netflix_read(r)
        self.assertEqual(customer, "1234:")

    def test_read_3(self):
        r = StringIO("6969:\n8008135")
        customer = netflix_read(r)
        self.assertEqual(customer, "6969:")

    #predict, remember to add more tests

    def test_predict(self):
        rate = netflix_predict(10,70987)
        self.assertEqual(rate, 3)

    #return

    def test_return(self):
        w = StringIO()
        netflix_return(w, 3)
        self.assertEqual(w.getvalue(), "3\n")

    #rmse

    def test_rmse(self):
        a = rmse([1,1,1], [2,2,2])
        self.assertEqual(a, 1)
        
    def test_rmse_2(self):
        a = rmse([1,1,1], [1,1,1])
        self.assertEqual(a, 0)

    def test_rmse_3(self):
        a = rmse([1.5,1.5,1.5], [2,2,2])
        self.assertEqual(a, .5)

    #solve

    def test_solve(self):
        r = StringIO("2048:\n13396\n987654\n456789")
        w = StringIO()
        netflix_solve(r, w)
        self.assertEqual(w.getvalue(), "2048:\n3\n3\n3")
        

main()
