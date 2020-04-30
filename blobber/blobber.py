import requests
import json
import threading
import time

class BlobberServerError(Exception):
    pass

class Connection:
    def __init__(self, token):
        self.key = token
        self.url = "https://preview.blobber.ch/Blobdoge/"

    # returns Payment Object: address to pay to
    def createPurchase(self, price):
        address = self.createAddress()
        return Purchase(price, self, address)

    # Returns a Payment Object with existing address
    # Address needs be a dogecoin address created with blobber
    # It is *NOT* recommended to use this method
    def getPurchase(self, price, address):
        return Purchase(price, self, address)

    # Creates Dogecoin address
    # It is *NOT* recommended to use this method
    # but rather to use createPurchase which creates a Purchase object with a newly generated address.
    def createAddress(self):
        # generate address
        url = self.url + "devNewAddress"
        mydat = {'devtoken': self.key}
        r = requests.post(url, verify=False, data=mydat).text
        js = json.loads(r)

        if js["error"] != "none":
            raise BlobberServerError

        return js["address"]

class Purchase:
    # paidBalance               (float) -> Amount of money that has been payed to address
    # paidBalanceUnconfirmed    (float) -> Amount of money that has started being sent to your address
    # paymentComplete            (bool) -> transaction has been received?
    # paymentCompleteUnconfirmed (bool) -> transaction has started (but is maybe not complete)?
    def __init__(self, price, con, address):
        self.price = price
        self.con = con
        self.address = address

        self.paidBalance = 0
        self.paidBalanceUnconfirmed = 0
        self.paymentComplete = False
        self.paymentCompleteUnconfirmed = False

    # Executes a function when payment is receive
    # function needs to have 1 argument (uesed to pass the Payment object)
    def executeOnComplete(self, func):
        th = threading.Thread(target=self.__waitForPayment, args=(self, func))
        th.start()

    # refeshes paidBalance, paymentComplete, paidBalanceUnconfirmed and paymentCompleteUnconfirmed
    def refresh(self):
        url = self.con.url + "devInfoAddress"
        mydat = {'devtoken': self.con.key, 'address': self.address}
        r = requests.post(url, verify=False, data=mydat).text
        js = json.loads(r)

        if js["error"] != "none":
            raise BlobberServerError

        self.paidBalance = js["balance"]
        self.paidBalanceUnconfirmed = js["balanceUnconfirmed"]

        if self.paidBalance >= self.price:
            self.paymentComplete = True

        if self.paidBalanceUnconfirmed >= self.price:
            self.paymentCompleteUnconfirmed = True

    @staticmethod
    def __waitForPayment(payment, func):
        while not payment.paymentComplete:
            time.sleep(20)
            payment.refresh()
        func(payment)
