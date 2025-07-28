import pandas
import csv

data = pandas.read_csv('data.csv')

red_fur_color = len(data[data['Primary Fur Color'] == 'Cinnamon']) 

gray_fur_color = len(data[data['Primary Fur Color'] == 'Gray']) 

black_fur_color = len(data[data['Primary Fur Color'] == 'Black']) 

data_dic = {
    "Fur Color": ["Red", "Gray", "Black"],
    "Count": [red_fur_color, gray_fur_color, black_fur_color]
}

df = pandas.DataFrame(data_dic)

df.to_csv('squirrel_count.csv')