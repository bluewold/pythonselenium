import ddt
import unittest
@ddt.ddt
class DataTest(unittest.TestCase):
    def setUp(self):
        print("这个是setup")

    def tearDown(self):
        print("这个是teardown")
    @ddt.data(
        ["1","2"],
        ["3","4"]
    )
    @ddt.unpack
    def test_add(self,a,b):
        print(a+b)

if __name__  == "__main__":
    unittest.main()