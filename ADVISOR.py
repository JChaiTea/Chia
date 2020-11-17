import pandas


class advisor(object):
    """The advisor for the client"""
    def __init__(self, dataset, tickers):
        """Constructor"""
        self.data = dataset
        self.watclist = tickers

    def momentum(self):
        """Check the momentum of an equity"""
        aboveAvgs = {}
        for item in self.data:
            if type(self.data[item].mean()[0]) is not None:
                average = int(self.data[item].mean()[0])
                for num in self.data[item]:
                    print(num)
        return aboveAvgs


    def correlation(self):
        """Check the Correlation of equities"""
        pass

    def volatility(self):
        """Get the volatility recommendation for equities"""
        pass
