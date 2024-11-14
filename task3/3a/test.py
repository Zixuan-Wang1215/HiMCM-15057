import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from statsmodels.tsa.arima.model import ARIMA
# Reload the CSV file
filepath = pd.read_csv('task3/3a/tot_energysource_sep.csv')

# Original years and values
years = [1, 2, 3, 4, 5, 6]
values = [filepath['Bioenergy Percent'][i] for i in range(6)]

# Fit the ARIMA model
arima_model = ARIMA(values, order=(1, 1, 1))
arima_result = arima_model.fit()

# Predict future values for 2024-2028
future_years = [7, 8, 9, 10, 11]
predicted_values = arima_result.forecast(steps=5)

# Combine original and predicted values for plotting
extended_years = years + future_years
extended_values = list(values) + list(predicted_values)

# Plot original data and predictions
plt.plot(years, values, 'o', color='orange', label='Original Data')  # Original data in orange
plt.plot(future_years, predicted_values, 'o', color='blue', label='Predicted Data')  # Predicted data in blue

# Set x-axis labels to display all years
plt.xticks(extended_years)

plt.xlabel('Year')
plt.ylabel('Percentage in Total Energy(%)')
plt.title('Prediction of Bioenergy Percentage in Total Energy from 2018 to 2028 with ARIMA')
plt.legend()
plt.show()
#plt.savefig('predictions/Prediction of Bioenergy Percentage in Total Energy from 2018 to 2028.png', dpi=300, bbox_inches='tight')

# Print ARIMA model summary
print(arima_result.summary())