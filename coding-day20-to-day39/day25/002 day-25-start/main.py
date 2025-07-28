# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
import pandas 
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     tempertures = []
#     for row in data:
#         if row[1] != "temp":
#             tempertures.append(int(row[1]))
#     print(tempertures)

pandas_data = pandas.read_csv("weather_data.csv")
# print(pandas_data)
# print(pandas_data["temp"])

dic = pandas_data.to_dict()
# print(dic)

# temps = dic['temp'].values()  # Get all temperature values
# average_temp = sum(temps) / len(temps)
# print(average_temp)

# Get the average temperature 
# print(pandas_data["temp"].mean())

# print(pandas_data["temp"].max())

# print(pandas_data[pandas_data.temp == pandas_data.temp.max()])

monday = pandas_data[pandas_data.day == "Monday"]

# covert monday temp to Fahrenheit
monday_temp_f = (monday.temp * 9/5) + 32
print(monday_temp_f)



