from Bank_Class import Account
import numpy as np

Fede = Account('Fede', 'data.csv', skip_line= True)


Fede.data()
Fede.graph()


# Problems to fix

# the new september bin is added to the old one, need to distinguish or make more bins that have the same name
# better plotting ability and also graph should be prettier
# plotting of the savings account
# Better system for sifting through the different vendors that one does not want to include?
# Also ability for the user inside main to choose the proper vendors
# Also write about this stuff that you learned on the tablet