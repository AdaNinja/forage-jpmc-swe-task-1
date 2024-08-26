import unittest
from client3 import getDataPoint

class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

      # This is wrong because data structure of quote is:
      # quote = {
      #   'stock': 'ABC',
      #   'top_bid': {
      #     'price': 120.48,
      #     'size': 109
      #   },
      #   'top_ask': {
      #     'price': 121.2,
      #     'size': 36
      # self.assertEqual((getDataPoint(quote)),(quote['stock'], quote['bid_price'], quote['ask_price'], quote['price']))
      #   },
      #   'timestamp': '2019-02-11 22:06:30.572453',
      #   'id': '0.109974697771'
      # }



  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    for quote in quotes:
      self.assertEqual(getDataPoint(quote), (quote['stock'], quote['top_bid']['price'], quote['top_ask']['price'],
                                             (quote['top_bid']['price'] + quote['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  def test_getDataPoint_emptyQuate(self):
    quote = {}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_missingTopBid(self):
    quote = {'stock':'ABC', 'top_ask':{'price':121.1, 'size':23}}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_missingTopAsk(self):
    quote = {'stock': 'ABC', 'top_bid': {'price': 120.48, 'size': 109}}
    with self.assertRaises(KeyError):
      getDataPoint(quote)

  def test_getDataPoint_zeroPrice(self):
    quote = {
      'stock': 'ABC',
      'top_bid': {'price': 0.0, 'size': 109},
      'top_ask': {'price': 100.0, 'size': 36}
    }
    self.assertEqual(getDataPoint(quote), ('ABC', 0.0, 100.0, 50.0))


if __name__ == '__main__':
    unittest.main()
