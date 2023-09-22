import csv
import matplotlib.pyplot as plt

months = {
    '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
    '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
}

class Account:

    white_list = ['CARD_PAYMENT', 'TRANSFER', 'FEE', 'CARD_REFUND']

    black_list = ['To Univ Of Manchester', 'Depositing savings', 'Withdrawing savings',
                   'Cavendish Place', 'Manchester Su', 'Sp Ratta Us', 'Uom Student Fee', 'To Apex Self Storage',
                  'Stagecoach']


    def __init__(self, name, file, skip_line = False):

        self.months = []

        self.name = name
        self.file = file
        self.skip_line = skip_line

        self.payments = [] # This also contains positive transfers made to you

        # To be implemented
        self.savings = []
        self.top_ups = []

        self.cache = []  # THe cache should store specific payments that the user does not want to take into account

        self.__compute() # When account is generated then it will automatically compute, maybe needs fixing


    def get_transactions(self, month, year):
        transactions = []
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            if self.skip_line:
                next(reader)

            for row in reader:
                if ((row[3][:7]).split('-')) == [year, month]:
                    if row[0] in Account.white_list and (row[4] not in Account.black_list):
                        if [row[5], (row[3][:10]).split('-'), row[4]] not in self.cache:
                            transactions.append([row[5], (row[3][:10]).split('-'), row[4]])
        return transactions

    def exclude_transactions(self, *args):   # The args should be lists exclude_transaction( [], [], ...)
        for arg in args:
            if arg not in self.cache:
                self.cache.append(arg)

    def make_attributes(self, month, year):
        head = year + '/' + month
        self.head = []
        self.months.append(head)
        return self.head

# This is a good start need to clean up the code significantly but this is a smart way to acces the possible month 
# attributes without creating them too ahead of time

    def set_set(self, month, year):
        head = year + '/' + month
        if head in self.months:
            self.head.append(0)
            return self.head

# You could create account objects, each monthly span is an attribute, from that i can print each attribute and remove
# any unecessay valuies and i can plot them side by side
# I should also have a yearly graph as back up in general


    def graph(self):  # I should also create a way to plot data just over the month
        plt.bar(self.bins, self.yvalues)
        plt.show()  # At one point change to saving the pictures in a correct width size

    def __compute(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            if self.skip_line:
                next(reader)

            for row in reader:
                if row[0] in Account.white_list and (row[4] not in Account.black_list):
                    self.payments.append((float(row[5]) + float(row[6]), (row[3][:10]).split('-')))

          #      if (row[4] == 'Depositing savings' or row[4] == 'Withdrawing savings'):
         #           self.savings.append( (float(row[5]) * -1, (row[3][:10]).split('-') ))


    def yearly_data(self):
        self.yvalues = []
        self.bins = []
        index = 0
        lst = self.payments
        j = 0
        results = []

        for i in range(13):  # the time period we want to assess
            month = months.get(lst[j][1][1])
            if i % 12 == 0:
                self.bins.append(month + '' + lst[j][1][0])  # This works for now if graph is large enough width wise
            else:
                self.bins.append(month)

            self.yvalues.append(0)

            while lst[j][1][1] == lst[j + 1][1][1] and j < len(lst) - 2:
                self.yvalues[i] += lst[j][0]
                j += 1

            self.yvalues[i] += lst[j][0]  # Done so the last element when the condition fails is also added to the list
            self.yvalues[i] = self.yvalues[i] * -1 # Negating values as we look at money spent
            j += 1            # Done so it does not get stuck and goes over to the next month
