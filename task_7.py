## sales Analysis
import numpy as np

## Create a NumPy array of sales data
sales = np.array([1200,1500,900, 2000, 1800, 1700, 1600])


tot_week_sales = np.sum(sales)  

average_daily_sales = np.mean(sales)

highest_sales = np.max(sales)

lowest_sales = np.min(sales)

std_daviation = np.std(sales) 

above_avg_sale = np.sum(sales > average_daily_sales)

## Print the results
print("Total weekly sales: ", tot_week_sales)
print("Average daily sales: ", average_daily_sales)
print("Highest sales: ", highest_sales)
print("Lowest sales: ", lowest_sales)
print("Standard deviation of sales: ", std_daviation)
print("Number of days with above average sales: ", above_avg_sale)

