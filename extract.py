import pandas as pd

print("Extract data from MYSQL")

data = {
    "emp_id" = [1,2,3],
    "emp_name" = ["Vaibhav","Kiran","Avnish"],
    "salary" = [10000,20000,30000] }

df = pd.DataFrame(data)
print(df)