import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import requests

arr = np.arange(1, 11)  
mean_value = np.mean(arr)
print("NumPy Array:", arr)
print("Mean:", mean_value)


data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 22, 27],
    'Score': [88, 92, 95, 85]
}
df = pd.DataFrame(data)
print("\nPandas DataFrame:\n", df)
print("\nSummary Statistics:\n", df.describe())


response = requests.get('the link to send or recive the requets')
if response.status_code == 200:
    bitcoin_data = response.json()
    usd_price = bitcoin_data['bpi']['USD']['rate']
    print("\nBitcoin Price in USD:", usd_price)
else:
    print("\nFailed to fetch data from the API.")


x = [1, 2, 3, 4, 5]
y = [10, 20, 15, 30, 25]

plt.plot(x, y, marker='o', linestyle='-', color='blue')
plt.title("Simple Line Graph")
plt.xlabel("X values")
plt.ylabel("Y values")
plt.grid(True)
plt.show()
