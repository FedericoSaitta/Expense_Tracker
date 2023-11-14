import csv
import matplotlib.pyplot as plt
import numpy as np

months = {
    '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
    '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
}


class Account:
    white_list = ['CARD_PAYMENT', 'TRANSFER', 'FEE', 'CARD_REFUND']

    black_list = ['To Univ Of Manchester', 'Depositing savings', 'Withdrawing savings',
                  'Cavendish Place', 'Manchester Su', 'Sp Ratta Us', 'Uom Student Fee', 'To Apex Self Storage',
                  'Stagecoach']

    cache = []

    def __init__(self, name, file):

        self.months = []
        self.name = name
        self.file = file

    def make_objects(self, month, year):
        name = month + year
        name = Transactions(self.file, month, year)
        self.months.append(name)

    def exclude_transactions(self, obj, *args):  # The args should be lists exclude_transaction( [], [], ...)
        for arg in args:
            if arg not in Account.cache:
                Account.cache.append(arg)
                obj.data.remove(arg)
        obj.compute_daily_payments()

    def graph(self, bar_chart=False):
        self.sort_objs()
        if bar_chart:
            bins = []
            y_values = []

            for obj in self.months:
                y_values.append(sum(obj.y))
                bins.append(months.get(obj.month) + ' ' + obj.year[2:])
            plt.title(f'Total money spent by {self.name} in each month')
            plt.bar(bins, y_values)

        else:                               # creates a cumulative plot
            for obj in self.months:
                cumulative = np.cumsum(obj.y)
                plt.plot(obj.x, cumulative, label=months.get(obj.month) + ' ' + obj.year[2:])

            plt.xlabel(f'Day of the month')
            plt.legend(loc="upper left")
            plt.title(f'Cumulative money by {self.name} over the month')

        plt.show()

    def sort_objs(self):
        print(self.months)
        self.months.sort(key=lambda x: int(x.month))
        self.months.sort(key=lambda x: int(x.year))


class Transactions:

    def __init__(self, file, month, year):

        self.file = file
        self.month = month
        self.year = year

        self.excluded_transactions = []



        self.__get_transactions()
        self.compute_daily_payments()

    def compute_daily_payments(self):
        self.x = [i for i in range(1, 32)]
        self.y = [0 for i in self.x]
        index = 0
        for i in self.x:
            while int(self.data[index][1][2]) == i:
                self.y[i - 1] -= float(self.data[index][0])
                if index == len(self.data) - 1:
                    break
                index += 1

    def __get_transactions(self):
        self.data = []
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            next(reader)                    # always skips the first line

            for row in reader:
                if ((row[3][:7]).split('-')) == [self.year, self.month]:
                    if row[0] in Account.white_list and (row[4] not in Account.black_list):
                        self.data.append([row[5], (row[3][:10]).split('-'), row[4]])
                    elif row[0] in Account.white_list:
                        self.excluded_transactions.append([row[5], (row[3][:10]).split('-'), row[4]])


    def __repr__(self):
        return self.month + '/' + self.year
