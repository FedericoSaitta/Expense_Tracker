from Bank_Class import Account

# Create the Account object with the file with all the transactions
Fede = Account('Fede', 'data.csv')


Fede.make_objects('09', '2023')
Fede.make_objects('05', '2023')
Fede.make_objects('03', '2023')
Fede.make_objects('10', '2022')
Fede.make_objects('09', '2022')



Fede.graph(bar_chart= True)





# program still assumes that all months have 31 days





# Advanced:
# Show vendors and signle transactions to be able to black_list them
# Add trend line
# implement interest rate with the time difference, note the savings values fluctuate
# For this you will need to calculate time passed by looking at dates
