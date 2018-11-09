import unittest
from models import newssource
Newssource = newssource.Newssource

class NewssourceTest(unittest.TestCase):
    """
    Test Class to test the behaviour of the Newssource class

    """

    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.new_newssource = Newssource(self,null,"Newsbtc.com","https://s3.amazonaws.com/main-newsbtc-images/2018/05/07074035/techanalysis-ada.jpg","2018-11-09T08:28:57Z", "https://www.newsbtc.com/2018/11/09/cardano-price-analysis-ada-usd-could-correct-towards-0-075/")
    
    def test_instance(self):
        self.assertTrue(isinstance(slef.new_newssource,Newssource))
if __name__ == '__main__':
    unittest.main()