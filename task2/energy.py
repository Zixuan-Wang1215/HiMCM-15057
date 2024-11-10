import pandas as pd
csv1=pd.read_csv('task2/used_csv/totenergy.csv')
csv2=pd.read_csv('task2/used_csv/energysource.csv')
newcsv=pd.DataFrame({
    'Country':csv1['Country'], 
    'Total Energy':csv1['Total Energy'],
    'Electricity from solar - TWh':csv2['Electricity from solar - TWh'] ,
    'Electricity from wind - TWh':csv2['Electricity from wind - TWh'],
    'Electricity from hydro - TWh':csv2['Electricity from hydro - TWh'],
    'Electricity from nuclear - TWh':csv2['Electricity from nuclear - TWh'] ,
    'Electricity from oil - TWh':csv2['Electricity from oil - TWh'] ,
    'Electricity from gas - TWh':csv2['Electricity from gas - TWh'] ,
    'Electricity from coal - TWh':csv2['Electricity from coal - TWh'] ,

})

newcsv.to_csv('energy1.csv', index=False)