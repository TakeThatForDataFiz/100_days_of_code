"""
sqrl.py -- 
    sample pandas script that aggregates dataframe
    of central park squirrel population in 2018
    and outputs CSV of primary fur color
"""
import pandas as pd

# retrieve data from squirrel.csv w/in same directory
data = pd.read_csv("squirrel.csv")

# find count of gray squirrels using conditional data
grey_sqrls = len(data[data["Primary Fur Color"] == "Gray"])
red_sqrls = len(data[data["Primary Fur Color"] == "Cinnamon"])
blk_sqrls = len(data[data["Primary Fur Color"] == "Black"])

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_sqrls, red_sqrls, blk_sqrls],
}
df = pd.DataFrame(data_dict)
df.to_csv("Squirrel_count.csv")
