from Bank_Class import Account

# Create the Account object with the file with all the transactions
Fede = Account('Fede', 'data.csv')

# Create a month object for each month that you want to track
Fede.make_objects('09', '2023')
Fede.make_objects('05', '2023')
Fede.make_objects('03', '2023')
Fede.make_objects('10', '2022')
Fede.make_objects('09', '2022')

# Plot the objects, together or separately
Fede.graph(bar_chart= True)
