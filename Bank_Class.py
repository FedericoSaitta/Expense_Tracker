import csv
import matplotlib.pyplot as plt


class Account:

    interest_rate = 1 # In %

    months = {
        '01': 'Jan', '02': 'Feb', '03': 'Mar', '04': 'Apr', '05': 'May', '06': 'Jun',
        '07': 'Jul', '08': 'Aug', '09': 'Sep', '10': 'Oct', '11': 'Nov', '12': 'Dec'
    }

    allowed_values = ['CARD_PAYMENT', 'TRANSFER', 'FEE', 'CARD_REFUND']

    not_allowed = [
                   ]


    def __init__(self, name, file, skip_line = False):

        self.name = name
        self.file = file
        self.skip_line = skip_line


        self.savings = []
        self.payments = [] # This also contains positive transfers made to you
        self.top_ups = [] # Have not implemented this yet

        self.__compute()


    def __compute(self):
        with open(self.file, 'r') as f:
            reader = csv.reader(f)
            if self.skip_line:
                next(reader)

            for row in reader:
                if row[0] in Account.allowed_values and (row[4] not in Account.not_allowed):
                    self.payments.append((float(row[5]) + float(row[6]), (row[3][:10]).split('-')))

                if (row[4] == 'Depositing savings' or row[4] == 'Withdrawing savings'):
                    self.savings.append( (float(row[5]) * -1, (row[3][:10]).split('-') ))


    def data(self):
        self.yvalues = []
        self.bins = []
        index = 0
        lst = self.payments
        j = 0
        results = []

        for i in range(12):  # the time period we want to assess
            self.bins.append(Account.months.get(lst[j][1][1]))
            self.yvalues.append(0)

            while lst[j][1][1] == lst[j + 1][1][1] and j < len(lst) - 2:
                self.yvalues[i] += lst[j][0]
                j += 1

                if i == 6:
                    print(lst[j][0])


            self.yvalues[i] += lst[j][0]  # Done so the last element when the condition fails is also added to the list
            self.yvalues[i] = self.yvalues[i] * -1 # Negating values as we look at money spent
            j += 1            # Done so it does not get stuck and goes over to the next month


    def graph(self):
        plt.bar(self.bins, self.yvalues)
        plt.show()
