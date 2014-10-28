class Transaction:
        def __init__(self, item):
                self._item = item
                self._seller = item.getseller()
                self._highBidder = None
                self._highBid = item.getstart()
                
        def getItem(self):
                return self._item
                
        def setItem(self, item):
                self._item = item
                
        def getSeller(self):
                return self._seller
                
        def setSeller(self, seller):
                self._seller = seller
                
        def submitBid(self, buyer, bid):
                if(bid > self._highBid):
                        self._highBidder = buyer
                        self._highBid = bid
                
        def setHighBid(self, bid):
                self._highBid = bid

        def getHighBid(self):
                return self._highBid
                
